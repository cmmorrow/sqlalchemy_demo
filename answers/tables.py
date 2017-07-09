# Import the ORMBase class
import db

# Import objects from sqlalchemy used to define ORM classes.
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship


# This is where the Declarative system is used to write classes that map to actual database tables.

class Artists(db.ORMBase):
    """Define an Object Relational Mapped class to represent the artists table."""

    # Declare the name of the artists table.
    __tablename__ = 'artists'

    # Declare variables that map to each of the fields in the artists table.
    # The variable name should match the field name in the artists table, but all lowercase.
    # The Column class is used to describe the schema.
    artistid = Column(Integer, primary_key=True)
    name = Column(String(120))

    # A relationship called albums is created to establish how the artists and albums tables should be joined.
    # SQLAlchemy has many ways of describing how tables can be joined.
    # The documentation on relationships can be found here:
    # http://http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html
    albums = relationship("Albums", back_populates='artists')


class Albums(db.ORMBase):
    """Define an Object Relational Mapped class to represent the albums table."""

    # Declare the name of the albums table.
    __tablename__ = 'albums'
    albumid = Column(Integer, primary_key=True)
    title = Column(String(160))
    artistid = Column(Integer, ForeignKey('artists.artistid'))

    """The ForeignKey for artistid is declared here and lets SQLAlchemy know that only values in artists.artistid are
    allowed in this field."""

    artists = relationship("Artists", back_populates='albums')
    tracks = relationship("Tracks", back_populates='albums')

    """The relationships in Albums tells SQLAlchemy how to join to the artists and tracks tables. The ForeignKey is used
    as the field to join on unless explicitly declared otherwise. If no ForeignKey is given and no join condition is
    declared, SQLAlchemy will attempt to join on primary keys."""


class Tracks(db.ORMBase):
    """Define an Object Relational Mapped class to represent the tracks table."""

    __tablename__ = 'tracks'
    trackid = Column(Integer, primary_key=True)
    name = Column(String(200))
    albumid = Column(Integer, ForeignKey('albums.albumid'))
    mediatypeid = Column(Integer, ForeignKey('media_types.mediatypeid'))
    genreid = Column(Integer, ForeignKey('genres.genreid'))
    composer = Column(String(220))
    milliseconds = Column(Integer)
    bytes = Column(Integer)
    unitprice = Column(Float)
    albums = relationship("Albums", back_populates='tracks')
    media_types = relationship("MediaTypes", back_populates='tracks')
    genres = relationship("Genres", back_populates='tracks')


class MediaTypes(db.ORMBase):
    """Define an Object Relational Mapped class to represent the mediatypes table."""

    __tablename__ = 'media_types'
    mediatypeid = Column(Integer, primary_key=True)
    name = Column(String(120))
    tracks = relationship("Tracks", back_populates='media_types')


class Genres(db.ORMBase):
    """Define an Object Relational Mapped class to represent the genres table."""

    __tablename__ = 'genres'
    genreid = Column(Integer, primary_key=True)
    name = Column(String(120))
    tracks = relationship('Tracks', back_populates='genres')
