from fastapi import FastAPI, Query

from typing import Optional

app = FastAPI()

@app.get("/books")
def read_books(test: Optional[str] = Query(None, min_length=3, max_length=10)):
    results = {"books": [{"book_name": "The Great Hunt"}, {"book_name": "The Dragon Reborn"}]}

    if test:
        results.update({"test": test})
    
    return results