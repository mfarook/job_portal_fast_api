from sqlalchemy.orm import Session

from . import models, schemas


def get_job(db: Session, job_id: int):
    return db.query(models.Jobs).filter(models.Jobs.id == job_id).first()

def delete_job(db: Session, job_id: int):
    job_delete = db.query(models.Jobs).filter(models.Jobs.id == job_id).delete()
    db.commit()
    return job_delete
    
def signup_canditate(db: Session, canditate: schemas.CanditateCreate):
    db_candiate = models.Canditate(name=canditate.name, email=canditate.email)
    db.add(db_candiate)
    db.commit()
    db.refresh(db_candiate)
    return db_candiate


def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Jobs(job_role=job.job_role, salary=job.salary, job_location=job.job_location)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def apply_job(db: Session, item: schemas.ApplicationCreate):
    db_item = models.Jobapply(**item.dict())
    canditate_check = db.query(models.Canditate).filter(models.Canditate.id == db_item.canditate_id).first()
    if canditate_check:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return None


def get_canditates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Canditate).offset(skip).limit(limit).all()

def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Jobs).offset(skip).limit(limit).all()

def get_appliedjobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Jobapply).offset(skip).limit(limit).all()


