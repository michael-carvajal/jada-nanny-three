from flask import Flask, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import generate_csrf
from models import db
from config import Config
from routes import bookings_routes, user_routes, auth_routes, home_page_routes,about_page_routes,contact_page_routes,faq_page_routes,service_page_routes,testimonial_page_routes,resource_page_routes
from seeds import seed_commands

app = Flask(__name__)
app.cli.add_command(seed_commands)

app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.unauthorized'
# register blue prints here
app.register_blueprint(bookings_routes, url_prefix='/api/bookings')
app.register_blueprint(testimonial_page_routes, url_prefix='/api/testimonial_page')
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(home_page_routes, url_prefix='/api/home_page')
app.register_blueprint(about_page_routes, url_prefix='/api/about_page')
app.register_blueprint(faq_page_routes, url_prefix='/api/faq_page')
app.register_blueprint(contact_page_routes, url_prefix='/api/contact_page')
app.register_blueprint(service_page_routes, url_prefix='/api/service_page')
app.register_blueprint(resource_page_routes, url_prefix='/api/resource_page')


db.init_app(app)
Migrate(app, db)
CORS(app)

@app.route('/api/get_csrf_token', methods=['GET'])
def get_csrf_token():
    csrf_token = generate_csrf()
    response = make_response(jsonify({'csrf_token': csrf_token}))
    response.headers['Set-Cookie'] = f'csrf_token={csrf_token}; Secure; HttpOnly; SameSite=Strict'
    return response

@app.route('/api/hello', methods=['GET'])
def hello_world():
    print('hello inside hello route  ==================>')
    return {"hello" : "Hello, World!"}


if __name__ == '__main__':
    app.run(port=5000)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.unauthorized'

