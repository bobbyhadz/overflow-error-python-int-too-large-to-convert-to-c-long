# OverflowError: Python int too large to convert to C long

import numpy as np

arr = np.array([1, 5, 2147483648], dtype=np.int64)

print(arr)