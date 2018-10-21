import numpy as np
import smart_meshgrid as s_m

if __name__ == "__main__":
  X1 = np.arange(0,1000)
  X2 = np.arange(10,210)
  X3 = np.arange(30,4100)

  for x in s_m.smart_meshgrid(X1, X2, X3):
    print x