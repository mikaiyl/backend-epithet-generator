#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import jsonify
from configure import app
from helpers import Epithet, Vocabulary

PATH = '../../resources/data.json'


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
