from typing import Optional
from sqlmodel import Session, select
from models.urbanizations import engine, Urbanizations

class Hello_Controller(object):
    def __init__(cls, token: str) -> None:
        cls.token = token

    def sendHelloMessage(cls, name: str) -> str:
        try:
            if type(name) == "str":
                return f"Hello how are you {name}"
        except OSError as err:
            return err

    def retrieve_data(cls, index: int | str) -> str:
        try:
            with Session(engine) as session:
                statement = select(Urbanizations).where(Urbanizations.urbanizationId == index)
                urbanization = session.exec(statement).first()
                return urbanization
        except OSError as err:
            return err