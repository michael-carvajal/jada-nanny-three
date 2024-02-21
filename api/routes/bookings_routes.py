from flask import Blueprint, jsonify, request
from models import Booking, db
from forms import BookingForm

bookings_routes = Blueprint('bookings', __name__)


@bookings_routes.route('/')
def bookings():
    """
    Query for all bookings and returns them in a list of bookings dictionaries
    """
    bookings = Booking.query.all()
    return {'bookings': [booking.to_dict() for booking in bookings]}


@bookings_routes.route('/', methods=['POST'])
def create_booking():
    """
    Create a new booking
    """
    form = BookingForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    print(request.get_json())
    if form.validate():
        booking = Booking(
            name=form.name.data,
            email_id=form.email_id.data,
            add_guest=form.add_guest.data,
            special_notes=form.special_notes.data,
        )

        db.session.add(booking)
        db.session.commit()

        return jsonify({'message': 'Booking created successfully', 'booking': booking.to_dict()}), 201

    return jsonify({'errors': form.errors}), 400

@bookings_routes.route('/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    """
    Delete a booking by ID
    """
    booking = Booking.query.get(booking_id)

    if booking:
        db.session.delete(booking)
        db.session.commit()
        return jsonify({'message': 'Booking deleted successfully'}), 200
    else:
        return jsonify({'error': 'Booking not found'}), 404
