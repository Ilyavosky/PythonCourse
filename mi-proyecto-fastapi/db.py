from typing import Annotated
from sqlmodel import Session, create_engine
from fastapi import Depends, FastAPI
from sqlmodel import SQLModel


sqlite_name = "db.sqlite3"
sqlite_url= f"sqlite:///{sqlite_name}"

engine =create_engine(sqlite_url)

def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield #Le pasamos el control a fastapi para que ejecute la función

#Método para obtener una sesión de Base de datos
#Usamos un context processor, variable que nos permite usar variables dde otras clases internamente
def get_session():
    with Session(engine) as session:
        yield session
        
SessionDep = Annotated[Session, Depends(get_session)]     
        