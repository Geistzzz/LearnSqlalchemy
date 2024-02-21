from sqlalchemy import create_engine,Column,String,Integer,Date
from sqlalchemy.orm import declarative_base,sessionmaker


engine = create_engine("mysql+pymysql://root:abcd=1234@localhost:3306/itcast")

Base = declarative_base()

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer,primary_key=True)
    name = Column(String(128),unique=True,nullable=False)
    birthday = Column(Date,nullable=False)
    address = Column(String(255),nullable=True)



Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)