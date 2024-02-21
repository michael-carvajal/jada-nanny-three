from flask import Blueprint, jsonify, request
from models import ResourcePage, db
from forms import ResourcePageForm
from datetime import datetime

resource_page_routes = Blueprint('/resource_page', __name__)

@resource_page_routes.route('/')
def get_resource_pages():
    """
    Query for all resource pages and return them in a list of resource page dictionaries
    """
    resource_pages = ResourcePage.query.all()
    return {'resource_pages': [resource_page.to_dict() for resource_page in resource_pages]}

@resource_page_routes.route('/<int:resource_page_id>', methods=['GET'])
def get_resource_page(resource_page_id):
    """
    Get a resource page by ID
    """
    resource_page = ResourcePage.query.get(resource_page_id)

    if resource_page:
        return {'resource_page': resource_page.to_dict()}
    else:
        return jsonify({'error': 'Resource Page not found'}), 404

@resource_page_routes.route('/<int:resource_page_id>', methods=['PUT'])
def update_resource_page(resource_page_id):
    """
    Update a resource page by ID
    """
    resource_page = ResourcePage.query.get(resource_page_id)

    if resource_page:
        data = request.get_json()
        resource_page.title = data["title"]
        resource_page.url = data["url"]
        resource_page.description = data["description"]
        db.session.commit()
        return jsonify({'message': 'Resource Page updated successfully'}), 200
    else:
        return jsonify({'error': 'Resource Page not found'}), 404

@resource_page_routes.route('/', methods=['POST'])
def create_resource_page():
    """
    Create a new resource page
    """
    form = ResourcePageForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        resource_page = ResourcePage(
            title=form.data['title'],
            url=form.data['url'],
            description=form.data['description'],
            created_at=datetime.utcnow()
        )

        db.session.add(resource_page)
        db.session.commit()
        return jsonify({'message': 'Resource Page created successfully', 'resource_page': resource_page.to_dict()}), 201

    return jsonify({'errors': form.errors}), 400

@resource_page_routes.route('/<int:resource_page_id>', methods=['DELETE'])
def delete_resource_page(resource_page_id):
    """
    Delete a resource page by ID
    """
    resource_page = ResourcePage.query.get(resource_page_id)

    if resource_page:
        db.session.delete(resource_page)
        db.session.commit()
        return jsonify({'message': 'Resource Page deleted successfully'}), 200
    else:
        return jsonify({'error': 'Resource Page not found'}), 404
