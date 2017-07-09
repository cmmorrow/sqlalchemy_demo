# Import the Declarative objects from the db module.
from db import Session, Albums, Tracks, Artists
from db import engine
import pandas as pd

# Instantiate a new Session object which serves as the interface to the database.
sess = Session()

# Insert the Jamiroquai album Travelling Without Moving into the database along with all of its tracks.
# Use 1 for mediatypeid and genreid for the sake of simplicity, and use 0.99 for unitprice.
# For composer and milliseconds, use the following page:
# https://en.wikipedia.org/wiki/Travelling_Without_Moving
# Convert the track length to milliseconds and use milliseconds x 10 to get an approximate number for bytes.
# After inserting the new tracks, display the results from the database to verify the insert worked.

# First, create a new Artists object.
jamiroquai = Artists(name='Jamiroquai')

# Next, create a new Albums object for "Travelling Without Moving."
travelling = Albums(title='Travelling Without Moving')

# Associate the new Album with the Artist.
jamiroquai.albums = [
    travelling
]

"""Since an artist can have more than one album, the albums attribute of the Artists class can accept a list of Albums
 objects."""

# Associate all the Tracks with the Album.
travelling.tracks = [
    Tracks(name='Virtual Insanity',
           mediatypeid=1,
           genreid=1,
           composer='Jay Kay, Toby Smith',
           milliseconds=340000,
           bytes=3400000,
           unitprice=0.99),
    Tracks(name='Cosmic Girl',
           mediatypeid=1,
           genreid=1,
           composer='Jay Kay, Derrick McKenzie',
           milliseconds=243000,
           bytes=2430000,
           unitprice=0.99),
    Tracks(name='Use the Force',
           mediatypeid=1,
           genreid=1,
           composer='Jay Kay, Toby Smith, Derrick McKenzie, Sola Akingbola',
           milliseconds=240000,
           bytes=2400000,
           unitprice=0.99),
    Tracks(name='Everyday',
           mediatypeid=1,
           genreid=1,
           composer='Jay Kay, Toby Smith, Stuart Zender',
           milliseconds=268000,
           bytes=2680000,
           unitprice=0.99),
    Tracks(name='Alright',
           mediatypeid=1,
           genreid=1,
           composer='Jay Kay, Toby Smith',
           milliseconds=265000,
           bytes=2650000,
           unitprice=0.99),
    Tracks(name='High Times',
           mediatypeid=1,
           genreid=1,
           composer='Jay Kay, Toby Smith, Stuart Zender, Derrick McKenzie',
           milliseconds=358000,
           bytes=3580000,
           unitprice=0.99),
    Tracks(name='Drifting Along',
           mediatypeid=1,
           genreid=1,
           composer='Jay Kay, Derrick McKenzie, Simon Katz, Stuart Zender',
           milliseconds=246000,
           bytes=2460000,
           unitprice=0.99),
    Tracks(name='Didjerama',
           mediatypeid=1,
           genreid=1,
           composer='Jay Kay, Wallis Buchanan, Derrick McKenzie',
           milliseconds=230000,
           bytes=2300000,
           unitprice=0.99),
    Tracks(name='Didjital Vibrations',
           mediatypeid=1,
           genreid=1,
           composer='Jay Kay, Wallis Buchanan, Stuart Zender',
           milliseconds=349000,
           bytes=3490000,
           unitprice=0.99),
    Tracks(name='Travelling Without Moving',
           mediatypeid=1,
           genreid=1,
           composer='Jay Kay',
           milliseconds=220000,
           bytes=2200000,
           unitprice=0.99),
    Tracks(name='You Are My Love',
           mediatypeid=1,
           genreid=1,
           composer='Jay Kay',
           milliseconds=235000,
           bytes=2350000,
           unitprice=0.99),
    Tracks(name='Spend a Lifetime',
           mediatypeid=1,
           genreid=1,
           composer='Jay Kay, Toby Smith, Stuart Zender',
           milliseconds=254000,
           bytes=2540000,
           unitprice=0.99)
]

"""In practice, ORM objects would not be explicitly created this way and are better suited to being created with a
function and loop. For example:

>>> def make_tracks(title, mediatypeid, genreid, composer, millsec, price):
...     return Tracks(name=title,
...                   mediatypeid=mediatypeid,
...                   genreid=genreid,
...                   composer=composer,
...                   milliseconds=millsec,
...                   unitprice=price)
...
>>> make_tracks('Virtual Insanity', 1, 1, 'Jay Kay, Toby Smith', 340000, 3400000, 0.99)
<Tracks(name='Virtual Insanity', mediatypeid=1, genreid=1, composer='Jay Kay, Toby Smith', milliseconds=340000, bytes=34
00000, unitprice=0.99)>
"""

# Add and commit the new Album.
sess.add(travelling)
sess.commit()

# Write a query that will select the Artists.name, Albums.title and Tracks.name for "Travelling Without Moving."
query = sess.query(
    Artists.name,
    Albums.title,
    Tracks.name.label('track')
).join(
    Albums, Tracks
).filter(
    Artists.name == 'Jamiroquai',
    Albums.title == 'Travelling Without Moving'
)

"""Notice how the same Session object was used for adding records and querying the database.
SQLAlchemy will keep the session open until it knows that the seesion won't be needed anymore."""

# Print the results.
print(pd.read_sql_query(query.statement, engine))

# ****************************************** EXTRA CHALLENGE ******************************************
# Generalize the code used to insert records into the database into a function.
# Next, allow the function to accept a URL to a Wikipedia page with a Track List table.
# The function should be able to scrape the HTML from the Wikipedia page and insert the records into the database.
# The beautifulsoup python package is a great way work with text scraped from the web.
# NOTE: Not all Wikipedia pages for albums are formatted in the same way. At bare minimum, try to scrape the track
# title, writer and length.
