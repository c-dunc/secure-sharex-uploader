import config

from flask import Flask
from core.routes import routes

def main():
    try:
        app = Flask(__name__)
        app.register_blueprint(routes)
        app.run(host='0.0.0.0', port=config.webserver_port, debug=False)
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
