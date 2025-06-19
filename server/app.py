from flask import Flask,request
from flask_migrate import Migrate
from flask_restful import Api, Resource  
from dotenv import load_dotenv
from models import db,Student,Course,Enrollment,Gender
from controllers import controller


load_dotenv()

app = Flask(__name__)
# Loads from FLASK_SQLALCHEMY_DATABASE_URI and others
app.config.from_prefixed_env()  

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return 'Home'

crud_routes = [
    {
        "name":"students",
        "model":Student
     },
     {
        "name":"courses",
        "model":Course
     },
     {
        "name":"enrollments",
        "model":Enrollment
     },
     {
        "name":"genders",
        "model":Gender
     }
]
for route in crud_routes:
    students_bp = controller(**route)
    app.register_blueprint(students_bp,url_prefix=f'/{route["name"]}')


if __name__ == '__main__':
    app.run()
