from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str


class patient(BaseModel):
    name:str
    gender:str
    age:str
    address:Address

address_dict={'city':'gurgaon','state':'haryana','pin':'122002'}

address1=Address(**address_dict)

patient_dict={'name':'nitish','gender':'male','age':'35','address':address1}


patient1=patient(**patient_dict)


print(patient1.name)
print(patient1)
print(patient1.address)