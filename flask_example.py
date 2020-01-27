from flask import Flask

app = Flask(__name__)

@app.route('/mehdi')

def home():
    # deployed model geos here
    return '<h1> Hello, World!</h1>'


if __name__ == "__main__":
    app.run(debug=True, port = 8080)


    