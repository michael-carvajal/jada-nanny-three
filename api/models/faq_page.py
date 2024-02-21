from .db import db, environment, SCHEMA
from datetime import datetime


class FAQPage(db.Model):
    __tablename__ = 'faq_pages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    faq_page_id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def to_dict(self):
        return {
            'faq_page_id': self.faq_page_id,
            'question': self.question,
            'answer': self.answer,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
