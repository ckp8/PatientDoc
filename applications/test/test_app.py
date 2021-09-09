from flask_testing import TestCase
from applications import app, db
from applications.models import Questions, Options


class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///Patientdata.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
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
        db.sessin.remove()
        db.drop_all()
class TestViews(TestBase):

    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)

    def test_cancel(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code,200)

    
    





