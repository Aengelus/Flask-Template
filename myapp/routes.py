from flask import render_template
from myapp import app
from flask.helpers import make_response



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        return do_the_login()
#    else:
#        return show_the_login_form()

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html'), 404)
    #resp.headers['X-Something'] = 'A value'
    return resp