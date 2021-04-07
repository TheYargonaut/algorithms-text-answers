# Ch 8 Problems

1. Subproblems:
   1.  The input space consists of arrays of $n$ distinct elements. This array has $n!$ permutations, and that each of these permutations is equally likely, for $1/n!$ probability for each permutation appearing. Since the sorting of each distinct permutation of the original elements creates a distinct permutation of the indices of the input permutation, there are an equal number of reachable leaves in the decision tree to the number of permutations on the input vector which each have equal probability to the input permutation which produces it. Therefore, there are exactly $n!$ leaves labeled $1/n!$; the remaining must be labeled 0 by the normalization property of probability mass functions.
   2.  The path from the root of T to each leaf is exactly one branch longer than the path from the roots of LT and RT. $D(LT)+D(RT)+\sum_k1=D(LT)+D(RT)+k$, QED.
   3.  This is a direct consequence of the formula shown in part `2`, where the $k$ leaves are divided among the two subtrees:\
       $\min{d(k)}$\
       $= \min{D(T_k)}$\
       $= \min_{1\leq{i}\leq{k-1}}{(D({LT}_i)+D({RT}_{k-i})+k)}$\
       $= \min_{1\leq{i}\leq{k-1}}{(\min{D({LT}_i)}+\min{D({RT}_{k-i})}+k)}$\
       $= \min_{1\leq{i}\leq{k-1}}{(d(i)+d(k-i)+k)}$\
       QED
   4.  Calculus proof is straightforward:\
   $0=\frac{d}{di}\lparen i\lg{i}+(k-i)\lg{(k-i)} \rparen$\
   $0=\lg{i}+1-\lg{(k-i)}-1$\
   $0=\lg{\frac{i}{k-i}}$\
   $1=\frac{i}{k-i}$\
   $k-i=i$\
   $k=2i$\
   $i=\frac{k}{2}$\
   Evaluating the second derivate at this point:\
   $\frac{d^2}{{di}^2}\lparen i\lg{i}+(k-i)\lg{(k-i)} \rparen$\
   $=\frac{d}{di}\lparen \lg{i}-\lg{(k-i)} \rparen$\
   $=\frac1i + \frac{1}{k-i}$\
   $=\frac4k$\
   $>0$\
   And is therefore minimized at $i=\frac{k}{2}$. Plugging this result into the formula from 3 produces the recursion $d(k)= 2d(k/2) + k$, the solution to which is $\Theta(k\lg k)$ by the master theorem, which implies $\Omega(k\lg k)$.
   5.  $D(T_A)\geq d(k=n!)=\Omega(n!\lg{n!})$ as implied by parts `1` and `5`\
   Which implies that the average path to each leaf is $\Omega(n!\lg{n!})/n!=\Omega(\frac{n!n\lg{n}}{n!})=\Omega(n\lg{n})$, QED
   6.  B reduces to at best A in expectation by the assumption of uniform inputs, which follows from the previous parts.

2. Subproblems
   1. Counting Sort
   2. The Partition procedure of QuickSort with improvement from exercise 7.2-2
   3. Insertion Sort
   4. Only algorithms which satisfy part (a) can be used as the sorting method in line 2 of `RADIX-SORT`; if criterion 1 is not satisfied, it will not be $O(bn)$; if criterion 2 is not satisfied, it will not produce a correct algorithm.
   5. Same counts as before, but place elements by swapping positions within A.

3. Subproblems
   1. Group by length and radix sort each group. Grouping done in $O(n)$ because at most $n$ integers, radix sort on all groups together done in $O(n)$, and $O(n) + O(n) = O(n)$ 
   2. Radix sort, with the first step being length and subsequent steps being on each character position down from the last position in the longest string; strings without that position may be considered as having a -infinity value for that character or just excluded.

4. Subproblems
   1. Compare every red jug to every blue jug sequentially until finding a match.
   2. Proof is same as in problem 8-1 except using a 3-tree, the hight of which is only a constant factor ($\frac{1}{\lg3}$) different in height from the binary decision tree.
   3. Basically Quicksort: Choose a red jug at random and use to partition the blue jugs. This will also find the blue jug which is equal to the chosen red jug; use it to partition the red jugs. Use this procedure recursively on each partition, grouping the upper partitions and lower partitions. The expectation and bounds differ from vanilla quicksort by a constant factor (2). The worst case is still $O(n^2)$

