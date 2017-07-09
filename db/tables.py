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


class Tracks(db.ORMBase):
    """Define an Object Relational Mapped class to represent the tracks table."""


class MediaTypes(db.ORMBase):
    """Define an Object Relational Mapped class to represent the mediatypes table."""


class Genres(db.ORMBase):
    """Define an Object Relational Mapped class to represent the genres table."""
