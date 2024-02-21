from models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


def seed_user():
    home_page1 = User(
        email = "admin@email.com",
        password = "password",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )



    db.session.add(home_page1)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_user():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
