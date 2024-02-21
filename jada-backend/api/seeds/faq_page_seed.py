from models import db, FAQPage, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


def seed_faq_page():
    faq_page1 = FAQPage(
        question = "Will you use your phone while caring for my child?",
        answer = "Absolutely not! I prioritize your child's care and only use my phone for emergencies. Ensuring your child's safety and engagement is my top priority.",
        created_at=datetime.utcnow()
    )
    faq_page2 = FAQPage(
        question = "How do you handle discipline?",
        answer = "I believe in redirection rather than discipline. My approach is to guide the child gently and align with the methods you prefer as parents. It's about creating a positive and nurturing environment for your child.",
        created_at=datetime.utcnow()
    )
    faq_page3 = FAQPage(
        question = "What is your approach to comforting children?",
        answer = "I follow your lead as parents. Whether it’s immediate comfort or letting your child cry it out, I respect your parenting style and adapt my care to match it. Your child's emotional well-being is important to me.",
        created_at=datetime.utcnow()
    )
    faq_page4 = FAQPage(
        question = "Can I receive updates and photos of my child?",
        answer = "Certainly! I'm happy to provide updates on your child's day. Photos can also be sent upon your specific request, ensuring you're connected and informed.",
        created_at=datetime.utcnow()
    )
    faq_page5 = FAQPage(
        question = "Are you equipped to care for non-verbal children?",
        answer = "Yes, I am. I have experience and training in caring for non-verbal children, including those on the autism spectrum or infants. I'm committed to understanding and meeting their unique needs.",
        created_at=datetime.utcnow()
    )
    faq_page6 = FAQPage(
        question = "What payment methods do you accept?",
        answer = "For your convenience, I accept electronic payments through the website. This process is secure and easy, ensuring hassle-free transactions.",
        created_at=datetime.utcnow()
    )
    faq_page7 = FAQPage(
        question = "What is your cancellation policy?",
        answer = "Life is unpredictable, so I offer flexible cancellation policies. Just give me advance notice if you need to cancel, and I'll do the same for any changes on my end.",
        created_at=datetime.utcnow()
    )
    faq_page8 = FAQPage(
        question = "Do you support all forms of child expression, such as color preferences?",
        answer = "Absolutely! I encourage all forms of expression in children. Whether it's a favorite color or a unique interest, I believe in nurturing their individuality.",
        created_at=datetime.utcnow()
    )
    faq_page9 = FAQPage(
        question = "Do you offer tutoring or homework help?",
        answer = "Yes, I do! Drawing from my academic background and experience, I offer tutoring and homework assistance to support your child's educational journey.",
        created_at=datetime.utcnow()
    )

    faqPages = [faq_page1, faq_page2, faq_page3, faq_page4, faq_page5, faq_page6, faq_page7, faq_page8, faq_page9 ]
    _ = [db.session.add(faqpage) for faqpage in faqPages]
    db.session.commit()



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_faq_page():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.faq_pages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM faq_pages"))

    db.session.commit()
