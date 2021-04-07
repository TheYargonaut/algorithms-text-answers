# Ch 6 Problems

1. Subproblems
   1. No. Counter-example:\
      $\langle 1, 2,3, 4 \rangle$\
      BUILD-MAX-HEAP\
      $\langle 1, 2,3, 4 \rangle$\
      $\langle 1, 4,3, 2 \rangle$\
      $\langle 4, 1,3, 2 \rangle$\
      $\langle 4, 2,3, 1 \rangle$\
      BUILD-MAX-HEAP'\
      $\langle 1, 2,3, 4 \rangle$\
      $\langle 2, 1,3, 4 \rangle$\
      $\langle 3, 1,2, 4 \rangle$\
      $\langle 3, 4,2, 1 \rangle$\
      $\langle 4, 3,2, 1 \rangle$\
      The elements 2 and 3 are interchanged.   
   2. makes $\Theta(n)$ calls to a $\Theta(\lg{n})$ procedure, so is in the worst case $\Theta(n\lg{n})$

2. Subproblems
   1. Same as a binary heap, but with the following adjustment to `PARENT`
      ```
      PARENT-D( i, d )
         return floor( i / d )
      ```
      and instead of LEFT and RIGHT, the following CHILD proceedure for retrieving the injdex of the k-th child
      ```
      CHILD( i, d, k )
         if k > d
            error "child queried greater than number of children"
         return d*i + k - 1
      ```
   2. $h=\lfloor\log_dn\rfloor$
   3. Using the above implementation of `CHILD` and assuming `A` has a property `A.d` which encodes its d-aryness
      ```
      D-MAX-HEAPIFY-ITERATIVE( A, i )
         subroot = i
         while subroot > floor( A.heap-size / A.d )
            largest = subroot
            start = CHILD( subroot, A.d, 1 )
            stop = CHILD( subroot, A.d, A.d )
            if stop > A.heap-size
               stop = A.heap-size
            for l = start to stop
               if A[ l ] > A[ largest ]
                  largest = l
            if largest == subroot
               return
            exchange A[ subroot ] with A[ largest ]
            subroot = largest

      D-HEAP-EXTRACT-MAX( A )
         if A.heap-size < 1
            error "heap underflow"
         max = A[ 1 ]
         A[ 1 ] = A[ A.heap-size ]
         A.heap-size = A.heap-size - 1
         D-MAX-HEAPIFY-ITERATIVE( A, 1 )
         return max
      ```
      Runs in $O(d+\log_dn)$ time.
   4. Using the above implementation of `PARENT`
      ```
      D-HEAP-INCREASE-KEY( A, i, key )
      if key < A[ i ]
         error "new key less than current key"
      parent = PARENT( i, A.d )
      while i > 1 and A[ parent ] < key
         A[ i ] = A[ parent ) ]
         i = parent
         parent = PARENT( i, A.d )
      A[ i ] = key

      MAX-HEAP-INSERT( A, key )
         A.heap-size = A.heap-size + 1
         A[ heap-size ] = -INF
         D-HEAP-DECREASE-KEY( A, heap-size, key )
      ```
      Runs in $O(\log_dn)$ time.
   5. See above implementation of `D-HEAP-INCREASE-KEY`\
      Runs in $O(\log_dn)$ time.

3. Subproblems
   1. ```
       2    3   4   5
       8    9  12  14
      16  inf inf inf
      inf inf inf inf
      ```
   2. No elements less than $\infty$ if $Y[1,1]=\infty$, so $Y$ is empty\
      No elements are $\infty$ if $Y[m,n]<\infty$, so $Y$ is full
   3. tedious, elide
   4. tedious, elide
   5. tedious, elide
   6. tedious, elide