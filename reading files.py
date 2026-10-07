# =========================================================
# PYTHON READING FILES (.txt, .json, .csv)
# =========================================================

import json
import csv


# =========================================================
# FILE PATHS
# =========================================================

txt_file = r"C:\Users\BEHNAM\OneDrive\Desktop\employees.txt"
json_file = r"C:\Users\BEHNAM\OneDrive\Desktop\employee.json"
csv_file = r"C:\Users\BEHNAM\OneDrive\Desktop\employees.csv"


# =========================================================
# READ TXT FILE
# =========================================================
# .read() returns the entire file as a string

try:

    with open(txt_file, mode="r") as file:

        content = file.read()
        print(content)

except FileNotFoundError:
    print("That file was not found.")

except PermissionError:
    print("You do not have permission to read this file.")


# =========================================================
# READ JSON FILE
# =========================================================
# json.load() converts JSON data into a Python dictionary

try:

    with open(json_file, mode="r") as file:

        content = json.load(file)

        print(content["job"])

except FileNotFoundError:
    print("That file was not found.")

except PermissionError:
    print("You do not have permission to read this file.")


# =========================================================
# READ CSV FILE
# =========================================================
# csv.reader() reads CSV data row by row

try:

    with open(csv_file, mode="r") as file:

        content = csv.reader(file)

        for row in content:
            print(row[2])

except FileNotFoundError:
    print("That file was not found.")

except PermissionError:
    print("You do not have permission to read this file.")