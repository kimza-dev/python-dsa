def binarySearch(arr, l,r,x):
    # check base case
    if r >= l:
        mid = l + (r - l ) // 2

        # if element is present in the midele itself
        if arr[mid] == x:
            return mid
        
        # if element i smaller than mid, then it can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        
        # else the element can only be present in the righ subarray
        else:
            return binarySearch(arr, mid +1 , r, x)
    
    # element is not present in the array
    else:
        return -1

# driver code
if __name__ == '__main__':
    arr = [2,3,4,10,40]
    print("Length of arary: ",arr.__len__())
    x = 10

    # function call
    result = binarySearch(arr, 0, len(arr)-1, x)

    if result != -1:
        print("Element is present at index: ", result)
    else:
        print("Element is not present in the array")
        
    # 