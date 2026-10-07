# function = a block of reusable code
#            place () after the function name to invoke it

# return = statement used to end a function
#          and send a result back to the caller
# ----------------------------------------------------------------------------
# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of CHF{amount} is due: {due_date}")
# display_invoice("Ali_64", 240, "1st march")
# ----------------------------------------------------------------------------
# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = (x - y)
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(subtract(6, 3))
# print(multiply(3, 1))
# print(int(divide(15, 5)))
# ----------------------------------------------------------------------------
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")

print(full_name)