# iterative Binary Search Algorithm

def binarySearch(arr, l, r, x):
    while l <= r:
        # middle value is equal to lowest value + (highest - lowest) value divided by Two
        mid = l + (r - l )//2

        # check if x is present at mid
        if arr[mid] == x:
            return mid
        # if x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
        # if x is smaller, ignore right half
        else:
            r = mid - 1

    # if we reach here, then the element was not present
    return -1

# Driver code
if __name__ == '__main__':
    arr= [2,3,4,10,40]
    x = 2

    # fucntion call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

