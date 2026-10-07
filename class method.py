# class method = allows operations related the class itself
#                take (cls) as the first parameter, which represents the class itself
#                self = refers to any object created from that class
#                cls = refers to the class, not any objects

# instance method = best for operations on the instances of the class (objects)
# static method = best for utility functions that do not need access to class data
# class method = best for class_level data or require access to the class itself


class Student:

    num_of_std = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.num_of_std += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_num_of_std(cls):
        return f"total # of students = {cls.num_of_std}"
    @classmethod
    def get_average_gpa(cls):
        if cls.num_of_std == 0:
            return 0
        else:
            return f"the average gpa is: {cls.total_gpa / cls.num_of_std:.2f}"


student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_num_of_std())
print(Student.get_average_gpa())