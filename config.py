class Config(object):
    DEBUG = True # Turns on debugging features in Flask
    TESTING = False

    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91" # This is a secret key that is used by Flask to sign cookies. It’s also used by extensions like Flask-Bcrypt. You should define this in your instance folder to keep it out of version control. You can read more about instance folders in the next section.
        # To generate the secret key, use the method:
            ## import secrets
            ## secrets.token_hex(16)    # This will give you a 16bit hex code

    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"
    SQLALCHEMY_DATABASE_URI = ""

    IMAGE_UPLOADS = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True # Turns on debugging features in Flask

    SECRET_KEY = "xxx" # This is a secret key that is used by Flask to sign cookies. It’s also used by extensions like Flask-Bcrypt. You should define this in your instance folder to keep it out of version control. You can read more about instance folders in the next section.
        # To generate the secret key, use the method:
            ## import secrets
            ## secrets.token_hex(16)    # This will give you a 16bit hex code

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"
    SQLALCHEMY_DATABASE_URI = ""

    IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False

    BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension

    MAIL_FROM_EMAIL = "alpha@bravo.charlie" # For use in application emails

class TestingConfig(Config):
    TESTING = True

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"
    SQLALCHEMY_DATABASE_URI = ""

    SESSION_COOKIE_SECURE = False

