from flask import Flask,request
from flask_migrate import Migrate
from flask_restful import Api, Resource  
from dotenv import load_dotenv
from server.models.db import db

load_dotenv()

app = Flask(__name__)
# Loads from FLASK_SQLALCHEMY_DATABASE_URI and others
app.config.from_prefixed_env()  

db.init_app(app)
migrate = Migrate(app, db)

# register api routes
from server.routes.students_route import api as students_api
from server.routes.courses_route import api as courses_api
from server.routes.enrollments_route import api as enrollments_api

students_api.init_app(app)
courses_api.init_app(app)
enrollments_api.init_app(app)

if __name__ == '__main__':
    app.run()
