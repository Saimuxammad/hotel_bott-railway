from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL не найден!")

# Маскировка пароля для вывода
masked_url = DATABASE_URL.replace(DATABASE_URL.split(':')[2].split('@')[0], '*****')
print(f"✅ DATABASE_URL: {masked_url}")

# Движок с SSL
load_dotenv()
engine = create_engine(
    os.getenv("DATABASE_URL"),
    connect_args={'client_encoding': 'utf8'}  # Явное указание кодировки <button class="citation-flag" data-index="2">
)

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
    try:
        print("🔄 Создание таблиц...")
        Base.metadata.create_all(engine)
        print("✅ Таблицы созданы!")
    except SQLAlchemyError as e:
        print(f"❌ Ошибка: {e}")
        raise

if __name__ == "__main__":
    init_db()


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

# В database.py
try:
    engine.connect()
    print("✅ База данных доступна!")
except Exception as e:
    print(f"❌ Ошибка: {e}")
