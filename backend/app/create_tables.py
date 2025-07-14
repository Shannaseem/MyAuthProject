# create_tables.py

from app.database import Base, engine
from app.models import User  # import all your models here

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
