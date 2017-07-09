# Import the Declarative objects from the db module.
from db import Session, Artists, Albums
from db import engine
import pandas as pd
from sqlalchemy import func, desc

# Instantiate a new Session object which serves as the interface to the database.
sess = Session()

# Write a query that will display the 3 artists with the most albums as well as the number of albums.
# HINT: It will be necessary to aggregate results. Aggregation functions can be implemented using
# sqlalchemy.func. The documentation can be found here:
# http://http://docs.sqlalchemy.org/en/latest/core/sqlelement.html#sqlalchemy.sql.expression.func
query = sess.query(
    Artists.name,
    func.count(Albums.title).label('number_of_albums')
).join(
    Albums
).group_by(
    Artists.name
).order_by(
    desc('number_of_albums')
)

"""The equivalant SQL for this query is:
"SELECT artists.name, count(albums.title) AS number_of_albums
FROM artists
    JOIN albums
        ON artists.artistid = albums.artistid
GROUP BY artists.name
ORDER BY number_of_albums DESC"

The group_by and order_by functions work very similar to the equivalent SQL clauses. The label function is used to to
specify a name for the aggregated count column, otherwise, SQLAlchemy would use the default name of "count_1."
"""

# Print the results.
example2 = pd.read_sql_query(query.statement, engine)
print(example2[:3])
