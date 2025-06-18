from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  MetaData, ForeignKey
from sqlalchemy.orm import relationship


metata = MetaData()

db = SQLAlchemy(metadata=metata)