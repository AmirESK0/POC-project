# membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, dictionary)
#                        1. in
#                        2. not in

word = "APPLE"

letter = (input("guess the letter in the secret word: "))

if letter in word:
    print(f"there is a {letter}")
else:
    print(f"{letter} was not found")

print("")

students = {"spongebob", "patrick", "sandy"}

student = input("enter the name of a student: ")

if student not in students:
    print(f"{student} is not a student")
else:
    print(f"{student} is a student")

print("")

grades = {"spongebob": "A", "patrick": "B", "sandy": "C"}
student = input("enter the name of a student: ")

if student in grades:
    print(f"{student} has a grade of {grades[student]}")
else:
    print(f"{student} is a student")