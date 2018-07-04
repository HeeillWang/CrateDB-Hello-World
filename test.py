from crate import client

connection = client.connect("http://localhost:4200/", username="crate")

cursor = connection.cursor()

cursor.execute("INSERT INTO tweets (id, text) VALUES (?,?)", ("floyd","hello world"))
