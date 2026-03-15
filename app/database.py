from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Ayanfe12!!@localhost/fastAPIProject'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


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



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()