import numpy as np

def _iterate(arrays, cur_depth, iterators, n):
  """
    dfs algorithm for returning the next iterator value
    Args:
      arrays: A list of 1-D arrays
      cur_depth: the depth of the dfs tree in current call
      iterators: a list of iterators
      n: number of arrays
    Returns:
      new iterator value
  """
  if cur_depth >= 0 and cur_depth < n - 1:
    iterators = _iterate(arrays, cur_depth + 1, iterators, n)
    iterators[cur_depth] += (iterators[cur_depth + 1] // len(arrays[cur_depth + 1]))
    iterators[cur_depth + 1] %= len(arrays[cur_depth + 1])
    return iterators
  elif cur_depth == n - 1:
    iterators[cur_depth] += 1
    return iterators

def _get_item_from_arrays(arrays, iterators, n):
  item = np.zeros((n), dtype=type(arrays[0][0]))
  for i, arr in enumerate(arrays):
    item[i] = arr[iterators[i]]
  return item

def smart_meshgrid(*arrays):
  """
    get the next value in the meshgrid iteration, like numpy meshgrid does.
    Args:
      arrays: The array for which to do meshgrid
  """
  N = len(arrays)
  iterators = np.zeros((N,), dtype=np.int)
  total_elements = np.prod([len(arr) for arr in arrays])  
  for _ in xrange(total_elements):
    yield _get_item_from_arrays(arrays, iterators, N)
    iterators = _iterate(arrays, 0, iterators, N)
   

