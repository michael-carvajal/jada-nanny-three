from models import db, TestimonialPage, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


def seed_testimonials():
    testimonial1 = TestimonialPage(
        name='Jane R.',
        review="Jada has been a blessing for our family. Her patience and skill in handling our son's unique needs have made a significant difference. We're grateful for her dedicated and compassionate approach.",
        created_at=datetime.utcnow()
    )

    testimonial2 = TestimonialPage(
        name="Antonia E.",
        review="Since Jada started her book club, our daughter's love for reading has blossomed. It's incredible to see her so engaged and excited about books. Jada's nurturing presence is truly special",
        created_at=datetime.utcnow()
    )

    testimonial3 = TestimonialPage(
        name='Michael T.',
        review="We were initially anxious about finding the right care for our non-verbal daughter. Jada's expertise and gentle manner have put our worries to rest. She communicates wonderfully with our daughter, and we couldn't be happier.",
        created_at=datetime.utcnow()
    )


    db.session.add(testimonial1)
    db.session.add(testimonial2)
    db.session.add(testimonial3)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_testimonials():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.testimonial_pages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM testimonial_pages"))

    db.session.commit()
