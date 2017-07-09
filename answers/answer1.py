# Import the Declarative objects from the db module.
from db import Session, Artists, Albums, Tracks
from db import engine
import pandas as pd


# Instantiate a new Session object which serves as the interface to the database.
sess = Session()

# Write a query that will select the Artists.name, Albums.title and Tracks.name for "Ozzy Osbourne."
# HINT: It will be necessary to join the artists, albums and tracks tables.
# There are several ways to join tables in SQLAlchemy and the documentation can be found here:
# http://http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.join
query = sess.query(
    Artists.name,
    Albums.title,
    Tracks.name.label('track')
).join(
    Albums, Tracks
).filter(
    Artists.name == 'Ozzy Osbourne'
)

"""The equivalant SQL for this query is:
"SELECT artists.name, albums.title, tracks.name
FROM artists
    JOIN albums
        ON artists.artistid = albums.artistid
    JOIN tracks
        ON albums.albumid = tracks.albumid
WHERE artists.name = 'Ozzy Osbourne'"

Because SQLAlchemy knows the tables the fields come from, it isn't
necessary to write a FROM clause. Also, as long as the relationships
are setup properly in the Declarative objects, joining tables is as
simple as specifying the Declaratives.
"""

# Print the results.
print(pd.read_sql_query(query.statement, engine))

"""Pandas can directly import from SQLAlchemy by using the read_sql_query function."""
