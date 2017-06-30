# Real Python book, script to create a DB

# Create a SQLite Database and table

# import sqlite3 ibrary
import sqlite3

# create a new database if it does not exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
                """)

#close the database connection
conn.close()


