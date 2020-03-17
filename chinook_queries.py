import os 
import sqlite3

#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "./data", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
print("Connection: ", connection)

cursor = connection.cursor()
print("Cursor: ", cursor)

# query = "SELECT * FROM customers;"
query = """
SELECT
    Country
    ,count(distinct CustomerId) as CustomerCount -- > 59
FROM customers
GROUP BY Country
ORDER BY CustomerCount DESC
LIMIT 5
"""


# result = cursor.execute(query)
# print("Result: ", result) # This returns a cursor object w/o results

result2 = cursor.execute(query).fetchall()
print("Result2: ", result2)

for row in result2:
    print(type(row))
    print(row)
    print(row["Country"])
    print(row["CustomerCount"])
    print("-------")