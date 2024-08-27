from flask import Flask, render_template

__name__ = "__main__"

app = Flask(__name__)

#--------------ADDING ROUTES---------------------------
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/userlogin')
def userlogin():
    return render_template('userlogin.html')

@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')

if __name__ == "__main__":
    app.run(debug = True)