from models import db, Booking, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


def seed_bookings():


    booking1 = Booking(
        name='John Doe',
        email_id='john.doe@example.com',
        add_guest='Jane Doe',
        special_notes='Special requests for booking 1',
        created_at=datetime.utcnow()
    )

    booking2 = Booking(
        name='Alice Smith',
        email_id='alice.smith@example.com',
        special_notes='No additional notes for booking 2',
        created_at=datetime.utcnow()
    )

    booking3 = Booking(
        name='Bob Johnson',
        email_id='bob.johnson@example.com',
        add_guest='Eve Johnson',
        special_notes='Special requests for booking 3',
        created_at=datetime.utcnow()
    )
    db.session.add(booking1)
    db.session.add(booking2)
    db.session.add(booking3)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_bookings():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.bookings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM bookings"))

    db.session.commit()
