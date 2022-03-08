import random


def binary_insertion_sort(arr: list[int]) -> None:
    """
    Sort arr
    Args:
        arr (list[int])
    """
    
    for i in range(1, len(arr)):
        # Find the index to insert arr[i]
        x = arr[i]
        l, r = 0, i
        
        while l < r:
            m = l + r >> 1
            
            if arr[m] >= x:
                r = m
            else:
                l = m + 1
        
        index = l

        #Insert arr[i] to the found index
        for j in range(i, index, -1):
            arr[j] = arr[j - 1]
        arr[index] = x


if __name__ == "__main__":
    n = random.randint(1, 100)
    arr = [random.randint(1, 1000) for i in range(n)]
    arr_copy = arr.copy()
    
    print("arr before sorting:", arr, '\n')
    binary_insertion_sort(arr)
    print("arr if sorted by binary insertion sort:", arr, '\n')
    arr_copy.sort()
    print("arr if sorted by built-in function:", arr_copy, '\n')
    print("Are those two equal?:", arr == arr_copy)
    
            
        
                