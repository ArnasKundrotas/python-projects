# this bin search example uses sorted arrays
# binary search O(log n)
# simple search O(n)

import math

def binary_search(list, item):
    
    low = 0
    high = len(list) - 1 # len(list) print number of elements (4). We need last array index 3 -> -1

    while low <= high:
        mid = int((low + high)/2) 
        # if not even number rounded down by Python NOT!!!
        # must do casting int(), (int+int)/2 returns float and error in Python v3

        guess = list[mid] # guessing that item is in the middle

        if guess == item: # guessed the number
            return mid #return array index
        if guess > item: # item is lower then the guess
            high = mid - 1 
            # since high was used and item is lower anyway
            # decrease high index of array by 1 and divide by 2 in the first line of while loop
        else:
            low = mid + 1 
            # since low was used and item is higher anyway
            # increase the low index of array by 1 and divide by 2 in the first line of while loop
    return None # if no right gueeses return None

my_list = [1,3,5,7,9] # input

print (binary_search(my_list, 3)) # return array index number or None
print (binary_search(my_list, -1)) # return array index number or None

# returns :
# 1 <- array index
# None
