# *args    = allows u to pass multiple non_key arguments <class 'tuple'>
# **kwargs = allows u to pass multiple keyword arguments <class 'dict'>
#            * unpacking operator - the parameter name can vary
#            1. positional, 2. default, 3. keyword, 4. ARBITRARY


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(5, 7))
print("")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="sunshine st.",
              city="los angeles",
              state="california",
              zip="54321")
print("")


def shipping_label(*names, **addresses):
    for name in names:
        print(name, end=" ")
    print("")

    if "apt" in addresses:
        print(f"{addresses.get('street')} {addresses.get('apt')}")
    elif "pobox" in addresses:
        print(f"{addresses.get('street')}")
        print(f"{addresses.get('pobox')}")
    else:
        print(f"{addresses.get('street')}")
    print(f"{addresses.get('street')} {addresses.get('street')}, {addresses.get('street')}")


shipping_label("Dr.", "spongebob", "squarepants", "III",
               street="123 sunshine st.",
               apt="#100",
               city="los angeles",
               state="california",
               zip="54321")
print("")