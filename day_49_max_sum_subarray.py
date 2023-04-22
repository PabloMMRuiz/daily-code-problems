"""Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
Do this in O(N) time."""

def max_contiguous_sum(arr:list)->int:
    #We start at first positive number:
    curr_max = 0
    curr_count = 0
    left_side = 0
    right_side = 0
    for index, i in enumerate(arr):
        if i>0:
            left_side = index
            break
    # Pass 1:
    for index_mod, elem in enumerate(arr[left_side:]):
        curr_count += elem
        if curr_count>curr_max:
            right_side = index_mod+left_side
            curr_max = curr_count
    #Pass 2:
    curr_count = curr_max
    for elem in arr[:right_side+1]:
        curr_count -= elem
        if curr_count >curr_max:
            curr_max = curr_count
    return curr_max

print(max_contiguous_sum([34, -50, 42, 14, -5, 86]))
        
