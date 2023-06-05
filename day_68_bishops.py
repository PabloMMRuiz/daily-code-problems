"""
On our special chessboard, two bishops attack each other if they share the same diagonal. 
This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. 
Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) 
is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.

"""


def attacks(positions: list):
    dimension = max(max(t[0], t[1]) for t in positions)
    res = 0
    for bishop in positions:
        x , y = bishop
        #First diagonal: \
        while x <= dimension and y <= dimension:
            x+=1
            y+=1
            if (x, y) in positions:
                res +=1
        #Second diagonal: /
        x , y = bishop
        while x <= dimension and y >= 0:
            x+=1
            y-=1
            if (x, y) in positions:
                res +=1
    return res


if __name__ == "__main__":
    print(attacks([(0, 0),(1, 2),(2, 2),(4, 0),(1,1)]))
