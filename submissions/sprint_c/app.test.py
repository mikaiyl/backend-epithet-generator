#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import jsonify, Flask
from flask_testing import TestCase
# from configure import app
from helpers import Epithet, Vocabulary

PATH = '../../resources/data.json'


class FlaskTestApp(TestCase):

    @staticmethod
    def create_app(self):
            app = Flask(__name__)
            app.config['TESTING'] = True
            return app




@app.route('/')
def generate_epithet():
    return jsonify(Epithet.create_epithet(PATH))


@app.route('/vocabulary')
def vocabulary():
    return jsonify(Vocabulary.from_file(PATH, fields=False))


@app.route('/epithets/')
@app.route('/epithets/<qty>')
def epithets(qty):
    return jsonify(Epithet.get_epithets(PATH, number=int(qty)))


@app.route('/random')
def random():
    return jsonify(Epithet.get_random(PATH))
