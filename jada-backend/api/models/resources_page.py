from .db import db, environment, SCHEMA
from datetime import datetime


class ResourcePage(db.Model):
    __tablename__ = 'resource_pages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    resource_page_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def to_dict(self):
        return {
            'resource_page_id': self.resource_page_id,
            'title': self.title,
            'url': self.url,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
