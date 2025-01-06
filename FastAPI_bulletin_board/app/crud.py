from sqlalchemy.orm import Session
from . import models, schemas

def get_advertisements(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Advertisement).offset(skip).limit(limit).all()

def get_advertisement(db: Session, ad_id: int):
    return db.query(models.Advertisement).filter(models.Advertisement.id == ad_id).first()

def create_advertisement(db: Session, ad: schemas.AdvertisementCreate):
    db_ad = models.Advertisement(**ad.dict())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad

def delete_advertisement(db: Session, ad_id: int):
    db_ad = db.query(models.Advertisement).filter(models.Advertisement.id == ad_id).first()
    if db_ad:
        db.delete(db_ad)
        db.commit()
    return db_ad
