# def insert_patient_data(name:str,age:int):
#   if type(name)==str and type(age)==int:
#     print(name)
#     print(age)
#     print("insert into databases")
#   else:
#     raise TypeError("inccorect data type")

# insert_patient_data('gopal',30)




# def update_patient_data(name:str,age:int):
#   if type(name)==str and type(age)==int:
#     if age<0:
#       raise ValueError("age can't be negative ")
#     else:
#         print(name)
#         print(age)
#         print(" updated to databases")
#   else:
#     raise TypeError("inccorect data type")

# update_patient_data('gopal',87)
# # from pydantic import Basemodel


# # class pat


from pydantic import  BaseModel,EmailStr,AnyUrl,Field

from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : Annotated[str,Field(max_length=50,title="name of the patient",description='Give patient name of the pateint in less than 50 chars',examples=['nitish','amit'])]
    email:EmailStr
    linkedin:AnyUrl
    age : int=Field(gt=0,lt=120)
    weight:Annotated[float,Field(gt=0,strict=True)]
    married:bool
    allergies:Optional[List[str]]=Field(default=None,max_length=5)
    contact_details:Dict[str,str]


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')






def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')



patient_info={'name':'nitish','email':'gopal@123gmail.com','linkedin':'https://www.linkedin.com/feed','age':'30','weight':75.2,'married':True,
              'allergies':['pollen','dust'],'contact_details':{'675844':'969555'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)

update_patient_data(patient1)







