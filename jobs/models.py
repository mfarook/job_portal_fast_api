from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base
from pydantic import BaseModel


class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_role = Column(String)
    salary = Column(Integer)
    job_location = Column(String)



class Jobapply(Base):
    __tablename__ = "jobapply"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))

    