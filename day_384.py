"""
This problem was asked by WeWork.

You are given an array of integers representing coin denominations and a total amount of money. Write a function to compute the fewest number of coins needed to make up that amount. If it is not possible to make that amount, return null.

For example, given an array of [1, 5, 10] and an amount 56, return 7 since we can use 5 dimes, 1 nickel, and 1 penny.

Given an array of [5, 8] and an amount 15, return 3 since we can use 5 5-cent coins."""


def min_coin_adding(ls:list, n:int):
    ls.sort()
    if n == 0:
        return 0
    if n < 0:
        return None
    return min_coin_adding_res(ls, n, len(ls)-1, 0)

def min_coin_adding_res(ls, n, curr_index, res):
    if curr_index<0:
        return None
    if n-ls[curr_index]<0:
        if curr_index >0:
            return min_coin_adding_res(ls, n, curr_index-1, res)
        else:
            return None
    if n-ls[curr_index] == 0:
        return res+1
    elif min_coin_adding_res(ls, n-ls[curr_index], curr_index, res+1):
        return min_coin_adding_res(ls, n-ls[curr_index], curr_index, res+1)
    elif min_coin_adding_res(ls, n, curr_index-1, res):
        return min_coin_adding_res(ls, n, curr_index-1, res)


if __name__ == "__main__":
    print(min_coin_adding([1,5,10], 56))
