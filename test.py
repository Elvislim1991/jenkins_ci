#!/usr/bin/env python3
import unittest
import app

class TestHello(unittest.TestCase):
    
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_name_full_data(self):
        name = 'Elvis'
        rv = self.app.get(f'/hello/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, bytes(f'Why Hello {name}!\n', 'utf-8'))

    def test_new_feature(self):
        rv = self.app.get('/new_feature/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'new feature!\n')

    def test_new_page(self):
        rv = self.app.get('/new_page/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'new page!\n')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
