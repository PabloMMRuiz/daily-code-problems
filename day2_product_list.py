"""Given an array of integers, return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would
be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]"""

def solWithDivision(data):
    product = 1.0
    for i in data:
        product *= i
    return[product/i for i in data]
#TODO encontrar solucion mas eficiente
def solWithoutDivision(data):
    res = [1 for i in data]
    for index, n in enumerate(data):
        for index2 in range(len(res)):
            if index != index2:
                res[index2] *= n
    return res


if __name__ == "__main__":
    print(solWithDivision([1,2,3,4,5]))
    print(solWithoutDivision([1,2,3,4,5]))
