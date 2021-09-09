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

    