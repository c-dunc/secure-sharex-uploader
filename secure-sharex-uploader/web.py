import json

from core import config

def main():
    test = config.load_config()
    print(test)

if __name__ == '__main__':
    main()
