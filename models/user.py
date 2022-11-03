from init import db
# This is one of the places where the init items are imported

# the class User uses Sqlalchemy to create a table structure with column names and data types.
class User(db.model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    dob =db.Column(db.Date)
    # if user is younger than 18 he is not allowed to use the app