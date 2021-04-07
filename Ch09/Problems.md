# Ch 9 Problems

1. Subproblems. Choosing `HEAP-SORT` as fast comparison sort, but could be any equivalently-fast comparison sorting algorithm.
   1. `HEAP-SORT`, $\Theta(n\lg{n})$
   2. `BUILD-MAX-HEAP` and `EXTRACT-MAX`, $\Theta( n + i\lg{n} )$
   3. `SELECT` then `HEAP-SORT`, $\Theta( n + i\lg{i} )$

2. Subproblems
   1. $\sum_{x_i>x_k}w_i=\sum_{x_i>x_k}\frac{1}{n}=\frac{|x_i>x_k|}{n}<\frac12$\
      likewise\
      $\sum_{x_i<x_k}w_i=\sum_{x_i<x_k}\frac{1}{n}=\frac{|x_i<x_k|}{n}\geq\frac12$
      Both occur if and only if the cardinality of the set of $x_i>x_k$ is one less than the cardinality of of the set of $x_i<x_k$, that is, when $x_k$ is the median. QED.
   2. Sort with a fast sorting algorithm (like `HEAP-SORT`) in $O(n\lg n)$ time, then create a new array of the same size `C` for the cumulative weight, where $c_k=\sum_{x_i<x_k}w_i$ in $O(n)$ time, and finally use `BINARY-SEARCH` to find the result in $O(n)$ time, for a total of $O(n\lg n)+O(n)+O(n)=O(n\lg n)$ time.
   3. Use `SELECT` to find the median element and partition about it. Sum the elements less than the median. If this sum is greater than 1/2, recurse on the lower partition. If the sum is less than 1/2, recurse on the upper partition, using the sum of the lower partition to avoid summing those elements again.\
   Since the algorithm needs to find the first index where the cumulative weight is less than 1/2 but where the next index has a cumulative weight greater than 1/2, it will always recurse the worst case. This case is O(n), because all steps are $O(n)$ and are called with at most $2n$ elements.
   4. Tedious, but same as exercise 9.3-8
   5. Solve as two 1-dimensional problems: $x$ only and $y$ only (projected onto the axes, respectively), since they are independant.

3. Tedious, see full solution [here](https://ita.skanev.com/09/problems/03.html).

4. Tedious, see full solution [here](https://ita.skanev.com/09/problems/04.html).