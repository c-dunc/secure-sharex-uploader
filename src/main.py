import sys
import config

from flask import Flask
from core import routes
from core import monitoring

def main():
    if monitoring.check_vulnerable() == True:
        sys.exit(1)
    else: 
        routes.start_webapp()
        
if __name__ == '__main__':
    main()
