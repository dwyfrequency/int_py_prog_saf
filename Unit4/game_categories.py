import sqlite3, time

start = time.time()

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("""Select game From category
               ORDER BY RANDOM() Limit 1;""")
results = cursor.fetchall()
# print(results)
game_id = results[0][0]
print("Categories for game {}".format(game_id))

# Get the categories for the game
q = """Select name, round From category
Where game = {} Order By round""".format(game_id)
cursor.execute(q)
results = cursor.fetchall()
print(results)

# Process the results
for result in results:
    # unpack tuple
    name, round = result
    print("Round {}: {}".format(round, name))

connection.close()

end = time.time()
print("Total time: {}".format(end-start))
