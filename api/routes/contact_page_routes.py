from flask import Blueprint, jsonify, request
from models import ContactPage, db
from forms import ContactPageForm

contact_page_routes = Blueprint('/contact_page', __name__)

@contact_page_routes.route('/')
def get_contact_pages():
    """
    Query for all contact pages and return them in a list of contact page dictionaries
    """
    contact_pages = ContactPage.query.all()
    return {'contact_pages': [contact_page.to_dict() for contact_page in contact_pages]}


@contact_page_routes.route('/<int:contact_page_id>', methods=['PUT'])
def update_contact_page(contact_page_id):
    """
    Update a contact page by ID
    """
    contact_page = ContactPage.query.get(contact_page_id)

    if contact_page:
        data = request.get_json()
        contact_page.email = data["email"]
        db.session.commit()
        return jsonify({'message': 'Contact Page updated successfully'}), 200
    else:
        return jsonify({'error': 'Contact Page not found'}), 404

@contact_page_routes.route('/', methods=['POST'])
def create_contact_page():
    """
    Create a new contact page
    """
    form = ContactPageForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        contact_page = ContactPage(
            email=form.data['email']
        )

        db.session.add(contact_page)
        db.session.commit()
        return jsonify({'message': 'Contact Page created successfully', 'contact_page': contact_page.to_dict()}), 201
    
@contact_page_routes.route('/<int:contact_page_id>', methods=['DELETE'])
def delete_contact_page(contact_page_id):
    """
    Delete a contact page by ID
    """
    contact_page = ContactPage.query.get(contact_page_id)

    if contact_page:
        db.session.delete(contact_page)
        db.session.commit()
        return jsonify({'message': 'Contact Page deleted successfully'}), 200
    else:
        return jsonify({'error': 'Contact Page not found'}), 404
    

  
