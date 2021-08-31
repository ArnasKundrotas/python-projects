# arrays, lists, Big O
# sort given array from lowest to highest values

def find_smallest_arr_value(arr):
    smallest_arr_value = arr[0]
    smallest_arr_index = 0

    for i in range(1, len(arr)): # example [5,3,6,2,10] -> loops i -> 
        print(arr)
        #[5, 3, 6, 2, 10]
        #[5, 3, 6, 2, 10]
        #[5, 3, 6, 2, 10]
        #[5, 3, 6, 2, 10]
        #[5, 3, 6, 10]
        #[5, 3, 6, 10]
        #[5, 3, 6, 10]
        #[5, 6, 10]
        #[5, 6, 10]
        #[6, 10]
        # ---------
        #1
        #2
        #3
        #4
        if arr[i] < smallest_arr_value:
            # 3 < 5
            # 2 < 3
            # 3 < 5
            smallest_arr_value = arr[i] # 3,2
            smallest_arr_index = i # 1,3
            # 3 1
            # 2 3 
            # 3 1
    # 3
    # 1
    # 0
    # 0
    # 0 
    return smallest_arr_index # 3


def selec_sort(arr):
    new_arr = []
    for i in range(len(arr)): # example [5,3,6,2,10] -> loops i -> 0,1,2,3,4 -> 5 loops
        #0
        #1
        #2
        #3
        #4
        smallest_arr_value = find_smallest_arr_value(arr) 
        #3
        #1
        #0
        #0
        #0
        new_arr.append(arr.pop(smallest_arr_value))
        #[2]
        #[2, 3]
        #[2, 3, 5]
        #[2, 3, 5, 6]
        #[2, 3, 5, 6, 10]
    return new_arr

print (selec_sort ([5,3,6,2,10])) # print must be in ()

# example arr -> [5,3,6,2,10]

# def selec_sort
# bind new_arr[]
# len(arr) -> 5 -> i from 0 to 4 ???
# smallest_arr_value -> def find_smallest_arr_value

# def find_smallest_arr_value -> [5,3,6,2,10]
# smallest arr[0] i=0 -> 5
# if arr[1]=3 < smallest arr[0]=5 -> smallest -> arr[i]=3, i=1
# def select_sort
# arr pop -> 3 value -> arr -> [5,6,2,10]
# new_arr append -> new_arr [3]

# def find_smallest_arr_value -> [5,6,2,10]
# smallest arr[0], i=0 -> 5
# if 6<5 -> NOT -> i=1
# def select_sort
# arr pop -> 3 value -> arr -> [5,6,2,10]
# new_arr append -> new_arr [3]