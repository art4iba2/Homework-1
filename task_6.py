
def square_num(num):
    return math.sqrt(num)
a = int(input())
try:
    print(square_num(a))
except NameError:
    print("name 'math' is not defined. Did you forget to import 'math'?")
    print("Importing math module...")
    import math
    print("Math module imported.")
    try:
        print(square_num(a))
    except ValueError:
        print("Wrong number for sqrt")



