import datetime

from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from typing_extensions import Annotated
from typing import List

engine = create_engine("mysql+pymysql://root:abcd=1234@localhost:3306/itcast")

Base = declarative_base()

int_pk = Annotated[int, mapped_column(primary_key=True)]
required_unique_name = Annotated[str, mapped_column(String(128), unique=True, nullable=False)]
timestamp_not_null = Annotated[datetime.datetime, mapped_column(nullable=False)]


class Department(Base):
    __tablename__ = "department"

    id: Mapped[int_pk]
    name: Mapped[required_unique_name]
    employees: Mapped[List["Employee"]] = relationship(back_populates="department")
    def __repr__(self):
        return f'id:{self.id},name:{self.name}'


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int_pk]
    dep_id: Mapped[int] = mapped_column(ForeignKey("department.id"))
    name: Mapped[required_unique_name]
    birthday: Mapped[timestamp_not_null]

    department: Mapped[Department] = relationship(lazy=False, back_populates="employees")  # 这里定义了一个关系

    def __repr__(self):
        return f'id:{self.id},dep_id:{self.dep_id},name:{self.name},birthday:{self.birthday}'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
