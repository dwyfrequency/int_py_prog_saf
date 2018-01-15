import sqlite3, time

start = time.time()

#establish connection
connection = sqlite3.connect("jeopardy.db")

#cursor  is used to access the database
cursor = connection.cursor()
results = cursor.execute("Select name From category Limit 10")

print("Categories:")
for i in results:
    print("\t{}".format(i[0]))

connection.close()
end = time.time()

print("Total time: {}".format(end-start))
