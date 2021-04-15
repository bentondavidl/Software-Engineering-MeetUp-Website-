from database.database import db

class User(db.Model):
    # add records here
    id = db.Column('id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String(50), nullable=False)
    last_name = db.Column('last_name', db.String(50), nullable=False)
    password = db.Column('password', db.String(50), nullable=False)
    email = db.Column('email', db.String(50), unique=True, nullable=False)
    events = db.relationship('Event', backref='user', lazy=True)
    rsvps = db.relationship('RSVP', backref='user', lazy=True)
    # add parameters for each field
    def __init__(self, id, first_name, last_name, password, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name 
        self.password = password
        self.email = email

class Event(db.Model):
    # add records here
    id = db.Column('id', db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column('name', db.String(100), nullable=False)
    is_private = db.Column('is_private', db.Boolean, nullable=False)
    location = db.Column('location', db.String(200), nullable=False)
    start_time = db.Column('start_time', db.DateTime, nullable=False)
    end_time = db.Column('end_time', db.DateTime)
    description = db.Column('description', db.VARCHAR, nullable=False)
    rsvps = db.relationship('RSVP', backref='event', cascade='all, delete-orphan', lazy=True)
    # add parameters for each field
    def __init__(self, id, host_id, name, is_private, location, start_time, end_time, description):
        self.id = id
        self.host_id = host_id
        self.name = name
        self.is_private = is_private
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.description = description


class RSVP(db.Model):
    # same as above
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    guests = db.Column('guests', db.SmallInteger, nullable=False)

    def __init__(self, user_id, event_id, guests):
        self.user_id = user_id
        self.event_id = event_id
        self.guests = guests
    

