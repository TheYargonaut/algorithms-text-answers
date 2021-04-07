# Ch 12 Problems

1. Subproblems
   1. $O(n^2)$
   2. $O(n\lg n)$
   3. $O(n)$
   4. Worst case $O(n^2)$, but like previous proofs on randomized quicksort average case is $O(n\lg n)$

2. Store in radix tree, $\Theta(n)$ in total length, then print in-order, which is $o(n)$.

3. Subproblems
   1. By definition of average, it has to be.
   2. Pre-existing path length, plus one for the additional depth of each node other than the root.
   3. Definition of expectation applied to previous results.
   4. Linearity and symmetry of summation
   5. Concluded
   6. Given the order of elements, isn't that just 'how quicksort works' in general?

4. Elide