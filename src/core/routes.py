from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return 'Hello, World!'

@routes.route('/test')
def test():
    return 'Test endpoint'