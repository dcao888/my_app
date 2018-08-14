from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# 1. create declarative base 
engine = create_engine('postgresql+psycopg2://usr:pass@postgres/db')
Base   = declarative_base()

# 2. assign table to Base 
class Record(Base):
    # strores all records from our toy website 
    __tablename__ = 'records'

    id          = Column(Integer, primary_key = True)
    user        = Column(String)
    record      = Column(String)
    upload_dttm = Column(DateTime(timezone = True))

    def __init__(self, user, record, upload_dttm):
        self.user        = user
        self.record      = record
        self.upload_dttm = upload_dttm

    def __repr__(self):
        return "<user: {}, record: {}>".format(self.user, self.record)

# 3. create tables in Base 
Base.metadata.create_all(bind = engine)


