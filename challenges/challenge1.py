# Import the Declarative objects from the db module.
from db import Session, Artists, Albums, Tracks
from db import engine

# Instantiate a new Session object which serves as the interface to the database.
sess = Session()

#************** Be sure to have completed the Albums and Tracks tables before starting this challenge! **************

# Write a query that will select the Artists.name, Albums.title and Tracks.name for "Ozzy Osbourne."
# HINT: It will be necessary to join the artists, albums and tracks tables.
# There are several ways to join tables in SQLAlchemy and the documentation can be found here:
# http://http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.join
query = sess.query(

)

# Print the results.
print()
