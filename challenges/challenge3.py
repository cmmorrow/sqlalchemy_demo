# Import the Declarative objects from the db module.
from db import Session, Albums, Tracks, Artists
from db import engine

# Instantiate a new Session object which serves as the interface to the database.
sess = Session()

#************** Be sure to have completed the Albums and Tracks tables before starting this challenge! **************

# Insert the Jamiroquai album Travelling Without Moving into the database along with all of its tracks.
# Use 1 for mediatypeid and genreid for the sake of simplicity, and use 0.99 for unitprice.
# For composer and milliseconds, use the following page:
# https://en.wikipedia.org/wiki/Travelling_Without_Moving
# Convert the track length to milliseconds and use milliseconds x 10 to get an approximate number for bytes.
# After inserting the new tracks, display the results from the database to verify the insert worked.

# First, create a new Artists object.
jamiroquai = Artists(name='Jamiroquai')

# Next, create a new Albums object for "Travelling Without Moving."


# Associate the new Album with the Artist.
jamiroquai.albums = [

]

# Associate all the Tracks with the Album.


# Add and commit the new Album.
sess.add(

)
sess.commit()

# Write a query that will select the Artists.name, Albums.title and Tracks.name for "Travelling Without Moving."
query = sess.query(

)

# Print the results.
print()

# ****************************************** EXTRA CHALLENGE ******************************************
# Generalize the code used to insert records into the database into a function.
# Next, allow the function to accept a URL to a Wikipedia page with a Track List table.
# The function should be able to scrape the HTML from the Wikipedia page and insert the records into the database.
# The beautifulsoup python package is a great way work with text scraped from the web.
# NOTE: Not all Wikipedia pages for albums are formatted in the same way. At bare minimum, try to scrape the track
# title, writer and length.
