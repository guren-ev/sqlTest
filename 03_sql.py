#excumentary Method

import sqlite3

with sqlite3.connect("new.db") as connection:

    c =  connection.cursor()

    # insert multiple record using tuples

    cities = [
            ('boston', 'ma', 483974893274 ),
            ('michigan', 'mi', 8978978979),
            ('chicago', 'li', 90989786876 ),
            ('houston', 'tx', 8997896786786 ),
            ('Phoenix', 'az', 89986786768 ),
           ]
# insert data into table

    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)    
