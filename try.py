from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def default():
    return {'message ':'hii how can i help you '}


@app.get("/name")
def name():
    name=input("Enter your name : ")
    return {"message" : f"your is {name}"}

@app.get("/course")
def course():
    coursename=input("Enter your course name : ")
    return {'message ':f"you r purshing {coursename} course"}