from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    age: int = Field(gt=0)
    email: EmailStr
    linked_In: AnyUrl
    weight: float
    height: float = Field(gt=0)
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self)-> float:
        calculated_bmi = self.weight/(self.height**2)
        return calculated_bmi



patient_info = {"name": "Hasnain", 'age': 22,'weight':52, 'email':'sh@gmail.com','linked_In':'https://linkedin.com/12345','height': 1.75, 'contact_details': {'email':'abc@gmail.com','phone':'03126641280'}}

patient1 = Patient(**patient_info)

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linked_In)
    print(patient.bmi)


insert_patient(patient1)
