from flask import Flask, render_template, request, url_for, get_flashed_messages, session

__name__ = "__main__"
app = Flask(__name__)

app.secret_key = "test_push"

#--------------ADDING ROUTES---------------------------
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/userlogin', methods = ['POST', 'GET'])
def userlogin():
    error = None
    if request.method == "POST":
        if valid_login
    return render_template('userlogin.html', error = error)

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