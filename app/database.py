from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

POSTGRESQL_URL="postgresql://pharmacy_3dgv_user:i6nnfzm94GgFX1lR1BYqkcJThFZPa32P@dpg-cnhhko7jbltc73a82qkg-a.oregon-postgres.render.com/pharmacy_3dgv"

engine=create_engine(POSTGRESQL_URL)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally: 
        db.close()


