from models import db, AboutPage, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


def seed_about_page():
    about_page1 = AboutPage(
        first_para = "Growing up as an only child with a busy single mom, I understood loneliness and made it my mission to prevent it in as many children as possible. Since receiving my certifications in 2019, I have been dedicated to providing love, guidance, and fun learning experiences to every child and family I work with.",
        second_para = "I'm not just a nanny; I'm a mentor, a tutor, and a friend. My journey has led me to earn a Registered Behavior Technician certification, allowing me to offer specialized care for children with different needs. My motto is simple: 'You're There for Them, and I'm Here For You.'",
        created_at=datetime.utcnow()
    )



    db.session.add(about_page1)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_about_page():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.about_pages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM about_pages"))

    db.session.commit()
