# Select statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # use a for loop to iterate through the database
    for row in c.execute("SELECT firstname, lastname FROM employees"):
        print(row)
