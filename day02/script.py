import pandas as pd

my_series = pd.Series([5, 6, 8, 9, 10, 12])

my_series2 = pd.Series( [ 10, 11, 13, 17, 21, 22 ], index = [ 'a', 'b', 'c', 'd', 'e', 'f' ] )

print(my_series)
print('')

print(my_series.index)
print('')

print(my_series.values)
print('')

print( my_series2['c'] )
print('')

print( my_series2[ ['a', 'c', 'f'] ] )

my_series2[ ['a', 'c', 'f'] ] = 0

print( my_series2[ ['a', 'c', 'f'] ] )
print('')

print( my_series2[ my_series2 > 0 ] )
print('')