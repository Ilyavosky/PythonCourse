import zoneinfo
from datetime import datetime
from fastapi import FastAPI, status, HTTPException
from models import Customer, Transaction, Invoice, CustomerCreate
from timezonesDictionary import country_timezones
from db import SessionDep, Session, create_all_tables
from sqlmodel import select

app = FastAPI(lifespan=create_all_tables)


@app.get("/")
async def root():
    return {"message": "Hola Soy Ilya jeje, este es mi primer hola mundo en Python con FastAPI ٩(˘◡˘)۶"}

#Método GET para conocer el país con su zona horaria
@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    if timezone_str is None:
        return {"error": "Código de país no válido"}
    else:
        tz = zoneinfo.ZoneInfo(timezone_str)
        return {"timezone": timezone_str,
                "time": datetime.now(tz)}

#Método GET para conocer el país con su zona horaria más legible        
@app.get("/timeFormat/{iso_code}")
async def timeformat(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    if timezone_str is None:
        return{"error": "Código de país no valido"}
    else:
        tz = zoneinfo.ZoneInfo(timezone_str)
        date_object  = datetime.strftime(datetime.now(tz), "%Y-%m-%d %H:%M:%S")
        return {"timezone": timezone_str,
                "time": date_object}    

#Métood POST para crear a un usuario, recibe información del modelo "CustomerCreate" y responde con el modelo Customer para el ID
@app.post("/customers", response_model= Customer) #FastAPI nos permite responder con otro modelo, en este caso "Customer"
async def create_customer(customer_data: CustomerCreate, session: SessionDep): #CustomerCreate es el modelo que nos permite recibir datos
    customer = Customer.model_validate(customer_data.model_dump())#Se le debe pasar un diccionario para validar
    session.add(customer)
    session.commit() #En SQLModel cuando queremos ejeuctuar queries debemos hacer un commit, eso significa que se esta ejecutando en nuestro engine automaticamente
    session.refresh(customer)
    return customer


@app.get("/customers", response_model= list[Customer])
async def list_customer(session: SessionDep):
    session.exec(select(Customer)).all()
    return session.exec(select(Customer)).all()

@app.get("/customers/{id}", response_model=Customer)  # status_code por defecto es 200
async def get_by_id(session: SessionDep, id:int):
    customer = session.get(Customer, id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer

@app.post("/transactions")
async def create_customer(transaction_data: Transaction):
    return transaction_data

@app.post("/invoices")
async def create_customer(invoice_data: Invoice):
    return invoice_data