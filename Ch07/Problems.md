# Ch 7 Problems

1. Subproblems
   1. $\langle ()13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11[] \rangle$\
      $\langle 13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, [11] \rangle$\
      $\langle (13), 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, [11] \rangle$\
      $\langle (11), 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, [13] \rangle$\
      $\langle (11), 19, 9, 5, 12, 8, 7, 4, 21, 2, [6], 13 \rangle$\
      $\langle 11, (19), 9, 5, 12, 8, 7, 4, 21, 2, [6], 13 \rangle$\
      $\langle 11, (6), 9, 5, 12, 8, 7, 4, 21, 2, [19], 13 \rangle$\
      $\langle 11, (6), 9, 5, 12, 8, 7, 4, 21, [2], 19, 13 \rangle$\
      $\langle 11, 6, 9, 5, 12, 8, 7, 4, (21), [2], 19, 13 \rangle$\
      $\langle 11, 6, 9, 5, 12, 8, 7, 4, (2), [21], 19, 13 \rangle$\
      $\langle 11, 6, 9, 5, 12, 8, 7, 4, [2], (21), 19, 13 \rangle$\
      return 9
   2. Initialized outside but move in to valid values before any accesses, plus terminates as soon as crossover (so they don't go out the other side).
   3. `j` and `i` cross over somewhere in the middle; `j` is always less than `r` because of its initialization, and always at least `p` because it will stop at `A[j]=x=A[p]` OR `i` will have crossed at least one element which will hit the `j` condition to stop; in both cases it returns immediately.
   4. That's the termination statement of the loop variant, i.e. every element of `A[p..i]` is less than or equal to every element of `A[j+1..r]` or those arrays are empty. Trivial at initialization, maintained by the swaps, and termination gives the thing that is to be proved as its conclusion.
   5. Tedious, elide

2. Subproblems
   1. Still $\Theta(n^2)$ without the improvement from exercise 7.2-2
   2. ```
      PARTITION'( A, p, r )
         x = A[ r ]
         q = p // track lesser area
         t = r // track greater area
         i = r - 1
         while i > q
            if A[ i ] > x
               exchange A[ i ] with A[ t ]
               t = t - 1
               i = i - 1
            elif A[ i ] == x
               i = i - 1
            else \\ A[ i ] < x
               exchange A[ i ] with A[ q ]
               q = q + 1
         return q, t
      ```
   3. ```
      RANDOMIZED-PARTITION'( A, p, r )
         i = RANDOM( p, r )
         exchange A[ r ] with A[ i ]
         return PARTITION'( A, p, r )

      QUICKSORT'( A, p, r )
         if p < r
            q, t = RANDOMIZED-PARTITION'( A, p, r )
            QUICKSORT'( A, p, q - 1 )
            QUICKSORT'( A, t + 1, r )
      ```
   4. Any elements equal to the chosen pivot are 'discarded', that is excluded from lower levels of the tree, just like the chosen pivot itself. This removes the need for the distinctiveness assumption.

3. tedious, elide

4. Subproblems
   1. Same calls as normal `QUICKSORT` (in the same order as well), just different stack patterns.
   2. If the pivot is always chosen such that $r-q = 1$, the stack depth will be $\Theta(n)$
   3. Just follow the largest partition and call down with the smaller one.
      ```
      TAIL-RECURSIVE-QUICKSORT'( A, p, r )
         while p < r
            q = PARTITION( A, p, r )
            if r - q > q - p
               TAIL-RECURSIVE-QUICKSORT`( A, p, q - 1 )
               p = q + 1
            else
               TAIL-RECURSIVE-QUICKSORT`( A, q + 1, r )
               r = q - 1
      ```

5. tedious, elide

6. Subproblems
   1. Basically treat all intervals which overlap $\frac{a_i+b_i}{2}$ for the pivot as being equal to the pivot and use QUICKSORT' from part 2. Otherwise, greater or lesser based on $a_i$ of candidate compared with $\frac{a_i+b_i}{2}$ of pivot.

   2. The more which are discarded as equal, the closer to $\Theta(n)$ it gets by discarding more values during the (modified) $\Theta(n)$ `RANDOMIZED-PARTITION'` call. Otherwise, it reduces to the original `QUICKSORT` problem.