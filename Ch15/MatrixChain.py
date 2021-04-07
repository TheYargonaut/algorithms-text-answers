import numpy as np

def matrixChainOrder( p ):
   n = len( p ) - 1
   m = np.full( ( n, n ), np.inf )
   s = np.zeros( ( n - 1, n - 1 ), dtype=int )
   for i in range( 0, n ):
      m[ i, i ] = 0
   for l in range( 2, n ):
      for i in range( 0, n - l + 1 ):
         j = i + l - 1
         for k in range( i, j ):
            q = m[ i, k ] + m[ k + 1, j - 1 ] + p[ i ] * p[ k ] * p[ j ]
            if q < m[ i, j - 1 ]:
               m[ i, j - 1 ] = q
               s[ i, j - 1 ] = k
   return m, s

def formatOptimalParens( s, i, j ):
   print( i, j )
   if i == j:
      return "A%d" % i
   return "( %s%s )" % ( 
      formatOptimalParens( s, i, s[ i, j ] ),
      formatOptimalParens( s, s[ i, j ] + 1, j ) )

def test():
   _, s = matrixChainOrder( [ 5, 10, 3, 12, 5, 50, 6 ] )
   print( formatOptimalParens( s, 0, len( s ) - 1 ) )

if __name__ == "__main__":
   test()