
from pydantic import  BaseModel,EmailStr,AnyUrl,Field,field_validator

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


    @field_validator('age',mode='after')
    @classmethod
    def valid_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")


    @field_validator('name')
    @classmethod
    def name_transform(cls,value):
        return value.upper()


    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icic.com']
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')
        return value

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')





patient_info={'name':'nitish','email':'gopal@hdfc.com','linkedin':'https://www.linkedin.com/feed','age':'30','weight':75.2,'married':True,
              'allergies':['pollen','dust'],'contact_details':{'675844':'969555'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)

