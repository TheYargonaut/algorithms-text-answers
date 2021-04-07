# Ch 15 Problems

1. Since it's acyclic, it can actually be solved with dynamic programming in the same way as shortest-path routing but with the opposite metric.

2. Use the 'longest common subsequence' algorithm on the string and a reversed copy of the string. It can of course be optimized to work from only one copy, but the asymptotic running time will be identical.

3. Scan horizontally, keeping track of the cost of each subproblem (subset of points) optimal solution, which goes by assigning each point to the leftward or rightward part of the tour (starting with the two leftmost points arbitrarily assigned). Adding a point with each larger problem and using memoization will yield an $O(n^2)$ solution.

4. Add words, solve lines? Use hash of lines (or word index and line) to tabulate costs for lower lines/words. Should be $O(n)$ in space (limited number of words to shift per line) and $O(n^3)$ in time (adding n rows, each adjusting n lines, each checking $O(n)$ subproblems)

5. Subproblems
   1. Costs for each set of operations which produces the substrings of increasing length in $z$, capped with $kill$. Use memoization, build table of choices for order. Each is production of a substring plus next letter. Should be $O(n^3)$ in time, $O(n^2)$ in space.
   2. Restrict operations by removing twiddle; the remaining operations can all be represented by adding spaces to one sequence or the other (but never both), and allows copys on non-equal values (for penalty). By assigning the appropriate costs, the edit distance algorithm can solve the alignment problem.

6. Subtrees are subproblems, memoize solutions, essentially move upward leaves to root (recursion stack grows in oposite direction, of course) solving each subtree with restrictions and moving back upward.

7. Subproblems
   1. Just traverse the graph in-order? $\Theta(s.length)$
   2. Now it needs a dynamic programming solution, taking each valid path to sound 1, then to sound 2, etc. and consolidating the solutions at each spot. Asymptotically linear in sequence length plus number of edges.

8. Subproblems
   1. Each step can choose from n (the first step), 2 (where the previous step was on an edge), or three pixels to remove. This means the number of unique sequences is $\Omega(2^n)$.
   2. Choose each at the top. Evaluate with next row of pixels and keep best. For each pixel, keep the best score and associated sequence in a table size $O(mn)$ (since one entry of size up to $n$ for each of the $m$ pixels). Since each is evaluated in $O(1)$ time, it will also run in time $O(mn)$.

9. Work backward joining smallest strings, then assembling the next size using each combination of smaller, and memoize the sequence costs, preserving the lowest-cost sequence to build (really to break) each string, until finally the original string has a path all the way from the smallest strings in order. The inverse of the build-order is the break-order.

10. Subproblems
    1.  Follows from linearity of the returns
    2.  Any solution to $k$ years with money ending in investment $i$ includes the optimal solution to $k-1$ years with money ending in each of the investments, and each solution is independent of the others.
    3.  Solve for first year given that the money ends up in each investment, then do the same for each subsequent year given the solutions to the previous years until all years are solved, then take the path with the highest overall return. Total running time $\Theta(n)$ per year; similarly in space, though since the algorithm only needs to remember the results of the previous year and the currently-solving year it only needs $\Theta(n)$ space period, not proportional to the number of years. (basically Viterbi algorithm)
    4.  Creates dependencies between sub-problems which are non-linear.

11. Comes down to balancing inventory costs vs. part-time labor costs. Trivially $O(nD)$ by choosing each value from $0..D$ as the full-time monthly production rate $p$ and evaluating for that solution. Can take advantage of linearity of subproblems to produce a binary-search style algorithm: for each choice of $p$ starting with $p=D/2$ evaluate the derivative of monthly costs (and total) and use the overall sign to produce an $O(n\lg D)$ hill-climbing algorithm.

12. Exploit marginal value; each value spent includes solution to subproblems of spending less money. Increase by $100,000 each time (seems to be the quantum of this problem), memoize previous solution, compare VORP of new player(s) which can be signed versus with smaller amount. O(XNP) because total players to consider is NP and number of subproblems is proportional to X.