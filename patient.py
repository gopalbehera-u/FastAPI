print("PATIENT FILE LOADED")
import json
from fastapi import FastAPI,Path,HTTPException,Query

app = FastAPI()

def loaddata():
    with open("pateint.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "patient management system API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records"}

@app.get("/view")
def view():
    data = loaddata()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str=Path(...,description='ID of the pateint in the DB ',example='P001')):
    data = loaddata()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404,detail='Pateint not found ')


@app.get('/sort')
def sort_patients(sort_by  :str=Query(...,description='sort on the basis of height ,weight or bmi'),order:str=Query('asc',description='sort in asc or desc order ')):
    valid_field=['height','weight','bmi']

    if sort_by not in valid_field:
        raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_field}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order between asc and desc')
    data=loaddata()
    sort_order=True if order=='desc' else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data