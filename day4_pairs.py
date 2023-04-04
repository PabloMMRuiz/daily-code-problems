"""cons(a, b) constructs a pair, and car(pair) and cdr(pair)
returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4."""
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pepino):
    return(pepino(lambda x,_:x))

def cdr(pepino):
    return(pepino(lambda _,x:x))


def abdakbd(a):
    def nn(n):
        return n(a)
    return nn

if __name__ == "__main__":
    test = cons("A", "B")
    print(car(test))
    print(cdr(test))
    ola = abdakbd(2)
    print(ola(lambda a:-5+a+2))