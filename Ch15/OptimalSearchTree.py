import numpy as np
import pdb

def optimalBst( p, q, n ):
   e = np.diag( q )
   w = np.diag( q )
   root = np.diag( np.arange( 0, len( p ), dtype=int ) )
   for l in range( n ):
      for i in range( n - l ):
         j = i + l + 1
         e[ i, j ] = np.inf
         w[ i, j ] = w[ i, j - 1 ] + p[ j - 1 ] + q[ j ]
         for r in range( i, j ):
            t = e[ i, r ] + e[ r + 1, j ] + w[ i, j ]
            if t < e[ i, j ]:
               e[ i, j ] = t
               root[ i, j - 1 ] = r + 1
   return e, root

def constructOptimalBstRecurse( root, i, j, parent, side ):
   if i > j:
      if i <= parent:
         print( "d%d is the left child of k%d" % ( parent, parent + 1 ) )
      else:
         print( "d%d is the right child of k%d" % ( parent + 1, parent + 1 ) )
   else:
      r = root[ i, j ] - 1
      print( "k%d is the %s child of k%d" % ( r + 1, side, parent + 1 ) )
      constructOptimalBstRecurse( root, i, r - 1, r, 'left' )
      constructOptimalBstRecurse( root, r + 1, j, r, 'right' )

def constructOptimalBst( root ):
   r = root[ 0, -1 ] - 1
   print( "k%d is the root" % ( r + 1 ) )
   constructOptimalBstRecurse( root, 0, r - 1, r, 'left' )
   constructOptimalBstRecurse( root, r + 1, len( root ) - 1, r, 'right' )

def test():
   p = [ 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14 ]
   q = [ 0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05 ]
   n = len( p )
   e, root = optimalBst( p, q, n )
   print( "Expected cost of optimal tree is", e[ 0, -1 ], '' )
   constructOptimalBst( root )

if __name__ == "__main__":
   test()