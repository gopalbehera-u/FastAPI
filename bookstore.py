from fastapi import FastAPI,HTTPException,Path

import json

app=FastAPI()


def loaddata():
    with open('bookstore.json','r') as f:
        data=json.load(f)
    return data


@app.get('/')
def hello():
    return {'message':'welcome to our book store '}


@app.get('/books')
def bookname():
    return loaddata()







@app.get('/books/filter')
def filter_books(
    title: str = None,
    author: str = None,
    category: str = None
):
    data = loaddata()

    filtered_books = {}

    for book_id, book in data.items():

        if title and book['title'].lower() != title.lower():
            continue

        if author and book['author'].lower() != author.lower():
            continue

        if category and book['category'].lower() != category.lower():
            continue

        filtered_books[book_id] = book

    if not filtered_books:
        raise HTTPException(
            status_code=404,
            detail='No books found'
        )

    return filtered_books

@app.get('/books/{book_id}')
def get_book(book_id:str=Path(description="Unique Book ID")):
    data=loaddata()
    if book_id in data:
        return data[book_id]
    raise HTTPException(
        status_code=404,
        detail='Book not found'
    )
