# reverse(λ) = λ where λ is the empty string
# reverse(cx) = reverse(x)c where c is a character in the alphabet and x is a string

def reverse(s):
    if not s:
        return s
    
    return reverse(s[1:]) + s[0]

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"The reverse of {s} is {reverse(s)}")
    