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
    job_id: int
    canditate_id: int


class ApplicationCreate(ApplicationBase):
    pass


class Jobapply(ApplicationBase):
    id: int
    
    

    class Config:
        orm_mode = True


class CanditateBase(BaseModel):
    name: str
    email: str
    


class CanditateCreate(CanditateBase):
    pass


class Candidate(CanditateBase):
    id: int

    class Config:
        orm_mode = True