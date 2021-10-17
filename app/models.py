from app import db
from datetime import datetime
# from flask_login import UserMixin
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class PostgresModel(db.Model):
    __tablename__ = 'PostgresModel'
    __bind_key__ = 'db1'
    # __table_args__ = {'schema': 'schema_any'}
    # __abstract__ = True
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(120),unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    added_date = db.Column(db.DateTime,nullable = False,default = datetime.utcnow)
    # posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return self.first_name



class MySQLModel(db.Model):

    __tablename__ = 'MySQLModel'
    __bind_key__ = 'db2'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(120),unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    added_date = db.Column(db.DateTime,nullable = False,default = datetime.utcnow)

db.create_all()