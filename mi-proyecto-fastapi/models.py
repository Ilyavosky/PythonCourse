from pydantic import BaseModel, EmailStr, Field
from sqlmodel import SQLModel, Field

#Modelo para validar en un endpoint, hereda de BaseModel
class CustomerBase(SQLModel):
    name: str = Field(default= None)
    #Descripción opcional
    description: str | None = Field(default= None)
    email: EmailStr = Field(default= None)
    age: int = Field(default= None)

class CustomerCreate(CustomerBase): #Herencia de la clase CustomerBase
    pass #pass es una instrucción nula que no hace nada cuando se ejecuta
    
class Customer(CustomerBase, table = True):    
    id: int | None = Field(default= None, primary_key= True)
   
    
class Transaction(BaseModel):
    id: int
    ammount: int
    description: str


class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int
    
    @property
    def ammount_total(self):
        return sum(transaction.ammount for transaction in self.transactionsS)