from .db import db, environment, SCHEMA
from datetime import datetime


class HomePage(db.Model):
    __tablename__ = 'home_pages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    home_page_id = db.Column(db.Integer, primary_key=True)
    site_title = db.Column(db.String(255), nullable=False)
    site_subtitle = db.Column(db.String(255), nullable=False)
    page_text = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def to_dict(self):
        return {
            'home_page_id': self.home_page_id,
            'site_title': self.site_title,
            'site_subtitle': self.site_subtitle,
            'page_text': self.page_text,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
