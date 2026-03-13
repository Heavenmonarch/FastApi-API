from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastAPIProject', 
        user='postgres', password='Ayanfe12!!', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("error:", error)
        time.sleep(5)

        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
        

# Landing page route
@app.get("/")
def root():
    return {"status": "okay",
            "process": "working",
            "message": "welcome to my API"}


