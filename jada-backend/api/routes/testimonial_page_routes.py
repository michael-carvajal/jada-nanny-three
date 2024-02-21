from flask import Blueprint, jsonify, request
from models import TestimonialPage, db
from forms import TestimonialForm
from datetime import datetime

testimonial_page_routes = Blueprint('/testimonial_page', __name__)

@testimonial_page_routes.route('/')
def get_testimonials():
    """
    Query for all testimonials and return them in a list of testimonial dictionaries
    """
    testimonials = TestimonialPage.query.all()
    return {'testimonials': [testimonial.to_dict() for testimonial in testimonials]}

@testimonial_page_routes.route('/<int:testimonial_id>', methods=['GET'])
def get_testimonial(testimonial_id):
    """
    Get a testimonial by ID
    """
    testimonial = TestimonialPage.query.get(testimonial_id)

    if testimonial:
        return {'testimonial': testimonial.to_dict()}
    else:
        return jsonify({'error': 'Testimonial not found'}), 404

@testimonial_page_routes.route('/<int:testimonial_id>', methods=['PUT'])
def update_testimonial(testimonial_id):
    """
    Update a testimonial by ID
    """
    testimonial = TestimonialPage.query.get(testimonial_id)

    if testimonial:
        data = request.get_json()
        testimonial.name = data["name"]
        testimonial.review = data["review"]
        db.session.commit()
        return jsonify({'message': 'Testimonial updated successfully'}), 200
    else:
        return jsonify({'error': 'Testimonial not found'}), 404

@testimonial_page_routes.route('/', methods=['POST'])
def create_testimonial():
    """
    Create a new testimonial
    """
    form = TestimonialForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        testimonial = TestimonialPage(
            name=form.data['name'],
            review=form.data['review'],
            created_at=datetime.utcnow()
        )

        db.session.add(testimonial)
        db.session.commit()
        return jsonify({'message': 'Testimonial created successfully', 'testimonial': testimonial.to_dict()}), 201

    return jsonify({'errors': form.errors}), 400

@testimonial_page_routes.route('/<int:testimonial_id>', methods=['DELETE'])
def delete_testimonial(testimonial_id):
    """
    Delete a testimonial by ID
    """
    testimonial = TestimonialPage.query.get(testimonial_id)

    if testimonial:
        db.session.delete(testimonial)
        db.session.commit()
        return jsonify({'message': 'Testimonial deleted successfully'}), 200
    else:
        return jsonify({'error': 'Testimonial not found'}), 404
