from .db import db, environment, SCHEMA
from datetime import datetime


class ServicePage(db.Model):
    __tablename__ = 'service_pages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    service_page_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def to_dict(self):
        return {
            'service_page_id': self.service_page_id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
