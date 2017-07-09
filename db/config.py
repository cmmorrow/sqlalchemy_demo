from os import sep, pardir
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Declare the path to the sqlite database file.
path = pardir + sep + 'db' + sep + 'files' + sep

# Declare the name and path of the sqlite database file.
db_file = path + 'chinook.db'

# Instantiate the engine that will be used to connect to our sqlite database.
engine = create_engine('sqlite:///' + db_file, echo=True)

# Instantiate a Session object that will serve as a factory for creating Session objects.
Session = sessionmaker(bind=engine)

# Instantiate the base Object Relational Mapper object.
# All declared ORM classes will inherit from this object.
ORMBase = declarative_base()
