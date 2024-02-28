from sqlalchemy import MetaData, Column, Integer, String, UUID
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declarative_base
metadata = MetaData()


Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks_table'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, unique=True)
    uuid: Mapped[str] = mapped_column(unique=True, nullable=False)
    task: Mapped[str] = mapped_column(nullable=False)
    param_1: Mapped[str] = mapped_column(nullable=True)
    param_2: Mapped[int] = mapped_column(nullable=True)
