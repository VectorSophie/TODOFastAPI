from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "blank"

engine = create_engine(
    DATABASE_URL,
    echo=True  # SQL 로그 보고 싶으면 True, 과제 끝나면 False
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
