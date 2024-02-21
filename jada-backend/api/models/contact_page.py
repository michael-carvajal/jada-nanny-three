from .db import db, environment, SCHEMA
from datetime import datetime


class ContactPage(db.Model):
    __tablename__ = 'contact_pages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    contact_page_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def to_dict(self):
        return {
            'contact_page_id': self.contact_page_id,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
