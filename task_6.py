
def square_num(num):
    return math.sqrt(num)
a = int(input())
try:
    print(square_num(a))
except NameError:
    print("name 'math' is not defined. Did you forget to import 'math'? Joke, I import it for u")
    import math
    try:
        print(square_num(a))
    except ValueError:
        print("Wrong number for sqrt")


