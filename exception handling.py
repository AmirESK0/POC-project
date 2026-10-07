# exception handling = an event that interrupts the flow of a program
#                      (ZeroDivisionError, TypeError, ValueError and...)
#                      1.try,  2.except,  3.finally

# 1 / 0       ----> ZeroDivisionError
# 1 + "1"     ----> TypeError
# int("pizza) ----> ValueError

# try:
     # Try some code
# except:
     # Handle an Exception
# finally:
     # Do some clean up
try:
    number = int(input("please enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("u cant divide by zero IDIOT!")
except ValueError:
    print("enter only numbers please!")
except Exception:
    print("something went wrong!")
finally:
    print("do some clean up here")