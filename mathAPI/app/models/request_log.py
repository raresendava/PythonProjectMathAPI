from sqlalchemy import Column, Integer, String, JSON, DateTime
from datetime import datetime
from app.db.database import Base

class RequestLog(Base):
    __tablename__ = "request_logs"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    operation = Column(String)
    input_data = Column(JSON)
    result = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)