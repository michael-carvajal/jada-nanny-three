from flask import Blueprint, jsonify, request
from models import FAQPage, db
from forms import FAQPageForm

faq_page_routes = Blueprint('/faq_page', __name__)

@faq_page_routes.route('/')
def get_faq_pages():
    """
    Query for all FAQ pages and return them in a list of FAQ page dictionaries
    """
    faq_pages = FAQPage.query.all()
    return {'faq_pages': [faq_page.to_dict() for faq_page in faq_pages]}

@faq_page_routes.route('/<int:faq_page_id>', methods=['GET'])
def get_faq_page(faq_page_id):
    """
    Get an FAQ page by ID
    """
    faq_page = FAQPage.query.get(faq_page_id)

    if faq_page:
        return {'faq_page': faq_page.to_dict()}
    else:
        return jsonify({'error': 'FAQ Page not found'}), 404

@faq_page_routes.route('/<int:faq_page_id>', methods=['PUT'])
def update_faq_page(faq_page_id):
    """
    Update an FAQ page by ID
    """
    faq_page = FAQPage.query.get(faq_page_id)

    if faq_page:
        data = request.get_json()
        faq_page.question = data["question"]
        faq_page.answer = data["answer"]
        db.session.commit()
        return jsonify({'message': 'FAQ Page updated successfully'}), 200
    else:
        return jsonify({'error': 'FAQ Page not found'}), 404

@faq_page_routes.route('/', methods=['POST'])
def create_faq_page():
    """
    Create a new FAQ page
    """
    form = FAQPageForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        faq_page = FAQPage(
            question=form.data['question'],
            answer=form.data['answer']
        )

        db.session.add(faq_page)
        db.session.commit()
        return jsonify({'message': 'FAQ Page created successfully', 'faq_page': faq_page.to_dict()}), 201

    return jsonify({'errors': form.errors}), 400

@faq_page_routes.route('/<int:faq_page_id>', methods=['DELETE'])
def delete_faq_page(faq_page_id):
    """
    Delete an FAQ page by ID
    """
    faq_page = FAQPage.query.get(faq_page_id)

    if faq_page:
        db.session.delete(faq_page)
        db.session.commit()
        return jsonify({'message': 'FAQ Page deleted successfully'}), 200
    else:
        return jsonify({'error': 'FAQ Page not found'}), 404
