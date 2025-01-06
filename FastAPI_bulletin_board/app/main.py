from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, get_db

app = FastAPI()

# Создание таблиц
Base.metadata.create_all(bind=engine)

@app.post("/advertisements/", response_model=schemas.Advertisement)
def create_advertisement(ad: schemas.AdvertisementCreate, db: Session = Depends(get_db)):
    return crud.create_advertisement(db=db, ad=ad)

@app.get("/advertisements/", response_model=list[schemas.Advertisement])
def read_advertisements(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_advertisements(db=db, skip=skip, limit=limit)

@app.get("/advertisements/{ad_id}", response_model=schemas.Advertisement)
def read_advertisement(ad_id: int, db: Session = Depends(get_db)):
    db_ad = crud.get_advertisement(db=db, ad_id=ad_id)
    if db_ad is None:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return db_ad

@app.delete("/advertisements/{ad_id}", response_model=schemas.Advertisement)
def delete_advertisement(ad_id: int, db: Session = Depends(get_db)):
    db_ad = crud.delete_advertisement(db=db, ad_id=ad_id)
    if db_ad is None:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return db_ad
