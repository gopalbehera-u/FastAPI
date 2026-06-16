
from pydantic import  BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field

from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : str
    email:EmailStr
    linkedin:AnyUrl
    age : int
    height:float
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @computed_field
    @property
    def calculated_bmi(self) -> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi




def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.calculated_bmi)
    print('inserted')





patient_info={'name':'nitish','email':'gopal@hdfc.com','linkedin':'https://www.linkedin.com/feed','age':'30','height':1.64,'weight':75.2,'married':True,
              'allergies':['pollen','dust'],'contact_details':{'675844':'969555'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)

