import timeit
from count import catalanPrefix


n = int(input("Enter n: "))

start = timeit.default_timer()

pair = n // 2
res = [''] * (2 * pair)
count = 0

def gen(i, openCount, closeCount):
    global count
    
    if openCount == closeCount:
        print(*res, sep='')
        count += 1
    
    if i >= 2 * pair or closeCount > openCount or openCount > closeCount + 2 * pair - i:
        return
    
    res[i] = '('
    gen(i + 1, openCount + 1, closeCount)
    res[i] = ')'
    gen(i + 1, openCount, closeCount + 1)
    res[i] = ''

gen(0, 0, 0)

end = timeit.default_timer()

print(f"There are total {count} strings")

print(f"Checking by calculate Catalan numbers, there are {catalanPrefix[pair]} strings")

print(f"Runtime: {end - start}s")
    
    