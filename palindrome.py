# Identify palindromes within strings. For ex, 'abcdedc" has the palindrome 'cdedc'
# Approach: two-pointer 

input_str = "abcdedc"

# logic: first pointer at beginning of string, second point at last position and move inward until meet at same point 

first = 0
second = len(input_str) - 1
substr = (first, second)

while first != second:
    if input_str[first] == input_str[second]:
        first += 1 
        second -= 1
    else:
        first += 1
    
print(input_str)
