import sys
import config

from flask import Flask
from core.routes import routes
from core.monitoring import check_vulnerable

def start_webapp():
    try:
        app = Flask(__name__)
        app.register_blueprint(routes)
        app.run(host='0.0.0.0', port=config.webserver_port, debug=False)
    except Exception as e:
        print(f'An error occurred: {e}')

def main():
    if check_vulnerable() == True:
        sys.exit(1)
    else: 
        start_webapp()
        
if __name__ == '__main__':
    main()
