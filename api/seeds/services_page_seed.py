from models import db, ServicePage, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


def seed_service_page():
    service_page1 = ServicePage(
        title= "Specialized Behavior Support",
        description= "As a Registered Behavior Technician, I provide specialized support for children with autism and other behavioral needs. My approach is tailored to each child, focusing on positive reinforcement and skill development.",
        created_at=datetime.utcnow()
    )
    service_page2 = ServicePage(
        title= "Customized Book Clubs",
        description= "Fostering a love for reading, I organize book clubs for children who can read independently. This encourages literacy, imagination, and social interaction in a fun, engaging environment.",
        created_at=datetime.utcnow()
    )
    service_page3 = ServicePage(
        title= "Multilingual and Cultural Exposure",
        description= "Understanding the importance of cultural diversity, I offer exposure to different languages and cultures. This includes books in Spanish, songs in Mandarin, or using ASL, catering to your family's preferences and heritage.",
        created_at=datetime.utcnow()
    )
    service_page4 = ServicePage(
        title= "Tailored Redirection Methods",
        description= "FDiscipline is not part of my approach. Instead, I focus on gentle redirection, aligning with your family's values and parenting style to ensure a consistent and nurturing environment for your child.",
        created_at=datetime.utcnow()
    )
    service_page5 = ServicePage(
        title= "Allergy and Sensitivity Accommodations",
        description= "Your child's health is paramount. I take all necessary precautions to accommodate any allergies or sensitivities, including dietary restrictions, pet allergies, or sensitivities to scents.",
        created_at=datetime.utcnow()
    )
    service_page6 = ServicePage(
        title= "Household Respect and Safety",
        description= "I respect your household rules, including off-limits areas for children and adherence to any specific parental guidelines regarding child activities and behavior.",
        created_at=datetime.utcnow()
    )
    service_page7 = ServicePage(
        title= "Tutoring and Academic Support",
        description= "Leveraging my early college experience, I provide tutoring and homework assistance. My aim is to support your child's academic growth with personalized attention and educational encouragement.",
        created_at=datetime.utcnow()
    )
    service_page8 = ServicePage(
        title= "Emergency Response Preparedness",
        description= "Certified in CPR and childcare, I am prepared to respond effectively to any emergency, ensuring your child's safety and well-being at all times.",
        created_at=datetime.utcnow()
    )
    service_page9 = ServicePage(
        title= "Flexible and Electronic Payment Options",
        description= "For your convenience, I accept various electronic payment methods through the website. This secure and straightforward process ensures hassle-free transactions.",
        created_at=datetime.utcnow()
    )
    service_page10 = ServicePage(
        title= "Introductory Meetings and Custom Service Plans",
        description= "I believe in starting our journey with a comprehensive introductory meeting. This allows me to understand your family's unique needs and tailor my services accordingly, ensuring the best care for your child.",
        created_at=datetime.utcnow()
    )


    resource_pages = [service_page1, service_page2, service_page3, service_page4, service_page5,service_page6,service_page7,service_page8,service_page9,service_page10]
    _ = [db.session.add(resource_page) for resource_page in resource_pages]
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_service_page():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.service_pages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM service_pages"))

    db.session.commit()
