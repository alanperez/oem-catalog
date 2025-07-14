from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Part(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True, nullable = False)
    oem_number = Column(String, index = True, nullable = False)
    sku = Column(String, index = True, nullable = False)
    manufacturer = Column(String, index = True, nullable = False)
    category = Column(String, index = True, nullable = False)
    subcategory = Column(String, index = True, nullable=True)
    description = Column(String, nullable = True)
    price = Column(Float, nullable = False)
    stock = Column(Integer, default = 0)


    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    vehicle = relationship("Vehicle", back_populates="parts")

