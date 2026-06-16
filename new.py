
from pydantic import  BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator

from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : str
    email:EmailStr
    linkedin:AnyUrl
    age : int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @model_validator(mode='after')
    def validate_emargecy_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('patient older than 60 must have an emergency contact')
        return model







def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')





patient_info={'name':'nitish','email':'gopal@hdfc.com','linkedin':'https://www.linkedin.com/feed','age':'30','weight':75.2,'married':True,
              'allergies':['pollen','dust'],'contact_details':{'675844':'969555'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)
