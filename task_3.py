class EvenNum (Exception):
    pass
class NegativeNum (Exception):
    pass


def check_exception(array):
    summ = 0
    for num in array:
        if num % 2 == 0:
            print(summ)
            raise EvenNum
        elif num < 0:
            print(summ)
            raise NegativeNum
        else:
            summ += num


lst1 = [3,5,7,9,-1]
print(f"List consist of: {lst1}")
try:
    check_exception(lst1)
except EvenNum:
    print("EvenNum")
except NegativeNum:

    print("NegativeNum")
