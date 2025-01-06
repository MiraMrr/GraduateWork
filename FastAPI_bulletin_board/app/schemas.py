from pydantic import BaseModel

class AdvertisementBase(BaseModel):
    title: str
    description: str
    price: int

class AdvertisementCreate(AdvertisementBase):
    pass

class Advertisement(AdvertisementBase):
    id: int

    class Config:
        orm_mode = True
