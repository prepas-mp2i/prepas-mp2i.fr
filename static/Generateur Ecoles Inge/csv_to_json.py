import csv
import json

with open("ecoles.csv", "r") as fichier_csv:
    with open("ecoles.json", "w") as fichier_json:
        fichier_csv.readline()
        spamreader = csv.reader(fichier_csv, delimiter=";")
        fichier_json.write("{\n")
        for row in spamreader:
            fichier_json.write(f'    "{row[0]}" : ')
            fichier_json.write("{")
            if row[1] != "":
                fichier_json.write(f'"Ville" : "{row[1]}", ')
            if row[2] != "":
                fichier_json.write(f'"Places" : "{row[2]}"')
            fichier_json.write("},\n")  # Penser à enlever la vigule de fin
        fichier_json.write("}\n")
