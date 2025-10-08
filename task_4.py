
arr = [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]

def check_exception(lst):
    try:
        i = int(input("input index of array: "))
        print(lst[i])
    except IndexError:
        print("Index out of range")

if __name__ == "__main__":
    check_exception(arr)
