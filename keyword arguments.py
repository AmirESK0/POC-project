# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments does not matter
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

print(get_phone(country=1, area=123, last=7890, first=456))