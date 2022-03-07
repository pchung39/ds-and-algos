
def binary_search(arr, target):

    start = 0
    end = len(arr) - 1 

    while start <= end:

        middle = mid = start + (end - start) // 2 

        if arr[middle] == target:
            return middle
        
        if target > arr[middle]:
            start = middle
        else:
            end = middle 
        
        # we need to adjust start and end 
        # if the target was greater than middle 



def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()