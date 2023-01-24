from itertools import groupby # Itertools.groupby(). This method calculates the keys for each element present in iterable. It returns key and iterable of grouped items.
for key, group in groupby(input()):
   print('({}, {})'.format(len(list(group)), key), end=" ")



