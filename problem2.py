import random


def ternary_search(arr: list[int], x: int) -> int:
    """
    Args:
        arr (list[int]): a sorted array
        x (int): an integer

    Returns:
        int: an index of x in arr if exist else -1
    """
    
    l = 0
    r = len(arr) - 1
    
    while l <= r:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        
        if arr[m1] == x:
            return m1

        if arr[m2] == x:
            return m2
        
        if arr[m1] > x:
            r = m1 - 1
        elif arr[m2] < x:
            l = m2 + 1
        else:
            l = m1 + 1
            r = m2 - 1
    
    return -1


if __name__ == "__main__":
    # Test case where x is in arr
    print("Test case where x is in arr")
    n = random.randint(1, 100)
    arr = sorted(random.randint(1, 1000) for i in range(n))
    x = random.choice(arr)
    
    print("arr =", arr)
    print("x =", x)
    
    i = ternary_search(arr, x)
    print("The result of ternary search: i =", i)
    print("The number at index i in arr is", arr[i])
    print()
    
    # Test case where x is not in arr
    print("Test case where x is not in arr")
    n = random.randint(1, 100)
    arr = sorted(random.randint(1, 1000) for i in range(n))
    not_in_arr = set(range(1, 1001)) - set(arr)
    x = random.choice(tuple(not_in_arr))
    
    print("arr =", arr)
    print("x =", x)
    
    i = ternary_search(arr, x)
    print("The result of ternary search: i =", i)  
    print("Checking by the in operator, is x in arr:", x in arr)
    