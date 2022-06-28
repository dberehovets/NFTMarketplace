from sqlalchemy import Column, Integer, Date, SmallInteger

from services.database import db


class DBPatch(db.Model):
    __tablename__ = 'db_patch'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    version = Column(SmallInteger, nullable=False)
