from sqlmodel import create_engine, SQLModel
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///./test.db"



engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

