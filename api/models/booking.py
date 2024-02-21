from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Booking(db.Model):
    __tablename__ = 'bookings'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    booking_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email_id = db.Column(db.String(255), nullable=False)
    add_guest = db.Column(db.String(255))
    special_notes = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def to_dict(self):
        return {
            'booking_id': self.booking_id,
            'name': self.name,
            'email_id': self.email_id,
            'add_guest': self.add_guest,
            'special_notes': self.special_notes,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
