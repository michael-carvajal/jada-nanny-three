from .db import db, environment, SCHEMA
from datetime import datetime


class TestimonialPage(db.Model):
    __tablename__ = 'testimonial_pages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    testimonial_page_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    review = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def to_dict(self):
        return {
            'testimonial_page_id': self.testimonial_page_id,
            'name': self.name,
            'review': self.review,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
