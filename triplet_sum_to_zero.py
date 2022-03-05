
def triplet_sum_to_zero(arr):

    unique_triplets = []
    sorted_arr = sorted(arr)

    for i in range(len(sorted_arr)): 

        if i > 0 and sorted_arr[i] == sorted_arr[i-1]:
            continue
        search_pair(sorted_arr, i, unique_triplets)
    
    return unique_triplets

def search_pair(sorted_arr, i, unique_triplets):

    # set up pointers
    left = i + 1
    right = len(sorted_arr) - 1
    value = sorted_arr[i]

    while (left < right):
        left_val = sorted_arr[left]
        right_val = sorted_arr[right]
        sum_value = value + left_val + right_val

        if sum_value > 0:

            # then we want to decrement right val
            right -= 1
        
        if sum_value < 0:

            left += 1
        
        if sum_value == 0:
            triplet = [sorted_arr[i], sorted_arr[left], sorted_arr[right]]
            unique_triplets.append(triplet)
            left += 1
            while sorted_arr[left] == sorted_arr[left - 1] and left < right:
                left += 1
    
    return unique_triplets

print(triplet_sum_to_zero([-3, 0, 1, 2, -1, 1, -2]))
