import itertools
import operator

catalan = [0] * 101

catalan[0] = catalan[1] = 1
for i in range(2, 101):
    for j in range(i):
        catalan[i] += catalan[j] * catalan[i - j - 1]

catalanPrefix = list(itertools.accumulate(catalan, operator.add))
