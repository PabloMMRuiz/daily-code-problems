"""Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?"""

def solNoLineal(l):
    if len(l)<3:
        return max(l)
    suma = [0 for a in l]
    suma[0]=l[0]
    suma[1]=l[1]
    for i, num in enumerate(l[2:]):
        suma[i+2] = max([(num + x) for x in suma[:i+1]])
    return max(suma)

def solLineal(l):
    if len(l)<3:
        return max(l)
    suma1 = 0
    suma2 = 0
    for n in l:
        suma1, suma2 = max(suma2 + n, n), max(suma1, suma2)
    return max(suma1, suma2)
if __name__ == "__main__":
    print(solNoLineal([-2,-2, -4, -6, -5]))
    print(solLineal([-2,-2, -4, -6, -5]))
    print(solNoLineal([5, 5, 10, 100, -10, -5,20,-10]))
    print(solLineal([5, 5, 10, 100, -10, -5, 20,-10]))