from flask import Flask, render_template
from .models import DB 


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHMEY_DATABASE_URI'] = 'sqlite://///Users/Medy/Desktop/Twitoff/twitoff/db.sqlite3.'
    DB.init_app(app)
    
    @app.route('/')
    def root():
        return render_template('base.html', title = 'the space Jam!')
    return app

 

# if __name__ == "__main__":
#     app.run(debug=True, port = 8080)