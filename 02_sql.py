# Real Python book, script to create a DB

# Create a SQLite Database and table

# import sqlite3 ibrary
import sqlite3

# create a new database if it does not exist
# get a cursor object used to execute SQL commands
# inset data
# commit changes
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population Values('Puerto Rico', 'PY', 908400000)")
    c.execute("INSERT INTO population Values('Colorado', 'CL', 765800000)")
    c.close()


