from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    check_in = Column(Date)
    check_out = Column(Date)
    room_type = Column(String)

def init_db():
    engine = create_engine(os.getenv("DATABASE_URL"))
    Base.metadata.create_all(engine)