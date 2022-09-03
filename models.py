
from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# moment = Moment(app)
# app.config.from_object('config')
db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate. **DONE
    genres = db.Column(db.ARRAY(db.String(120)))
    website_link = db.Column(db.String(500))
    looking_talent = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='venue', lazy=True)

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    # genres = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website_link = db.Column(db.String(500))
    looking_venues = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='artist', lazy=True)
    

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
  __tablename__ = 'Show'

  id = db.Column(db.Integer, primary_key=True)
  venue_id = db.Column(db.Integer, db.ForeignKey(
        'Venue.id'), nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey(
        'Artist.id'), nullable=False)
  start_time =  db.Column(db.DateTime)
  # artist = db.relationship('Artist', back_populates = 'artist_show' )
  # venue = db.relationship('Venue', back_populates = 'venue_show' )