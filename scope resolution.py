#   variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) local -> enclosed -> global -> built-in

# local:
def func1():
    x = 1
    print(x)
def func2():
    x = 2
    print(x)
func1()
func2()

# enclosed:
def func3():
    x = 3

    def func4():
        x = 4
        print(x)
    func4()
func3()

# global:
def func5():
    print(x)
def func6():
    print(x)
x = 5
func5()
func6()

# built-in:
from math import e
def func7():
    print(e)
# e = 5
func7()