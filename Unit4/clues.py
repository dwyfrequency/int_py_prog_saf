import sqlite3, time

start = time.time()

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("""Select text, value
               From clue import Limit 10;""")
results = cursor.fetchall()

for clue in results:
    question, points = clue
    print("The question for {} points is: {}\n".format(points, question))

connection.close()

end = time.time()
print("Total time: {}".format(end-start))
