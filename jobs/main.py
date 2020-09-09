from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Status(BaseModel):
    message: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/jobs/", response_model=schemas.Jobs)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db=db, job=job)


@app.post("/jobs/{job_id}/apply/", response_model=schemas.Jobapply)
def apply_job_for_user(
    job_id: int, item: schemas.ApplicationCreate, db: Session = Depends(get_db)
):
    return crud.apply_job(db=db, item=item, job_id=job_id)




@app.delete("/jobs/{job_id}", response_model=Status)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = crud.delete_job(db, job_id=job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail=f"Job_id {job_id} not found")
    return Status(message=f"Deleted job_id {job_id}")

@app.get("/jobs/{job_id}", response_model=schemas.Jobs)
def read_job(job_id: int, db: Session = Depends(get_db)):
    db_job = crud.get_job(db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job





@app.get("/jobs/", response_model=List[schemas.Jobs])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jobs = crud.get_jobs(db, skip=skip, limit=limit)
    return jobs

@app.get("/appliedjobs/", response_model=List[schemas.Jobapply])
def applied_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    applied_jobs = crud.get_appliedjobs(db, skip=skip, limit=limit)
    return applied_jobs