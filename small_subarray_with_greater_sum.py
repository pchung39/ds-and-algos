# Given an array of pos. numbers and a positive number 'S', find the length
# of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0
# if no such subarray exists.

# sliding window is not fixed. It shrinks and grows given the window sum 
import math

def smallest_subarray_sum(s, arr):
    min_length = float('inf')
    window_sum = 0
    window_start = 0

    first = 0

    for window_end in range(len(arr) - 1):

        window_sum += arr[window_end]

        # determine if window sum is greater than or equal "s"
        while window_sum >= s:
            window_length = window_end - window_start + 1
            min_length = min(min_length, window_length)
            window_sum -= arr[window_start]
            window_start += 1

    exact_numbers = [arr[i] for i in range(window_start - 1, window_end)]

    return min_length, exact_numbers


input_array = [2, 1, 5, 2, 3, 2]
s = 7
print(smallest_subarray_sum(s, input_array))