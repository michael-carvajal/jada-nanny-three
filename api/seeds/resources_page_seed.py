from models import db, ResourcePage, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


def seed_resource_page():
    resource_page1 = ResourcePage(
        title="Autism Speaks",
        url="https://www.autismspeaks.org",
        description="An organization dedicated to promoting solutions for individuals with autism and their families through advocacy and support.",
        created_at=datetime.utcnow()
    )
    resource_page2 = ResourcePage(
        title="Child Mind Institute",
        url="https://childmind.org",
        description="An independent, national nonprofit dedicated to transforming the lives of children and families struggling with mental health and learning disorders.",
        created_at=datetime.utcnow()
    )
    resource_page3 = ResourcePage(
        title="Understood",
        url="https://www.understood.org",
        description="Resources for people with learning and attention issues that empower them to understand their challenges and thrive.",
        created_at=datetime.utcnow()
    )
    resource_page4 = ResourcePage(
        title="CDC's Parent Information",
        url="https://www.cdc.gov/parents",
        description="The Centers for Disease Control and Prevention provides parents with credible, reliable health information.",
        created_at=datetime.utcnow()
    )
    resource_page5 = ResourcePage(
        title="Parenting Special Needs Magazine",
        url="https://parentingspecialneeds.org",
        description="An online magazine that provides practical tips, shares life’s lessons, tackles the challenges and celebrates the joys of parenting children with special needs.",
        created_at=datetime.utcnow()
    )

    resource_pages = [resource_page1, resource_page2, resource_page3, resource_page4, resource_page5]
    _ = [db.session.add(resource_page) for resource_page in resource_pages]
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_resource_page():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.resource_pages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM resource_pages"))

    db.session.commit()
