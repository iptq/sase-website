import os
import sys
import logging


class Config(object):
    """ Configuration for the Flask object based on environment variables. """

    def __init__(self):
        # ENVIRONMENT = { development | testing | production }
        self.ENVIRONMENT = os.getenv("ENVIRONMENT", "production")  # secure by defualt
        if self.ENVIRONMENT.lower() == "development":
            self.DEBUG = True
            self.TEMPLATES_AUTO_RELOAD = True

        self.port = int(os.getenv("PORT", "7400"))

        # Secret Key
        self.SECRET_KEY = Config.get_secret_key()

        # Database URL
        self.SQLALCHEMY_DATABASE_URI = Config.get_database_url()
        self.SQLALCHEMY_TRACK_MODIFICATIONS = True

        # Flask-Admin
        self.SECURITY_URL_PREFIX = os.getenv("SECURITY_URL_PREFIX", "/admin")

    @staticmethod
    def get_database_url():
        url = os.getenv("DATABASE_URL")

        if not url:
            sys.stderr.write(
                "DATABASE_URL not specified, application is exiting..\n")
            sys.stderr.flush()
            sys.exit(1)
        return url

    @staticmethod
    def get_secret_key():
        key = os.getenv("SECRET_KEY")
        if key:
            return key
        sys.stderr.write(
            "SECRET_KEY not specified, application is exiting..\n")
        sys.stderr.flush()
        sys.exit(1)

    @staticmethod
    def get_email_credentials():
        gmail_username = os.getenv("GMAIL_USERNAME")
        gmail_password = os.getenv("GMAIL_PASSWORD")
        if not (gmail_username and gmail_password):
            return False
        return (gmail_username, gmail_password)
