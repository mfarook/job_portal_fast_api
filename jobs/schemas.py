from typing import List, Optional

from pydantic import BaseModel


class JobBase(BaseModel):
    job_role: str
    salary: int
    job_location: str
    


class JobCreate(JobBase):
    pass


class Jobs(JobBase):
    id: int

    class Config:
        orm_mode = True


class ApplicationBase(BaseModel):
    name: str
    email: str


class ApplicationCreate(ApplicationBase):
    pass


class Jobapply(ApplicationBase):
    id: int
    job_id: int

    class Config:
        orm_mode = True