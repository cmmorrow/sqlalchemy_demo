# SQLAlchemy Demo
This demo serves as an introduction to SQLAlchemy by providing 3 guided exercises.

## Getting Started
The exercises in this demo require python 2.7 or 3.3+. The easiest way to install python on your system is with Anaconda or Miniconda.
If using a previously installed version of python, the sqlite3 package must be installed as well as SQLAlchemy. sqlite3 comes packaged with most versions of python and SQLAlchemy can be installed using the following command:
```shell
> pip install SQLAlchemy
```
Next, fork this repo by clicking the "Fork" button at the top right of this GitHub page. After forking the sqlalchemy_demo, click on the "Clone or download" button and copy the url to the clipboard. Finally, in a terminal window, navigate to the directory where you want to install the repo, then clone it with the following command:
```shell
> git clone https://github.com/cmmorrow/sqlalchemy_demo.git
```
Now, you're all set!

## Working Through the Demo
The top level of the repo has three directories, *answers*, *challenges* and *db*. The *db* directory is where the db engine, session, declarative base and tables are defined. The *challenges* directory has the exercises to work through, and *answers* the answers to the exercises.

Before getting started on the exercises, make sure to add all the fields for the Albums, Tracks, MediaTypes and Genres tables. The Artists table has already been completed, and can be used as a reference.