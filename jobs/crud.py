from sqlalchemy.orm import Session

from . import models, schemas


def get_job(db: Session, job_id: int):
    return db.query(models.Jobs).filter(models.Jobs.id == job_id).first()

def delete_job(db: Session, job_id: int):
    job_delete = db.query(models.Jobs).filter(models.Jobs.id == job_id).delete()
    db.commit()
    return job_delete
    


def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Jobs(job_role=job.job_role, salary=job.salary, job_location=job.job_location)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def apply_job(db: Session, item: schemas.ApplicationCreate, job_id: int):
    db_item = models.Jobapply(**item.dict(), job_id=job_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item




def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Jobs).offset(skip).limit(limit).all()

def get_appliedjobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Jobapply).offset(skip).limit(limit).all()


