from fastapi import APIRouter
from routes.WebsocketsRoute import websocketRoute
from routes.HelloRoute import helloRoute

router = APIRouter()
router.include_router(helloRoute, tags=["Authentication"])
router.include_router(websocketRoute, tags=["Websocket"])