from heapq import * 


def find_closest_elements(arr, K, X):


    # can use a hash map to store relative distance from X

    # use k to iterate through the hashmap and store in hashmap

    hash_map = {}

    for num in arr:

        # calculate distance  from X 
        distance = abs(X - num)
        hash_map[num] = distance
    
    min_heap = []

    for k,v in hash_map.items():
        heappush(min_heap, (v, k))

    # shave off excess entries in the heap
    # while len(min_heap) > K:
    #     heappop(min_heap)
    

    # iterate through remaining items and print them 
    result = []

    for x in range(K):
        curr = heappop(min_heap)
        result.append(curr[1])

    return sorted(result)
    
    


def main():
    print("'K' closest numbers to 'X' are: " + \
            str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " + \
            str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " + \
            str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()