from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()  # Загрузка переменных из .env

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL не задан!")

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    check_in = Column(Date)
    check_out = Column(Date)
    room_type = Column(String)

def init_db():
    Base.metadata.create_all(engine)

# database.py
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=engine)

def save_booking(user_data):
    session = Session()
    booking = Booking(
        user_id=user_data['user_id'],
        check_in=user_data['check_in'],
        check_out=user_data['check_out'],
        room_type=user_data['room_type']
    )
    session.add(booking)
    session.commit()
    session.close()