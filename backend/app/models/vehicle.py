from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key = True, index = True)
    make = Column(String, index = True, nullable = False)
    model = Column(String, index = True, nullable = False)
    year = Column(Integer, index = True, nullable = False)

    parts = relationship("Part", back_populates="vehicles")
