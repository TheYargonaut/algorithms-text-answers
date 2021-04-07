# Ch 13 Problems

1. Subproblems
   1. For insertion, only those on the simple route from the root to the insertion point.\
      For deletion, only those adjacent to the removed node and the node which replaces it
   2. De-allocate non-overlapping nodes\
      Move new-root to previous-root\
      Add new nodes down search path
   3. $\Theta(h)$ in both
   4. Basically have to create completely new tree, otherwise the two would feed into eachother and be confused.
   5. Just apply it to a red-black tree. Not much more to it, though it may require additional copies (no more than an increase in coefficient on the $O(h)$) for where reorg occurs to preserve red-black properties.

2. Subproblems
   1. Keep track of bh for the current node and decrement when moving over a black node. At most 1 computation per node visited.
   2. Go right until finding a black node with the right black height
   3. Make $T_y$'s parent point to $x$, make `$x.left$` point to $T_y$ and `$x.right$` point to $T_2$
   4. Red. Fix upward.
   5. Just swap the roles of the trees.
   6. Join is $O(1)$, color fixing is $O(\lg n)$, so the whole thing is $O(\lg n)$

3. Subproblems
   1. tedious, elide
   2. Proceed upward, find forst node where the height on each subtree would differ by 2. Rotate in the direction to resolve.
   3. Normal tree insert then call `BALANCE`.
   4. Same insertion time and seek time to rotation location $O(\lg n)$, then the single rotation to equalize the heights.

4. Subproblems
   1. Specifies keys and order of insertion; there is no alternate arrangement which satisfies the 3 properties; if one existed, it would violate at least one of the properties.
   2. Same result as that for a randomly-constructed binary tree.
   3. The hint gives literally the whole procedure; after normal tree insert based on the key, use rotations to move the new node upward until the min-heap property is restored.
   4. Insertion time $\Theta(\lg n)$ plus the rotation time which is $O(\lg n)$ moving toward the root, so is in total $\Theta(\lg n)$.
   5. Each rotation moves exactly one edge past the node which must be traversed for either the right or the left spine. Therefore, the total number of rotations is equal to the sum of the length of the spines.
   6. Relative priority of $y$ and $x$ follows from the condition on being in a subtree of $x$, while the relative key values follow from the condition on it being the left subtree, and the final condition follows from the stipulation that it be in the right spine of the left subtree.
   7. elide combinatorics
   8. Follows from previous result
   9. inverse of previous combinatorics
   10. Sum of expectations is less than 2, following from previous results indicates expected number of rotations performed on insertion is less than 2.