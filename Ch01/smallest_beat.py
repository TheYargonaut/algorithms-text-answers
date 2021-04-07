import numpy as np

def find_beat( asymptotic, smallset, maxn=int( 1e+3 ) ):
   '''find the lowest n for which the asymptotic perfomance function
      beats the smallset performance'''

   low = 1
   high = maxn

   while ( high - low > 1 ):
      n = ( high + low ) // 2
      if asymptotic( n ) < smallset( n ):
         high = n
      else:
         low = n

   print( "Result:", n )

if __name__ == "__main__":
   # exercise 1.2-2
   find_beat( lambda n : 64 * n * np.log( n ),
              lambda n : 8 * n ** 2,
              100 )
   
   # exercise 1.2-3
   find_beat( lambda n : 100 * n **2,
              lambda n : 2 ** n,
              100 )
