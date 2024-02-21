from flask import Blueprint, jsonify, request
from models import AboutPage, db
from forms import AboutPageForm

about_page_routes = Blueprint('/about_page', __name__)

@about_page_routes.route('/')
def get_about_pages():
    """
    Query for all about pages and return them in a list of about page dictionaries
    """
    about_pages = AboutPage.query.all()
    return {'about_pages': [about_page.to_dict() for about_page in about_pages]}


@about_page_routes.route('/<int:about_page_id>', methods=['PUT'])
def update_about_page(about_page_id):
    """
    Update an about page by ID
    """
    about_page = AboutPage.query.get(about_page_id)

    if about_page:
        data = request.get_json()
        about_page.first_para = data["first_para"]
        about_page.second_para = data["second_para"]
        db.session.commit()
        return jsonify({'message': 'About Page updated successfully'}), 200
    else:
        return jsonify({'error': 'About Page not found'}), 404

@about_page_routes.route('/', methods=['POST'])
def create_about_page():
    """
    Create a new about page
    """
    form = AboutPageForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        about_page = AboutPage(
            first_para=form.data['first_para'],
            second_para=form.data['second_para']
        )

        db.session.add(about_page)
        db.session.commit()
        return jsonify({'message': 'About Page created successfully', 'about_page': about_page.to_dict()}), 201

    return jsonify({'errors': form.errors}), 400

@about_page_routes.route('/<int:about_page_id>', methods=['DELETE'])
def delete_about_page(about_page_id):
    """
    Delete an about page by ID
    """
    about_page = AboutPage.query.get(about_page_id)

    if about_page:
        db.session.delete(about_page)
        db.session.commit()
        return jsonify({'message': 'About Page deleted successfully'}), 200
    else:
        return jsonify({'error': 'About Page not found'}), 404
