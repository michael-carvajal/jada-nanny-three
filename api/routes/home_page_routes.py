from flask import Blueprint, jsonify, request
from models import HomePage, db
from forms import HomePageForm

home_page_routes = Blueprint('/home_page', __name__)


@home_page_routes.route('/')
def home_page():
    """
    Query for all home_page and returns them in a list of home_page dictionaries
    """
    home_pages = HomePage.query.all()
    return {'home_page': [home_page.to_dict() for home_page in home_pages]}


@home_page_routes.route('/<int:home_page_id>', methods=['PUT'])
def update_home_page(home_page_id):
    """
    Update a home_page by ID
    """
    home_page = HomePage.query.get(home_page_id)

    if home_page:
        data = request.get_json()
        home_page.site_title = data["site_title"]
        home_page.site_subtitle = data["site_subtitle"]
        home_page.page_text = data["page_text"]
        db.session.commit()
        return jsonify({'message': 'Home Page updated successfully'}), 200
    else:
        return jsonify({'error': 'Home Page not found'}), 404
    

@home_page_routes.route('/', methods=['POST'])
def create_home_page():
    """
    Create a new home page
    """
    form = HomePageForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    print(request.get_json())
    if form.validate_on_submit():
        home_page = HomePage(
            site_title=form.data['site_title'],
            site_subtitle=form.data['site_subtitle'],
            page_text=form.data['page_text'],
            
        )

        db.session.add(home_page)
        db.session.commit()
        print(home_page)
        return jsonify({'message': 'Home Page created successfully', 'home_page': home_page.to_dict()}), 201

    return jsonify({'errors': form.errors}), 400
