from dotenv import load_dotenv
from pydantic import BaseModel
from utils.logging import Logging
from fastapi import APIRouter, Request, Response, BackgroundTasks
from schemas.auth_post_request import Auth_post_request
from controllers.Hello_controller import Hello_Controller
from schemas.transversal_schemas import GeneralResponse
import os, requests, json, uuid, hmac, hashlib

helloRoute = APIRouter()
load_dotenv()

class Data(BaseModel):
    algo: int

def manage_data_os(data: str, flagged: bool) -> bool:
    my_final_list = list()
    data_catched = [x for x in enumerate(data) if x.startwith("m")]
    for v, _i in enumerate(data_catched):
        if flagged: my_final_list.append(v)
    if len(my_final_list) != 0: return True
    return False

@helloRoute.post("/testing/", response_model=GeneralResponse)
async def testing_route(
    data: Data, 
    req: Request, 
    res: Response, 
    back_tasks: BackgroundTasks
) -> GeneralResponse:
    try:
        if req.method == "POST":
            signature = req.headers["x-signature"] # Get HMAC signature from client
            final = json.dumps(data.dict()).encode("utf-8") # Serialize JSON to string and encode to UTF-8
            final_key = str.encode(os.getenv("HMAC_KEY")) # Encode HMAC key
            hashed = hmac.new(final_key, final, hashlib.sha256).hexdigest() # Create the HMAC SHA256 hash
            back_tasks.add_task(manage_data_os, hashed, True)
            response = requests.get("https://dummyjson.com/products/1").json()
            if signature == hashed:
                final_res = GeneralResponse(
                    success=True, 
                    error=None, 
                    data=None
                )
                res_enc = json.dumps(final_res.dict()).encode("utf-8")
                res_hash = hmac.new(final_key, res_enc, hashlib.sha256).hexdigest()
                res.headers["x-signature"] = res_hash
                return final_res
            else: 
                return GeneralResponse(
                    success=False, 
                    error="HMAC_ERR", 
                    data=None
                )
        else: raise Exception("")
    except OSError as error:
        logger = Logging(error, 400)
        logger.save_log()
        return GeneralResponse(
            success=False, 
            error=error, 
            data=None
        )