# Static methods = a method that belongs to a class rather than any object from that class (instance)
#                  usually used for general utility function
# Instance methods = best for operations on instances of that class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Instance method:
# - Works on ONE specific object
# - Needs access to object data (self)
#
# Static method:
# - Belongs to the class itself
# - Does NOT use self
# - Used for rules / utility checks related to the class

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Instance method:
    # Uses self → depends on THIS employee
    def get_info(self):
        return f"{self.name} = {self.position}"

    # Static method:
    # General rule that does NOT depend on an employee object
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "janitor"]
        return position in valid_position

# Creating employee objects (instances)
employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")


# Static method call:
# No object needed → rule only
print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("CEO"))

# Instance method call:
# Requires an object → uses self
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())