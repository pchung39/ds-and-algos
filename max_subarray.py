
in_array = [2, 1, 5, 1, 3, 2]
k = 3 
# return: array with max sum subarray

# strategy: using a sliding window find the largest sum 
max_sum, window_sum = 0.0, 0.0
window_pos = 0

for i in range(len(in_array) - k + 1):

    # calculate window sum
    window_sum = in_array[i] + in_array[i + 1] + in_array[i + 2]

    if window_sum > max_sum:
        max_sum = window_sum 
        window_pos = i 

print(max_sum)
print([in_array[window_pos], in_array[window_pos + 1], in_array[window_pos + 2]])