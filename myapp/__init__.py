from flask import Flask
# Comvert Sass to css
from sassutils.wsgi import SassMiddleware
#from flask_sqlalchemy import SQLAlchemy

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db = SQLAlchemy(app)


app = Flask(__name__, instance_relative_config=True)
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")
# We can access the configuration variables via app.config["VAR_NAME"].v

#app.wsgi_app = SassMiddleware(app.wsgi_app, {
#    'app': ('static/sass', 'static/css', '/static/css')
#})

from myapp import routes

#setup (
#    # ...,
#    setup_requires=['libsass >= 0.6.0'],
#    sass_manifests={
#        'myapp': ('static/sass', 'static/css', '/static/css')
#    }
#)