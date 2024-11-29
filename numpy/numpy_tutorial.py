# 3 benefits of numpy over array 1) LESS MEMORY 2) FASTER 3) EASIER TO USE

import numpy as np
import time
import sys

l = range(10000)
print(sys.getsizeof(5) * len(l))

array = np.arange(1000)
print(array.size * array.itemsize)

SIZE = 20000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)
# Python List
start = time.time()
result = [(x + y) for x, y in zip(l1, l2)]
print((time.time() - start) * 1000)
# numpy array
start = time.time()
result = a1 + a2
print((time.time() - start) * 1000)