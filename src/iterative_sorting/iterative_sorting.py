# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapping = True
    while swapping:
        swapping = False  # If no swap, loop will stop after swappig become false
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:  # compare if current element is greater than its neighbor in right
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if yes
                swapping =  True    # Swap Happened
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr