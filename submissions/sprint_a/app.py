#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import jsonify
from configure import app


@app.route('/')
def generate_epithets():
    return jsonify(epithets={})


@app.route('/vocabulary')
def vocabulary():
    return jsonify(vocabulary={})
