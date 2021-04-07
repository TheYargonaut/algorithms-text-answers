# Ch 16 Problems

1. Subproblems
   1. Grab the largest denomination coin of less value than the difference between the change so far and the target.\
   Since no coin is more than half the value of any other coin, it always takes at least 2 coins of a lower denomination to replace 1 of a higher denomination. Therefore, any step which takes a smaller denomination can be improved by taking the larger.
   2. Any coin with denomination $c^i$ requires at least $c$ coins of denomination $c^{i-1}$ to replace, and can be replaced vice versa for instant improvement. Therefore, the greedy algorithm is always optimal.
   3. 1, 4, 5. Change of total value 8 would take 4 coins in the greedy solution (5, 1, 1, 1), but only 2 coins in the optimal solution (4, 4)
   4. Dynamic programming solution with memoization. Make 1, 2, 3, etc., computing the next value from any optimal combination of two previous values or a new denomination.

2. Subproblems
   1. Sort tasks in order of increasing $p_i$. Run in order. Since each running time is included in the completion time of every subsequent task, earlier tasks have larger coeficients in the average. Any change to this schedule by, say, a swap would necessarily increase the average completion time.
   2. Now just run the available task with the least remaining time at any given slot. $O(i\sum{p_i})$. Minimizes the multiplier still.

3. Subproblems
   1. The columns corresponding to a set of edges incident on a similar vertex can be added together modulo 2 to create a column equivalent to that of an edge between the two dissimilar vertices on which they are incident. Therefore, if a cycle exists, the sets of columns corresponding to the edges of the cycle on each path between two chosen vertices can be added together modulo two in order to create identical columns. Likewise, such cannot be accomplished without a cycle, as each pair of vertices then requires the same set of edges to set or unset. Therefore, the graph is acyclic iff $M$ has linearly independant columns.
   2. Sort the edges by weight and prepare a variable $Z$ (of column size) set to all zeros. Starting with the highest-weight edge $E_i$, add the column for that edge (from the incidence matrix) to $Z$. If $Z$ is nonzero in any field, choose $E_i$; otherwise, discard $E_i$ and add it's column to $Z$ again. The chosen edges are the maximum total weighted subset.
   3. Consider the case where there are two vertices, $V_0$ and $V_1$. Let there be three directed edges, two of which are $V_0\rightarrow V_1$ and one of which is $V_1\rightarrow V_0$. Now let there be two sets of edges which beling to $I$: set $A$ which contains only the latter edge, and set $B$ which contains both the previous. $|B|>|A|$, but adding either member of $B$ to $A$ creates a set $A'$ which does not belong to $I$. Therefore, this case violates the exchange property of matroids.
   4. A cycle requires entering and leaving each vertex in the cycle exactly once, and so the columns corresponding to that cycle sum to an all-zero column. A linearly independent set of columns, then, cannot contain a cycle, which is the very thing that was to be proved. Note, however, that the converse is not true; a linearly dependent set of columns may be a forest, such as the condition where there are 2 directed edges connecting one vertex to another.
   5. The two results are not contradictory because, while a linearly independent set of columns cannot contain a cycle, a non-independent set of columns does not necessarily contain a cycle.

4. Subproblems
   1. If there exists a more-optimal answer than that produced by this algorithm, it would imply that some $a_j$ which could be substituted in before its deadline $d_j$ which is of higher value than those in result of the algorithm. However, since the algorithm considers the tasks in order of decreasing value, it already chose the highest value tasks possible to complete. Therefore, the answer is always optimal.
   2. omitted pending Section 21.3

5. Subproblems
   1. ```
      // where R is array of size n
      FurthestInFuture( R, n, k )
        // list of decisions
        let D be an array of same size as R
        // track the cache
        let C be an array of size k
        let l be an integer initialized to 0
        // simulate requests
        for i in 1..n
            if R[i] in C
                // cache hit
                D[i] = NULL
                continue
            if l < k
                // empty space in cache

        return D
      ```