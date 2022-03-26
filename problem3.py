# m(c) = c where x is a character in the alphabet
# m(cx) = min(c, m(x)) where c is a character in the alphabet and x is a string

def m(s):
    if len(s) == 1:
        return s[0]
    
    return min(s[0], m(s[1:]))

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"The minimum character in {s} is {m(s)}")