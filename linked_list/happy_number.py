# detecting a cycle makes me believe that this is a linked list problem 
# can also use a hash table for constant time read. If a key is already found, we know that 
# a cycle was detected 

def split_number(num):

    return [int(n) for n in str(num)]

def find_happy_number(num):

    # need a few vars
    solutions = []
    solutions.append(num)
    
    while True:

        # do the core calculation
        split_num = split_number(solutions[-1])
        sum = 0

        for digit in split_num:
            sum += digit ** 2
        
        if sum == 1:
            return True 
        print(sum)
        if sum in solutions:
            return False 
        else:
            solutions.append(sum)
        
        print(solutions)

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()