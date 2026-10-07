# class variable = shared among all instances of a class
#                  defined outside the constructor
#                  allow u to share data among all objects created from that



class Student:

    # Class variables (shared by all students)
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        # Instance variables (unique to each student)
        self.name = name
        self.age = age

        # Update class variable
        Student.num_students += 1


student1 = Student("Larry", 21)
student2 = Student("patrick", 31)

print(student2.name)                       # patrick
print(student2.age)                        # 31
print(Student.class_year)                  # 2025
print(Student.num_students)                # 2
print(f"my class of {Student.class_year} has {Student.num_students} students")