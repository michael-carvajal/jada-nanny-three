from flask import Blueprint, jsonify, request
from models import ServicePage, db
from forms import ServicePageForm
from datetime import datetime

service_page_routes = Blueprint('/service_page', __name__)

@service_page_routes.route('/')
def get_service_pages():
    """
    Query for all service pages and return them in a list of service page dictionaries
    """
    service_pages = ServicePage.query.all()
    return {'service_pages': [service_page.to_dict() for service_page in service_pages]}

@service_page_routes.route('/<int:service_page_id>', methods=['GET'])
def get_service_page(service_page_id):
    """
    Get a service page by ID
    """
    service_page = ServicePage.query.get(service_page_id)

    if service_page:
        return {'service_page': service_page.to_dict()}
    else:
        return jsonify({'error': 'Service Page not found'}), 404

@service_page_routes.route('/<int:service_page_id>', methods=['PUT'])
def update_service_page(service_page_id):
    """
    Update a service page by ID
    """
    service_page = ServicePage.query.get(service_page_id)

    if service_page:
        data = request.get_json()
        service_page.title = data["title"]
        service_page.description = data["description"]
        db.session.commit()
        return jsonify({'message': 'Service Page updated successfully'}), 200
    else:
        return jsonify({'error': 'Service Page not found'}), 404

@service_page_routes.route('/', methods=['POST'])
def create_service_page():
    """
    Create a new service page
    """
    form = ServicePageForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        service_page = ServicePage(
            title=form.data['title'],
            description=form.data['description'],
            created_at=datetime.utcnow()
        )

        db.session.add(service_page)
        db.session.commit()
        return jsonify({'message': 'Service Page created successfully', 'service_page': service_page.to_dict()}), 201

    return jsonify({'errors': form.errors}), 400

@service_page_routes.route('/<int:service_page_id>', methods=['DELETE'])
def delete_service_page(service_page_id):
    """
    Delete a service page by ID
    """
    service_page = ServicePage.query.get(service_page_id)

    if service_page:
        db.session.delete(service_page)
        db.session.commit()
        return jsonify({'message': 'Service Page deleted successfully'}), 200
    else:
        return jsonify({'error': 'Service Page not found'}), 404
from flask import Blueprint, jsonify, request
from models import ServicePage, db
from forms import ServicePageForm
from datetime import datetime

service_page_routes = Blueprint('/service_page', __name__)

@service_page_routes.route('/')
def get_service_pages():
    """
    Query for all service pages and return them in a list of service page dictionaries
    """
    service_pages = ServicePage.query.all()
    return {'service_pages': [service_page.to_dict() for service_page in service_pages]}

@service_page_routes.route('/<int:service_page_id>', methods=['GET'])
def get_service_page(service_page_id):
    """
    Get a service page by ID
    """
    service_page = ServicePage.query.get(service_page_id)

    if service_page:
        return {'service_page': service_page.to_dict()}
    else:
        return jsonify({'error': 'Service Page not found'}), 404

@service_page_routes.route('/<int:service_page_id>', methods=['PUT'])
def update_service_page(service_page_id):
    """
    Update a service page by ID
    """
    service_page = ServicePage.query.get(service_page_id)

    if service_page:
        data = request.get_json()
        service_page.title = data["title"]
        service_page.description = data["description"]
        db.session.commit()
        return jsonify({'message': 'Service Page updated successfully'}), 200
    else:
        return jsonify({'error': 'Service Page not found'}), 404

@service_page_routes.route('/', methods=['POST'])
def create_service_page():
    """
    Create a new service page
    """
    form = ServicePageForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        service_page = ServicePage(
            title=form.data['title'],
            description=form.data['description'],
            created_at=datetime.utcnow()
        )

        db.session.add(service_page)
        db.session.commit()
        return jsonify({'message': 'Service Page created successfully', 'service_page': service_page.to_dict()}), 201

    return jsonify({'errors': form.errors}), 400

@service_page_routes.route('/<int:service_page_id>', methods=['DELETE'])
def delete_service_page(service_page_id):
    """
    Delete a service page by ID
    """
    service_page = ServicePage.query.get(service_page_id)

    if service_page:
        db.session.delete(service_page)
        db.session.commit()
        return jsonify({'message': 'Service Page deleted successfully'}), 200
    else:
        return jsonify({'error': 'Service Page not found'}), 404
