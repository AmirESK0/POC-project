# Python Writing Files (.txt, .json, .csv)

import csv
import json


# =========================================================
# FILE MODES
# =========================================================
# "r" = Read
# "w" = Write (overwrites file)
# "a" = Append (adds to file)
# "x" = Create (fails if file already exists)
#
# "t" = Text mode (default)
# "b" = Binary mode (images, videos, etc.)
# =========================================================

# =========================================================
# TXT FILE WRITING
# =========================================================

# A .txt file stores plain text

employees = [
    "Spongebob",
    "Patrick",
    "Squidward",
    "Sandy"
]

file_path = r"C:\Users\BEHNAM\OneDrive\Desktop\employees.txt"

try:

    with open(file_path, mode="w") as file:

        for employee in employees:
            file.write(employee + "\n")

    print(f"TXT file created successfully:\n{file_path}")

except PermissionError:
    print("Permission denied.")

except Exception as e:
    print(f"An error occurred: {e}")

# =========================================================
# JSON FILE WRITING
# =========================================================

# JSON stores data using key-value pairs
# Very common when working with APIs and databases

import json


employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "Cook"
}

file_path = r"C:\Users\BEHNAM\OneDrive\Desktop\employee.json"

try:

    with open(file_path, mode="w") as file:

        json.dump(employee, file, indent=4)

    print(f"JSON file created successfully:\n{file_path}")

except PermissionError:
    print("Permission denied.")

except Exception as e:
    print(f"An error occurred: {e}")

# =========================================================
# CSV FILE WRITING
# =========================================================

# CSV = Comma Separated Values
# Similar to an Excel spreadsheet (2D data)

import csv


employees = [
    ["name", "age", "job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 38, "Unemployed"],
    ["Squidward", 39, "Cashier"]
]

file_path = r"C:\Users\BEHNAM\OneDrive\Desktop\employees.csv"

try:

    with open(file_path, mode="w", newline="") as file:

        writer = csv.writer(file)

        for row in employees:
            writer.writerow(row)

    print(f"CSV file created successfully:\n{file_path}")

except PermissionError:
    print("Permission denied.")

except Exception as e:
    print(f"An error occurred: {e}")