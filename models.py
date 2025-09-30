from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped, relationship
from dataclasses import dataclass
from sqlalchemy import create_engine
from charset_normalizer import models
from faker.providers import phone_number



# base.createtable
class Base(DeclarativeBase):
    pass

# class Personal_Information(Base):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     phone_number: Mapped[str] = mapped_column(String(15))
#     address: Mapped[str] = mapped_column(String(150))
#     work_title: Mapped[str] = mapped_column(String(15))


class Client (Base):
    __tablename__ = "clients"
    name_of_client: Mapped[str] = mapped_column(String(100))
    id: Mapped[int] = mapped_column(primary_key=True)
    phone_number: Mapped[str] = mapped_column(String(15))
    address: Mapped[str] = mapped_column(String(150))
    work_title: Mapped[str] = mapped_column(String(15))


# class Vendor ():  # no overloading/over writing just reusing the init method from line 6
#     # __tablename__ = "vendor"
#     pass







