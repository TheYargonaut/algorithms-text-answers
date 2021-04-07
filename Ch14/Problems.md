# Ch 14 Problems

1. Subproblems
   1. Number only changes on endpoints, so at least one point of maximum overlap is at an endpoint of some interval.
   2. Solution [here](https://rqlbub.wordpress.com/2014/01/05/interval-tree-point-of-maximum-overlap/).
   
2. Build OS tree with keys 1..n in time $O(n\lg n)$. Keep track of the kill position by adding M-1 modulo the remaining tree size to the previous kill position, deleting the node with that rank each time and placing the key onto a stack for return (also $O(n\lg n)$).