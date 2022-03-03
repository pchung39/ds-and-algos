
def k_distinct_chars(k, arr):

    window_start = 0
    max_length = 0
    substring = []

    # TODO: take approach of sliding window
    # my approach did not use a hash map, but can probably do so. 

    for window_end in range(len(arr)):

        # add window_end to list
        substring.append(arr[window_end])
        # determine if over "k"
        if len(set(substring)) > k:
            
            max_length = max(max_length, window_end - window_start)
            # empty substring
            substring = []

            window_start = window_end
        
    return max_length

print(k_distinct_chars(3, "cbbebi"))

