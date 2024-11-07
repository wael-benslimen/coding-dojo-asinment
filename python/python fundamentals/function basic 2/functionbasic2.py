def countdown(x):
    list = []
    for i in range(x,-1,-1):
        list.append(i)
    return(list)
x = countdown(5)
print(x)
print("*"*10)
def print_and_return(array):
    print(array[0])
    return array[1]
x = print_and_return([1,2])
print(x)
print("*"*10)
def first_plus_length(array):
    x = len(array) + array[0]
    return x
x = first_plus_length([1,2,3,4])
print(x)
print("*"*10)
def values_grater_than_second(array):
    graterlist = []
    for i in range(len(array)):
        if array[i] > array[1]:
            graterlist.append(array[i])
    if len(graterlist) == 0:
        return False
    return graterlist
x = values_grater_than_second([1,2,3,4,5,6,7])
print(x)
print("*"*10)
def this_length_that_value(size,value):
    list = []
    for i in range(int(size)):
        list.append(value)
    return list
x = this_length_that_value(5,7)
print(x)
