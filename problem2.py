# ones(λ) = 0 where λ is the empty string
# ones(1x) = 1 + ones(x) where x is a string
# ones(0x) = ones(x) where x is a string

def ones(s):
    if not s:
        return 0
    
    if s[0] == '1':
        return 1 + ones(s[1:])
    else:
        return ones(s[1:])


if __name__ == "__main__":
    s = input("Enter the binary string: ")
    print(f"The number of 1-bit in {s} is {ones(s)}")