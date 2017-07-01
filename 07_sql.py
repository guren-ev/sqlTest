# UPDATING & DELETING  data from DB

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # update data
    c.execute("UPDATE population SET population = 9000000000000000000000000000 WHERE city = 'New Yor City'")
    
    # delete data
    c.execute("DELETE FROM population WHERE city = 'boston'")

    print("\nNew Data welebi\n")
    
    c.execute("SELECT * FROM population ")
    
    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])
