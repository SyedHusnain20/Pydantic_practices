from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Patient's name ", description='Enter the patients name here ', examples=['Hasnain','Ali'])]
    age: int = Field(gt=0)
    email: EmailStr
    linked_In: AnyUrl
    height: float = Field(gt=0)
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

patient_info = {"name": "Hasnain", 'age': 22, 'email':'sh@gmail.com','linked_In':'https://linkedin.com/12345','height': 190, 'contact_details': {'email':'abc@gmail.com','phone':'03126641280'}}

patient1 = Patient(**patient_info)

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linked_In)


insert_patient(patient1)
