from sqlalchemy import Column, Integer, String

from config.database import Base, engine


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)


Base.metadata.create_all(engine)
