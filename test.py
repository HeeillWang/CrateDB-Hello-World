from crate import client

connection = client.connect("http://localhost:4200/", username="crate")

cursor = connection.cursor()

while True:
    print("Pick operation:")
    print("1 - INSERT")
    print("2 - DELETE")
    print("3 - SELECT")
    print("4 - UPDATE")
    print("5 - Select all")
    print("0 - Terminate the program")
    pick = int(input())

    if pick == 0:
        break
    elif pick == 1:
        print("Enter ID:")
        str = input()
        cursor.execute("INSERT INTO newtable (id) VALUES (?)", (str,))
    elif pick == 2:
        print("Enter ID:")
        str = input()
        cursor.execute("DELETE FROM newtable WHERE id = ?", (str,))
    elif pick == 3:
        print("Enter ID:")
        str = input()
        cursor.execute("SELECT * FROM newtable WHERE id = ?", (str,))
    elif pick == 4:
        print("Enter ID that you want to update:")
        str = input()

        print("Enter new ID:")
        str2 = input()
        cursor.execute("UPDATE newtable SET id = ? WHERE id = ?", (str2, str,))
    elif pick == 5:
        cursor.execute("SELECT * FROM newtable")

    result = cursor.fetchall()
    print(result)
    print(cursor.description)






