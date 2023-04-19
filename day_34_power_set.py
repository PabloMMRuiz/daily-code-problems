"""The power set of a set is the set of all its subsets. 
Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}"""

def power_set(initial_set: set)->set:
    if len(initial_set) == 0:
        return {initial_set}
    res = [[]]
    for e in initial_set:
        temp = []
        for s in res:
            s = [elem for elem in s]
            s.append(e)
            temp.append(s)
        res.extend(temp)
    return sorted(res, key=lambda a:len(a)) #Innecesario, por mejora visual
seto = {1,2,3,4,5}
print(power_set(seto))