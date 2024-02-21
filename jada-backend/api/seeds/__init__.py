from flask.cli import AppGroup

from models.db import db, environment, SCHEMA
from .booking_seed import seed_bookings, undo_bookings
from .testimonial_page_seed import seed_testimonials, undo_testimonials
from .home_page_seed import seed_home_page, undo_home_page
from .user_seed import seed_user, undo_user
from .about_page_seed import seed_about_page,undo_about_page
from .contact_page_seed import seed_contact_page,undo_contact_page
from .faq_page_seed import seed_faq_page,undo_faq_page
from .resources_page_seed import seed_resource_page,undo_resource_page
from .services_page_seed import seed_service_page,undo_service_page
# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_testimonials()
        undo_bookings()
        undo_home_page()
        undo_user()
        undo_service_page()
        undo_about_page()
        undo_contact_page()
        undo_faq_page()
        undo_resource_page()
    seed_user()
    seed_home_page()
    seed_bookings()
    seed_testimonials()
    seed_about_page()
    seed_contact_page()
    seed_faq_page()
    seed_resource_page()
    seed_service_page()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_user()
    undo_home_page()
    undo_bookings()
    undo_testimonials()
    undo_resource_page()
    undo_about_page()
    undo_contact_page()
    undo_service_page()
    undo_resource_page()
    undo_faq_page()

    # Add other undo functions here
