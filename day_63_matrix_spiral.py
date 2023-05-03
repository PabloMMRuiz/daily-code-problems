"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Amazon.
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
For example, given the following matrix:"""

def column_getter(list_of_lists, col)->list:
    return [l[col]for l in list_of_lists]

def spiral(list_Of_lists: list):
    tick = 1

    while len(list_Of_lists)>0:
        if tick ==1:
            for i in list_Of_lists[0]:
                print(i)
            list_Of_lists.pop(0)
            tick +=1
        elif tick == 2:
            for i in column_getter(list_Of_lists, -1):
                print(i)
            for l in list_Of_lists:
                l.pop(-1)
            tick +=1
        elif tick ==3:
            for i in list_Of_lists[-1][::-1]:
                print(i)
            list_Of_lists.pop(-1)
            tick +=1
        else:
            tick = 1
            for i in column_getter(list_Of_lists, 0)[::-1]:
                print(i)
            for l in list_Of_lists:
                l.pop(0)
    
spiral([[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]])