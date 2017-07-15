# Import the Declarative objects from the db module.
from db import Session, Artists, Albums
from db import engine

# Instantiate a new Session object which serves as the interface to the database.
sess = Session()

#************** Be sure to have completed the Albums and Tracks tables before starting this challenge! **************

# Write a query that will display the 3 artists with the most albums as well as the number of albums.
# HINT: It will be necessary to aggregate results. Aggregation functions can be implemented using
# sqlalchemy.func. The documentation can be found here:
# http://http://docs.sqlalchemy.org/en/latest/core/sqlelement.html#sqlalchemy.sql.expression.func
query = sess.query(

)

# Print the results.
print()
