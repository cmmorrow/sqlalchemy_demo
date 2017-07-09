from db import Session, Artists, Albums, Tracks
from db import engine
import pandas as pd
from sqlalchemy import func, desc

sess = Session()

# Example 1
# query = sess.query(
#     Albums.title,
#     Artists.name,
#     Tracks.name
# ).join(
#     Artists, Tracks
# ).filter(
#     Artists.name == 'Ozzy Osbourne'
# )

# example1 = pd.read_sql_query(query.statement, engine)
# print(example1)

# Example 2
# query = sess.query(
#     Artists.name,
#     func.count(Albums.title).label('number_of_albums')
# ).join(
#     Albums
# ).group_by(
#     Artists.name
# ).order_by(
#     desc('number_of_albums')
# )

# example2 = pd.read_sql_query(query.statement, engine)
# print(example2[:3])

# Example 3
# washed_out = Artists(name='Washed Out')
# mister_mellow = Albums(title='Mister Mellow')
# washed_out.albums = [
#     mister_mellow
# ]
# mister_mellow.tracks = [
#     Tracks(name='Title Card', mediatypeid=1, genreid=1),
#     Tracks(name='Burn Out Blues'),
#     Tracks(name='Time Off'),
#     Tracks(name='Floating By'),
#     Tracks(name="I've Been Daydreaming My Entire Life"),
#     Tracks(name='Hard to Say Goodbye'),
#     Tracks(name='Down and Out'),
#     Tracks(name='Instant Calm'),
#     Tracks(name='Zonked'),
#     Tracks(name='Get Lost'),
#     Tracks(name='Easy Does It'),
#     Tracks(name='Million Miles Away')
# ]
# # sess.add(washed_out)
# sess.add(mister_mellow)
# sess.commit()
#
# query = sess.query(
#     Artists.name,
#     Albums.title,
#     Tracks.name.label('track')
# ).join(
#     Albums, Tracks
# ).filter(
#     Artists.name == 'Washed Out'
# )
#
# example3 = pd.read_sql_query(query.statement, engine)
# print(example3)

query = sess.query(
    MediaTypes
)

print(pd.read_sql_query(query.statement, engine))