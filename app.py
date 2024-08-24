from flask import Flask, render_template

__name__ = "__main__"

app = Flask(__name__)

print('Hi')

if __name__ == "__main__":
    app.run(debug = True)