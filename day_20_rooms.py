"""
Given an array of time intervals (start, end) for classroom lectures (possibly
overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
from collections import defaultdict

def num_rooms(l):
    total_rooms = 0
    curr_used_rooms = 0
    action = defaultdict(int)
    for i in l:
        action[i[0]] +=1
        action[i[1]] -=1
    linea = sorted(action.items())
    for i in linea:
        curr_used_rooms += i[1]
        total_rooms = max(total_rooms, curr_used_rooms)
    return total_rooms

print(num_rooms([(30, 75), (0, 50), (60, 150)]))


