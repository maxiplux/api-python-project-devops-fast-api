from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
import os


#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app2.db"


url = URL.create(
    drivername="postgresql",
    username=os.environ.get('DB_USERNAME', 'postgres'),
    password=os.environ.get('DB_PASSWORD', 'postgres'),
    host=os.environ.get('DB_HOST', 'LOCALHOST'),
    database=os.environ.get('DB_NAME', 'postgres'),
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()