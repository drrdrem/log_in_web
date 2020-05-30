import os
import unittest
 
from web import app, db

class UsersTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + \
            os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
        self.assertEquals(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass


def register(self, username, email, password, confirm):
    return self.app.post(
        'register/',
        data=dict(username=username, email=email, password=password, confirm=confirm),
        follow_redirects=True
    )


def login(self, username, password):
    return self.app.post(
        'login/',
        data=dict(username=username, password=password),
        follow_redirects=True
    )


def test_duplicate_email_user_registration(self):
    self.app.get('/register', follow_redirects=True)
    self.register('tt', 'tt@gmail.com', 'testtest', 'testtest')
    self.app.get('/register', follow_redirects=True)
    response = self.register('tt', 'tt@gmail.com', 'testtest', 'testtest')
    self.assertIn(b'ERROR! ', response.data)


def test_update_password_page(self):
    self.app.get('/register', follow_redirects=True)
    self.register('testtest', 'test@gmail.com', 'testtest', 'testtest')
    response = self.app.get('/password_change')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Password Change', response.data)
 
def test_update_password(self):
    self.app.get('/register', follow_redirects=True)
    self.register('testtest', 'test@gmail.com', 'testtest', 'testtest')
    response = self.app.post('/password_change', data=dict(password='newone'), follow_redirects=True)
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Password has been updated!', response.data)
    self.assertIn(b'User Profile', response.data)

 
def test_update_password_log_in(self):
    self.app.get('/register', follow_redirects=True)
    self.register('tt', 'tt@gmail.com', 'testtest', 'testtest')
    self.app.post('/password_change', data=dict(password='newone'), follow_redirects=True)
    response = self.login('tt', 'testtest')
    self.assertIn(b'ERROR! ', response.data)
    