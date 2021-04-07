# Ch 2 Problems

1. Subproblems
   1. $n/k * \Theta(k^2)$ = $\Theta(nk)$
   2. Coarse leaves to root there are $\lg(n/k)$ layers each with width $n$. Merge the sublists as usual for merge sort.
   3. $k=log(n)$
   4. By profiling to find the best $k$ incorporating all constants

2. Subproblems
   1. Nothing? Seems like those conditions are necessary and sufficient.
   2. At the start of each iteration of the inner loop, $A[ j ]$ is the minimum-valued element in $A[ j .. A.length ]$\
      **Initialization**: Trivially true at initialization, as $A[ j .. A.length ]$ contains only $A[j]$.\
      **Maintenance**: The swap step ensures the minimum value at for $A[ j-1 .. A.length ]$ is placed at $A[j-1]$, since it can only be the current minimum within $A[ j .. A.length ]$ or the current element at $A[ j - 1 ]$. \
      **Termination**: At termination, the minimum value of $A[ i .. A.length ]$ is guaranteed to be at $A[ i ]$
   3. At the start of each iteration of the outer loop, $A[ 1 .. i-1 ]$ contains either no elements or the lowest-valued $i-1$ elements in non-decreasing sorted order.
      **Initialization**: Trivially true at initialization, as $A[ 1 .. i - 1 ]$ is empty.\
      **Maintenance**: The termination property of the inner loop guarantees that $A[ i ]$ holds the minimum value of $A[ i .. A.length ] at the end of each iteration, maintaining the invariant. \
      **Termination**: At termination, the elements of $A$ are guaranteed to be in non-decreasing sorted order.
   4. $\Theta(n^2)$

3. Subproblems
   1. $\Theta(n)$
   2. Since exponentiation is not a primitive instruction:\
      ```
      NAIVE_POW( x, k )
         \\ Theta( k ) time
         if k == 0
            return 1
         if x == 0 or x == 1
            return x
         r = x
         for i = 1 to k-1:
            r = r * x
         return r
      
      FAST_POW( x, k )
         \\ Theta( lg k ) time with properties of exponents
         if k == 0
            return 1
         if x == 0 or x == 1
            return x
         square = x
         product = 1
         while k > 0
            if mod( k, 2 ) == 1:
               product = product * square
            square = square * square
            k = floor( k / 2 )
         return product
      
      POLYNOMIAL( x, A )
         y = 0
         for i = 0 to A.length
            y = y + NAIVE_POW( x, i ) * A[i]
         return y
      ```
      The most naive form of the polynomial runs in $\Theta(n^2)$ time; with fast exponentiation, this only gets to $\Theta(n\lg{n})$, both of which are slower than Horner's rule computation.

   3. **Initialization**: Trivially true, 0 = 0\
      **Maintenance**: Each iteration explicitly sets up the invariant for the next\
      **Termination**: At termination, where i=0, the invariant is equal to the condition to be shown

4. Subproblems
   1. (1,5), (2,5), (3,5), (4, 5), (3, 4)
   2. The one sorted in nonincreasing order, which has $n-1 + n-2 + ... n-n = n^2 - (n+1)*n/2 = (n^2-n)/2$ inversions
   3. The maximum number of inversions corresponds to the worst-case run time for insertion sort, both because it has the same condition and each inversion is a step that the insertion sort has to reverse.
   4. idea: count times drawn from 'higher' array during merge, incrementing by the number of elements remaining in the 'lower' array. Should work, eliding the full algorithm.

