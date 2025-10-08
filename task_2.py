a = input()
b = input()

try:
    result = int(a)/int(b)
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Input number")
else:
    print(result)
finally:
    print("Done")

