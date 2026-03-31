from pydantic import BaseModel, EmailStr, Field

#Modelo para validar en un endpoint, hereda de BaseModel
class CustomerBase(BaseModel):
    name: str
    #Descripción opcional
    description: str | None
    email: EmailStr
    age: int

class CustomerCreate(CustomerBase): #Herencia de la clase CustomerBase
    pass #pass es una instrucción nula que no hace nada cuando se ejecuta
    
class Customer(CustomerBase):    
    id: int | None = None
   
    
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