from sqlalchemy import create_engine, Column, Integer, String, Date
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    check_in = Column(Date)
    check_out = Column(Date)
    room_type = Column(String)

DATABASE_URL = os.getenv("DATABASE_URL")  # Получаем URL базы из переменной окружения
if not DATABASE_URL:
    raise ValueError("Ошибка: DATABASE_URL не задан!")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Функция сохранения бронирования
def save_booking(user_id, check_in, check_out, room_type):
    session = SessionLocal()
    new_booking = Booking(
        user_id=user_id,
        check_in=check_in,
        check_out=check_out,
        room_type=room_type
    )
    session.add(new_booking)
    session.commit()
    session.refresh(new_booking)
    session.close()
    return new_booking

# ✅ Функция для инициализации БД
def init_db():
    Base.metadata.create_all(engine)
