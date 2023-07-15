def binarySearch(arr, l, r, x):
    while l <= r:
        # middle value is equal to lowest value + (highest - lowest) value divided by Two
        mid = l + (r - l )/2