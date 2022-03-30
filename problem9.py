import timeit
from count import catalanPrefix


def balanceString(n: int)->None:
    pair = n // 2  # The number of maximum pairs
    res = [''] * (2 * pair) # Store temporary answer
    count = 0 # The number of answers

    # helper function
    # i: current index
    # openCount: number of current open brackets
    # closeCount: number of current close brackets
    def gen(i, openCount, closeCount):
        nonlocal count
        
        # found an answer, print it
        if openCount == closeCount:
            print("".join(res))
            count += 1
        
        # cannot continue
        if i >= 2 * pair or closeCount > openCount or openCount > closeCount + 2 * pair - i:
            return
        
        # try an open bracket
        res[i] = '('
        gen(i + 1, openCount + 1, closeCount)
        # try a close bracket
        res[i] = ')'
        gen(i + 1, openCount, closeCount + 1)
        # reset
        res[i] = ''

    gen(0, 0, 0)
    print(f"There are total {count} strings")

    print(f"Checking by calculate Catalan numbers, there are {catalanPrefix[pair]} strings")
    
if __name__ == "__main__":
    n = int(input("Enter n: "))

    start = timeit.default_timer()
    balanceString(n)
    end = timeit.default_timer()

    print(f"Runtime: {end - start}s")
        

        