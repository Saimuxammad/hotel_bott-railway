from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError

# Загружаем .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL не найден! Проверьте настройки Railway.")

# Приводим `postgres://` к `postgresql://`, если это необходимо
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Подключаемся к базе
engine = create_engine(DATABASE_URL, echo=True)
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(100), nullable=False)
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    room_type = Column(String(50), nullable=False)

def init_db():
    """Создаем таблицы"""
    try:
        print("🔄 Создание таблиц...")
        Base.metadata.create_all(engine)
        print("✅ Таблицы успешно созданы!")
    except SQLAlchemyError as e:
        print(f"❌ Ошибка при создании таблиц: {e}")
        raise

def save_booking(user_data):
    """Сохранение бронирования в базе данных"""
    session = Session()
    try:
        booking = Booking(
            user_id=user_data['user_id'],
            check_in=user_data['check_in'],
            check_out=user_data['check_out'],
            room_type=user_data['room_type']
        )
        session.add(booking)
        session.commit()
        print("✅ Бронирование успешно сохранено!")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"❌ Ошибка при сохранении бронирования: {e}")
    finally:
        session.close()

# Проверяем подключение
try:
    with engine.connect() as conn:
        print("✅ База данных доступна!")
except Exception as e:
    print(f"❌ Ошибка при подключении к базе: {e}")
