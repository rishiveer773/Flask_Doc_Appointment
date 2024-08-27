from flask import Flask, render_template, url_for

__name__ = "__main__"

app = Flask(__name__)

#--------------ADDING ROUTES---------------------------
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/userlogin/<username>')
def userlogin(username):
    return render_template('userlogin.html', username=username)

@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')

if __name__ == "__main__":
    app.run(debug = True)