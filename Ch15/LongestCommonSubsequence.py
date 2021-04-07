import numpy as np

MATCH = 0
UP = 1
LEFT = 2

def lcsLength( x, y ):
   m = len( x )
   n = len( y )
   b = np.zeros( ( m, n ), int )
   c = np.zeros( ( m + 1, n + 1 ), int )
   for i in range( m ):
      for j in range( n ):
         if x[ i ] == y[ j ]:
            c[ i + 1, j + 1 ] = c[ i, j ] + 1
            b[ i, j ] = MATCH
         elif c[ i, j + 1] >= c[ i + 1, j ]:
            c[ i + 1, j + 1 ] = c[ i, j + 1 ]
            b[ i, j ] = UP
         else:
            c[ i + 1, j + 1 ] = c[ i + 1, j ]
            b[ i, j ] = LEFT
   return c, b

def formatLcs( b, x, y ):
   i = len( x ) - 1
   j = len( y ) - 1
   s = ""
   while i >= 0 and j >= 0:
      if b[ i, j ] == MATCH:
         s = str( x[ i ] ) + s
         i -= 1
         j -= 1
      elif b[ i, j ] == UP:
         i -= 1
      else:
         j -= 1
         
   return s

def test():
   x = [ 1, 0, 0, 1, 0, 1, 0, 1 ]
   y = [ 0, 1, 0, 1, 1, 0, 1, 1, 0 ]
   _, b = lcsLength( x, y )
   print( formatLcs( b, x, y ) )

if __name__ == "__main__":
   test()