

def transform (num: str) -> float:
    return float(num)

try:
    inpt = input("Input number: ")
    print(transform(inpt))
except ValueError:
    print("Can't convert to float")

