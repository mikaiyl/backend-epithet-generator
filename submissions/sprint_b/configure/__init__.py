#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def configure_app():
    '''
    Configure flask app
    '''
    import os
    import dotenv
    from flask import Flask

    PROJECT_ROOT = os.path.abspath('.')
    # per project instructions
    dotenv.load_dotenv(os.path.join(PROJECT_ROOT, '.env'))
    # This is easier
    # dotenv.load_dotenv(dotenv.find_dotenv())

    # Init app
    app = Flask(__name__)

    return app


# Start app
app = configure_app()
