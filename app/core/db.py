import os

from dotenv import load_dotenv
# app/core/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@localhost:3306/llmagent?charset=utf8mb4"

engine = create_engine(
  DATABASE_URL,
  echo=False,
  pool_size=5,
  max_overflow=10,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_conn():
  return SessionLocal()


def release_conn(conn):
  conn.close()