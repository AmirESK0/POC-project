# list comprehension = a concise way to create a list in python
#                      compact and easier to read than the traditional loops
#                      [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)
# print(doubles)

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
square = [z * z for z in range(1, 11)]
print(doubles)
print(triples)
print(square)

fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
fruits2 = [fruit[0].upper() for fruit in ["apple", "orange", "banana", "coconut"]]
print(fruits)
print(fruits2)

numbers = [-1, 2, -3, -4, 5, -6]
positive_numbers = [number for number in numbers if number >= 0]
negative_numbers = [number for number in numbers if number < 0]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 == 1]
print(positive_numbers)
print(negative_numbers)
print(even_numbers)
print(odd_numbers)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grade = [grade for grade in grades if grade >= 60]
failing_grades = [grade for grade in grades if grade <= 60]
print(passing_grade)
print(failing_grades)