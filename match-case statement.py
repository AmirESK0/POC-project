# match-case statement (switch) = an alternative to using many "elif" statements
#         | = or                  execute some code if a value matches a  "case"
#                                 benefits : cleaner and syntax is more readable
def day_of_the_week(day):
    if day == 1:
        return "it is monday"
    elif day == 2:
        return "it is tuesday"
    elif day == 3:
        return "it is Wednesday"
    elif day == 4:
        return "it is Thursday"
    elif day == 5:
        return "it is Friday"
    elif day == 6:
        return "it is Saturday"
    elif day == 7:
        return "it is sunday"
    else:
        return "not a valid day"


def day_of_the_week_updated(day):
    match day:
        case 1:
            return "it is monday"
        case 2:
            return "it is tuesday"
        case 3:
            return "it is Wednesday"
        case 4:
            return "it is Thursday"
        case 5:
            return "it is Friday"
        case 6:
            return "it is Saturday"
        case 7:
            return "it is sunday"
        case _:
            return "not a valid day"

def is_weekend(day):
    match day:
        case "monday" | "tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "sunday":
            return True
        case _:
            return False

print(is_weekend(1))