from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL: str = "postgresql://svetlgo:belhard@localhost:5432/bh57"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(**kwargs, session=session)
    return wrapper
