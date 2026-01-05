from pydantic import BaseModel

class Address(BaseModel):
    city:str
    province: str
    pincode: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city':'Hyderabad','province':'Sindh','pincode':'7000'}
address1 = Address(**address_dict)

patient_dict = {'name':'Hasnain','gender':'Male','age':22,'address':address1}
patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.city)
print(patient1.address.province)