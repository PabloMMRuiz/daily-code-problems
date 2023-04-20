"""
Given a list of integers S and a target number k, write a function that returns a
subset of S that adds up to k. If such a subset cannot be made, then return null.
Integers can appear more than once in the list. You may assume all numbers in the list
are positive.
For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it
sums up to 24."""


def get_subset(goal, n_list: list):
    if not n_list:
        return None
    curr = n_list[0]
    if curr == goal:
        return [curr]
    next_iter = get_subset(goal-curr, n_list[1:])
    if next_iter is not None:
        return [curr] + next_iter
    return get_subset(goal, n_list[1:])


if __name__ == "__main__":
    print(get_subset(24,[12, 1, 61, 5, 9, 2]))
    print(get_subset(61,[12, 1, 61, 5, 9, 2]))

