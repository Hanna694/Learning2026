import csv


def prettyTablePrint(data):
    # Maximale Breite jeder Spalte bestimmen
    column_widths = []

    for row in data:
        for i in range(len(row)):
            width = len(str(row[i]))

            if i >= len(column_widths):
                column_widths.append(width)
            elif width > column_widths[i]:
                column_widths[i] = width

    # Trennlinie erstellen
    separator = "+"
    for width in column_widths:
        separator += "-" * (width + 2) + "+"

    print(separator)

    # Tabelle ausgeben
    for row in data:
        line = "|"

        for i in range(len(row)):
            line += " " + str(row[i]).ljust(column_widths[i]) + " |"

        print(line)
        print(separator)


# Test mit dem Beispiel aus der Aufgabe
data = [
    ["Name", "Alter", "Beruf", "Wohnort"],
    ["Max", 28, "Ingenieur", "Darmstadt"],
    ["Anna", 22, "Studentin", "Stuttgart"],
    ["Hans", 34, "Lehrer", "München"],
    ["Mike", 77, "Fachinformatiker", "Hannover"]
]

prettyTablePrint(data)


# CSV-Datei einlesen
with open("gemuese_eigen.csv", "r", encoding="utf-8") as datei:
    reader = csv.reader(datei)
    csv_data = []

    for zeile in reader:
        csv_data.append(zeile)

print("\nGemüse-Tabelle:")
prettyTablePrint(csv_data)
