from crate import client

connection = client.connect("http://localhost:4200/", username="crate")

cursor = connection.cursor()

while True:
    print("Pick operation:")
    print("1 - INSERT")
    print("2 - DELETE")
    print("3 - SELECT")
    print("4 - UPDATE")
    print("0 - Terminate the program")
    pick = int(input())

    if pick == 0:
        break
    elif pick == 1:
        cursor.execute("INSERT INTO newtable (id) VALUES (?)", ("floyd",))
    elif pick == 2:
        cursor.execute("DELETE FROM newtable WHERE id = ?", ("floyd",))
    elif pick == 3:
        cursor.execute("SELECT * FROM newtable WHERE id = ?", ("floyd",))
    elif pick == 4:
        cursor.execute("UPDATE newtable SET id = ? WHERE id = ?", ("pink", "floyd"))

    result = cursor.fetchone()
    print(result)
    print(cursor.description)






