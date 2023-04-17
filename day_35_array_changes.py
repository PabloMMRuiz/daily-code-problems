"""Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, 
the Gs come second, and the Bs come last. 
You can only swap elements of the array.
Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B']."""


def arr_segregate(arr: list)->list:
    length = len(arr)
    free_start = 0
    for i in range(0, length):
        if arr[i] == "R":
            arr[i], arr[free_start] = arr[free_start], arr[i]
            free_start +=1
    for i in range(free_start, length):
        if arr[i] == "G":
            arr[i], arr[free_start] = arr[free_start], arr[i]
            free_start +=1
    return arr

print(arr_segregate(['G', 'B', 'R', 'R','G', 'B', 'R', 'G','B','G']))

