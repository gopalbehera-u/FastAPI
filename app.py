import json
from fastapi import FastAPI

app=FastAPI()


def loaddata():
    with open('pateint.json','r') as f:
        data=json.load(f)
    return data

@app.get('/')
def hello():
    return {'message':'patient managment system API'}

@app.get('/about')
def about():
    return {"message" : "A fullly functional API to manage your patient records"}

@app.get("/view")
def view():
    data=loaddata()
    return data 