frst_num = int(input("Input first number: "))
scnd_num = int(input("Input second number: "))

try:
    result = frst_num / scnd_num
except ZeroDivisionError:
    scnd_num = int(input("Input not Zero as second number: "))
finally:
    result = frst_num / scnd_num
    print(result)
