from .db import db, environment, SCHEMA
from datetime import datetime


class AboutPage(db.Model):
    __tablename__ = 'about_pages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    about_page_id = db.Column(db.Integer, primary_key=True)
    first_para = db.Column(db.String(10000), nullable=False)
    second_para = db.Column(db.String(10000), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def to_dict(self):
        return {
            'home_page_id': self.about_page_id,
            'first_para': self.first_para,
            'second_para': self.second_para,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
