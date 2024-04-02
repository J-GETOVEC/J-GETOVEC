from datetime import datetime

from config import db, app


class Human(db.Model):
    """Модель для описания пользователей"""
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(30), index=True, unique=False)
    sec_name: str = db.Column(db.String(50), index=True, unique=False)
    photo: str = db.Column(db.String(1000), index=True, unique=True)
    gender: str = db.Column(db.String(20), index=True, unique=False)
    age: int = db.Column(db.String(3), index=True, unique=False)
    country: str = db.Column(db.String(30), index=True, unique=False)
    bio: str = db.Column(db.String(10000), index=True, unique=False)
    rost: int = db.Column(db.String(3), nullable=True)


class Flat(db.Model):
    """Модель для опсиания квартир"""

    id = db.Column(db.Integer, primary_key=True)
    square: int = db.Column(db.String(5), index=True, unique=False)
    rayon: str = db.Column(db.String(30), index=True, unique=False)
    number_of_rooms: int = db.Column(db.String(2), index=True, unique=False)
    floor: int = db.Column(db.String(5), index=True, unique=False)
    price: str = db.Column(db.String(20), index=True, unique=False)

