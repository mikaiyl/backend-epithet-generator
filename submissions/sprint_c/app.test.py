#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get
from flask_testing import TestCase# , LiveServerTestCase
from configure import app

PATH = '../../resources/data.json'


class TestFlaskApp(TestCase):

    def create_app(self):
        app.config['LIVESERVER_PORT'] = 0
        return app

    def test_server_running(self):
        res = get(self.get_server_url())
        self.assertEquals(res.code, 200)

    def test_generate_epithiet(self):
        res = self.client.get('/')
        self.assertEqual(res.code, 200)
        self.assertTrue(len(res.data) > 0)
        self.assertTrue(len(res.data.split()) >= 2)

    def vocabulary(self):
        res = self.client.get('/vocabulary')
        self.assertEquals(res.code, 200)
        self.assertTrue((res.data, dict))
        self.assertTrue((res.data['Column 1'], list))
        self.assertTrue((res.data['Column 2'], list))
        self.assertTrue((res.data['Column 3'], list))

    def epithets(self):
        res = self.client.get('/epithets/20')
        self.assertEquals(res.code, 200)
        self.assertTrue(isinstance(res.data, list))
        self.assertTrue(len(res.data) == 20)

    def random(self):
        res = self.client.get('/random')
        self.assertEquals(res.code, 200)
        self.assertTrue(isinstance(res.data, list))
        self.assertTrue(len(res.data) > 0)
        self.assertTrue(len(res.data) < 100)
