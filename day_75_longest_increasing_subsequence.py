"""
Given an array of numbers,
find the length of the longest increasing subsequence in the array.
The subsequence does not necessarily have to be contiguous.
For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15."""


def lis(a_list:list, n:int):
    global maximum
    if n ==1:
        return 1
    maxNow = 1
    for point in range(1,n):
        res = lis(a_list, point) #We calculate the possible longest lis ending before the current position
        if a_list[point-1] < a_list[n-1] and res+1 > maxNow: #If one of those sequences can be continued with current number then the max there is updated
            maxNow = res+1
        #We keep the maximum variable outside because the longest sequence might not end in the last number, which is the result the function would actually return
    if maxNow > maximum:
        maximum = maxNow
        
    return maxNow #We need to return this value for the function to work recursively

if __name__ == "__main__":
    global maximum
    maximum = 0
    tester = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    lis(tester, len(tester))
    print(maximum)

#TODO: Easy to make this better with memoization!!