5. Subproblems
   1. Exactly the same as being sorted normally
   2. `{ 1, 6, 2, 7, 3, 8, 4, 9, 5, 10 }`
   3. $\displaystyle\frac1k\sum_{j=i}^{i+k-1}A[j]\leq\frac1k\sum_{j=i+1}^{i+k}A[j]$\
   $\displaystyle\sum_{j=i}^{i+k-1}A[j]\leq\sum_{j=i+1}^{i+k}A[j]$\
   $\displaystyle A[i]+\sum_{j=i+1}^{i+k-1}A[j]\leq A[i+k]+\sum_{j=i+1}^{i+k-1}A[j]$\
   $\displaystyle A[i]\leq A[i+k]$\
   The equations are equivalent, and are both necessary and sufficient to each other. QED.
   4. Partition the array almost-equally into k groups (all of size `n//k` or `n//k + 1`). Use `HEAP-SORT` to sort each group, then merge the groups without reordering the elements or groups. Note that it could be done completely in-place by modifying the `PARENT` and `LEFT`/`RIGHT` procedures for heap-sort, but I'll keep a more general version which copies out/in each group so other sort algorithms can be substituted in easily, since it doesn't affect the big-oh time.\
   This will carry out $k$ sorts each in time $O(\frac{n}{k}\lg\frac{n}{k})$ for a total time of $O(n\lg\frac{n}{k})$.
   ```
   K-SORT( A, k )
      remainder = A.length % k
      for i in 1..k
         size_b = floor( A.length / k )
         if i <= remainder
            size_b = size_b + 1
         let B be an array of length size_b
         j = i
         for x in 1..size_b
            B[ x ] = A[ j ]
            j = j + k
         HEAP-SORT( B )
         j = i
         for x in 1..size_b
            A[ j ] = B[ x ]
            j = j + k
   ```
   5. Can use a k-way version of the `MERGE` procedure from `MERGE-SORT`, which will produce the total sort in time $O(n\lg{k})$
   6. Proof by contradition; if k-sorting an n-element array in less than $\Omega(n\lg n)$ were possible for constant k, then sorting that n-element array could be done in $O(n) + o(n\lg n) < \Omega(n\lg n)$ time per the results from part (e), which contradicts the results for lower bound on comparison sorts. Therefore, k-sorting an n-element array requires at least $\Omega(n\lg n)$ time.

6. Subproblems
   1. $\binom{2n}{n}=\frac{2^{2n}}{\sqrt{\pi n}}(1+O(1/n))$
   2. Height of tree is at least\
   $\lg(\frac{2^{2n}}{\sqrt{\pi n}}(1+O(1/n)))$\
   $=2n-\frac12\lg{(\pi n)} + \lg{(1+O(1/n))}$\
   $=2n-o(n)$
   3. If not compared, and from different lists, there is no way to order correctly, therefore must be compared (rough proof by contradiction).
   4. Worst case the elements alternate between lists when sorted, requiring $2n-1$ sorts for that number of adjacencies.

7. Subproblems
   1. If $A[p]$ is a misplaced element, and $A[q]$ is also misplaced, then $A[p]\neq A[q]$, otherwise the both elements would not be misplaced; further, since $A[p]$ is defined to be the smallest misplaced element, $A[p]>A[q]$. By the definition of $B$, this implies that $B[p]=0$ and $B[q]=1$.
   2. Monotonous mapping and compare-exchange sequences are commutative; since the same results would be produced whether the compare-echange algorithm is applied before or after the move to B, this implies that algorithm X would fail to sort B.
   3. The even-numbered steps are performed without influence from the sort procedures; since the sort procedures could be any algorithm, they could be treated as though they use correct oblivious compare-exchange algorithms. Therefore, columnsort can be treated as an oblivious compare-exchange algorithm.
   4. The top and bottom $r/s$ rows are each in row-major sorted order due to previously being the first and last columns sorted in step 1, producing clean zeros at the top and clean ones at the bottom. Each column produces $r/s$ rows, at most one of which is dirty for each column; the sort in step 3 then consolidates all dirty rows in a single block in the middle, with clean rows at the top and bottom, where the number of dirty rows is dependent on the difference in contamination between the columns, which is at most $s$. Therefore, there are at most $s$ dirty rows, surrounded above by clean zeros and below by clean ones.
   5. The at most $s$ dirty rows contain a maximum of $s^2$ elements; all other are clean. The reverse permutation makes these elements contiguous in column-major order; there is thus still a maximum area of $s^2$ dirty elements.
   6. To complete the sort, it is sufficient to show that every column-major contiguous area of $s^2$ is sorted; in other words, each index must be included in at least one sort with every element within $s^2$ column-major indices of its current location. Because $r\geq2s^2$, the remaining steps accomplish this goal.
   7. If $s$ doe not divid $r$ evenly, dirty rows may be created in any row which contains elements from two columns ($s-1$ rows) as well as the single dirty row each column may create on its own ($s$ as above), for a total maximum of $2s-1$ dirty rows.\
   Following the same logic as above, step 4 will produce at most an area of $2s^2-s$ dirty elements, which will require $r\geq4s^2-2s$ to sort correctly in steps 6 through 8.
   8. Subdivide the matrix into two (or more) sorting problems where $s$ divides $r$ for each subproblem, then use a `MERGE` procedure to combine the solutions.