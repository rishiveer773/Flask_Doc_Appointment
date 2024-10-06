from flask import Flask, render_template, request, url_for, get_flashed_messages, session, flash

__name__ = "__main__"
app = Flask(__name__)

app.secret_key = "test_push"

#--------------ADDING ROUTES---------------------------
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/patientlogin', methods = ['POST', 'GET'])
def patientlogin():
    error = None
    return render_template('patientlogin.html', error = error)

@app.route('/adminlogin', methods = ['POST', 'GET'])
def adminlogin():
    return render_template('adminlogin.html')


#---------------ERROR HANDLERS-------------------------
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


#---------------RUN THE CODE---------------------------
if __name__ == "__main__":
    app.run(debug = True)