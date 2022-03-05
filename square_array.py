
def square_array(arr):

    # use a two pointer approach

    first = 0
    second = len(arr) - 1
    result = []

    while first > second:

        square_l = arr[first] ** 2
        square_r = arr[second] ** 2

        if square_l > square_r:
            result.insert(0, square_l)
            result.insert(0, square_r)
        else:
            result.insert(0, square_r)
            result.insert(0, square_l)

        first += 1
        second -= 1
    
    # put in middle value 
    result.insert(0, arr[first] ** 2)

    return result 

print(square_array([-2, -1, 0, 2, 3]))
print(square_array([-3, -1, 1, 2]))


