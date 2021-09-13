
import pytest
import flask 
from flask_testing import TestCase
from applications import app, db
from applications.models import *
from applications.routes import *

class TestBase(TestCase) :
    def create_app(self):

        # Pass in testing configurations for the app.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///Patientdata.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                # WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
         

        # Create table schema
        db.create_all()

        # Create test dog
        test_patient = Patients(first_name="Chewbarka",last_name = "dog", dob = "29/11/1997")

       # save sample data to database
        db.session.add(test_patient)
        db.session.commit()
  
  
    def tearDown(self):
        db.session.remove()
        db.drop_all()
class TestViews(TestBase):

    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)

    def test_cancel(self):
        response = self.client.get(url_for('cancel'))
        self.assertEqual(response.status_code,200)
    
    def test_create(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code,200)
    
    def test_update(self):
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code,200)

    def test_view(self):
        response = self.client.get(url_for('view'))
        self.assertEqual(response.status_code,200)
    
    def test_views(self):
        response = self.client.get(url_for('views'))
        self.assertEqual(response.status_code,200)

    def test_home_get(self):


         response = self.client.get(url_for('home')) # send a GET request
         self.assertEqual(response.status_code, 200) # assert that the response code is 200
         self.assertIn(b"welcome to charanjit's practice", response.data)

    def test_update_get(self):


         response = self.client.get(url_for('cancel')) # send a GET request
         self.assertEqual(response.status_code, 200) # assert that the response code is 200
         self.assertIn(b"Cancel appointment", response.data)

class TestDelq(TestBase):
    def test_delete(self):
        response = self.client.get(url_for('cancel', patient_id = 1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'delete', response.data)
class TestUpdate(TestBase):
    def test_update(self):
        response = self.client.post(url_for('update', patient_id = 1), 
        data = dict(date = '29/11/2021',msg = "updated successfully"),
        follow_redirects=True
        )
        self.assertIn(b'update',response.data)
class TestViews(TestBase):

     def test_views(self):




