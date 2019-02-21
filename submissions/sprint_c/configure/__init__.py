#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import dotenv
from flask import Flask

# Set project root
PROJECT_ROOT = os.getcwd()

# Get ENV and assign FLASK_ENV to var
dotenv.load_dotenv(os.path.join(PROJECT_ROOT, '.env'))
FLASK_ENV = os.getenv('FLASK_ENV')


def configure_app():
    '''
    Configure flask app
    '''
    # per project instructions
    # This is easier
    # dotenv.load_dotenv(dotenv.find_dotenv())

    # Init app
    if FLASK_ENV == 'testing':
        app = Flask(__name__)
        app.config['TESTING'] = True
    else:
        app = Flask(__name__)

    return app


# Start app
app = configure_app()
