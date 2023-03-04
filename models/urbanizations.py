from os import getenv
from typing import Optional
from datetime import datetime
from dotenv import load_dotenv
from sqlmodel import Field, create_engine, SQLModel

load_dotenv()
todaysDate: datetime = datetime.now()
environment = getenv("ENVIRONMENT")
db_name = getenv("DB_NAME")
showEcho = environment == "development"
sqlite_url = f"sqlite:///{db_name}"
DATABASE_URL = f"mysql://sql10600900:9TxITNv2zb@sql10.freesqldatabase.com/sql10600900"

class Urbanizations(SQLModel, table=True):
    urbanizationId: Optional[str] = Field(default=None, primary_key=True, nullable=False)
    urbanizationName: str = Field(default=None, nullable=False)
    urbanizationAdminName: str = Field(default=None, nullable=False)
    urbanizationRucNumber: str = Field(default=None, nullable=False)
    urbanizationPhoneNumber: str = Field(default=None, nullable=True)
    urbanizationAddress: str = Field(default=None, nullable=False)
    urbanizationResidentialsNumber: int = Field(default=0, nullable=False)

class Residentials(SQLModel, table=True):
    residentialId: Optional[str] = Field(default=None, primary_key=True, nullable=False)
    residentialCreationDate: datetime = Field(default=todaysDate, nullable=False)
    residentialAddress: str = Field(default=None, nullable=False)
    residentialAdminId: str = Field(default=None, nullable=False)
    residentialUpToDate: bool = Field(default=False, nullable=False)
    urbanization_Id: Optional[str] = Field(default=None, foreign_key="urbanizations.urbanizationId")

class Residents(SQLModel, table=True):
    residentId: str = Field(default=None, primary_key=True, nullable=False)
    residentCreationDate: datetime = Field(default=todaysDate, nullable=False)
    residentName: str = Field(default=None, nullable=False)
    residentSurename: str = Field(default=None, nullable=False)
    residentPhoneNumber: str = Field(default=None, nullable=False)
    residential_Id: str = Field(default=None, foreign_key="residentials.residentialId")

engine = create_engine(sqlite_url, echo=showEcho, encoding="latin1")
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)