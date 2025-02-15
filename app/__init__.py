#This facilitates imports from the app directory

import os
from dotenv import load_dotenv

from flask import Flask

from web_app.routes.home_routes import home_routes
#from web_app.routes.book_routes import book_routes
#from web_app.routes.weather_routes import weather_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    #app.register_blueprint(book_routes)
    #app.register_blueprint(weather_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

load_dotenv()

APP_ENV = os.getenv("APP_ENV", default="development") # use "production" on a remote server

cd madeline-weather-app
git init
heroku git:remote -a madeline-weather-app
