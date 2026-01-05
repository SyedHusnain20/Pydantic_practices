from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    age: int = Field(gt=0)
    email: EmailStr
    linked_In: AnyUrl
    height: float = Field(gt=0)
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def emergency_contact_validator(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have emergency contact ')
        return model


patient_info = {"name": "Hasnain", 'age': 70, 'email':'sh@gmail.com','linked_In':'https://linkedin.com/12345','height': 190, 'contact_details': {'email':'abc@gmail.com','phone':'03126641280', 'emergency':'01234567890'}}

patient1 = Patient(**patient_info)

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linked_In)


insert_patient(patient1)
