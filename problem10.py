import random
import math


def gcd(a, b):
    if a > b:
        return gcd(b, a)
    
    if a == 0:
        return b
    
    if a % 2 == 0 and b % 2 == 0:
        return 2 * gcd(a // 2 , b // 2)

    if a % 2 == 0:
        return gcd(a // 2, b)
    
    return gcd(a, b - a)


if __name__ == "__main__":
    print("Generate Random Test Case")
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)

    print(f"gcd({a}, {b}) is {gcd(a, b)}")
    print(f"Checking by math.gcd(), gcd({a}, {b}) is {math.gcd(a, b)}")
