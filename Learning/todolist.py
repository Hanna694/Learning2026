todos = []

while True:
    print("--- ToDo-Liste ---")
    print("1. Aufgabe hinzufügen")
    print("2. Aufgaben anzeigen")
    print("3. Aufgabe als erledigt markieren")
    print("4. Beenden")

    auswahl = input("Auswahl: ")

    if auswahl == "1":
        aufgabe = input("Neue Aufgabe: ")
        todos.append([aufgabe, False])
        
    elif auswahl == "2":
        nummer = 1
        for todo in todos:
            if todo[1] == True:
                status = "X"
            else:
                status = " "

            print(f"{nummer}. [{status}] {todo[0]}")
            nummer += 1
            
    elif auswahl == "3":
        nummer = 1
        for todo in todos:
            print(f"{nummer}. {todo[0]}")
            nummer += 1

        nummer = int(input("Welche Aufgabe wurde erledigt? "))
        todos[nummer - 1][1] = True
        
        elif auswahl == "4":
        break

    else:
        print("Ungültige Eingabe.")
            