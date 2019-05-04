# Memoryless Meshgrid function

A function that does dfs to produce Meshgrid output without
worrying about memory limits.

It can be used when dealing with images or any other high dimensional data.

## Usage

See "smart_meshgrid_test.py" for more Examples.
A typical use:

```python
import numpy as np
import smart_meshgrid from smart_meshgrid

...
  X1 = np.arange(0, 100)
  X2 = np.arange(10, 210)
  # now print all elements of the meshgrid (X1, X2)
  for x in smart_meshgrid(X1, X2):
    print x
```

## Requirements

- Numpy
