# Ch 11 Problems

1. Subproblems
   1. $P( collision ) \leq 1/2$ For each sample. The probability of requiring more $k$ probes is the probability of colliding on those $k$ probes, which is $2^{-k}$
   2. $2^{-k}$ is the worst case in this table; all previous insertions have strictly lower probability of collision. $2^{ -2\lg{n} } = 2n^{-2} = O(1/n^2)$
   3. Probability of any of the probes having more than $2\lg{n}$ probes. Use upper bound on binomial process.
   4. Use expectation on binomial process

2. Subproblems
   1. Success, failure, and combinatorics.
   2. Upper bound on binomial process
   3. See Stirling's approximation
   4. elide
   5. elide

3. Subproblems
   1. $j_{y+1}=j_y+i_y=j_1+\sum_{x=1}^yi_x=h(k)+\sum_{x=1}^yx=j_1+y/2+y^2/2$\
      $c_1=c_2=1/2$
   2. $m/2+m^2/2$. Prove that all values are distinct mod m.\
      $\sum_{x=1}^yx-\sum_{x=1}^zx$\
      $=(y^2-z^2+y-z)/2$\
      $=((y-z)(y+z)+y-z)/2$\
      $=((y-z)(y+z+1))/2$\
      Since exactly one of the factors will be even and the other will be odd no matter the choice of $y$ and $z$, any choice which does not produce a factor of at least size $2m$ will not produce a value divisible by $m$. Therefore, all offsets will be unique and every bin visited.

4. Subproblems; see [here](https://walkccc.github.io/CLRS/Chap11/Problems/11-4/) for elided.
   1. 2-universal implies that any of the $m^2$ sequences are equally likely, of which $m$ sequences are collisions, for a probability of $m/m^2=1/m$ of collision, so $|H|/m$ functions collide for any given pair of keys, which is the definition of universality.
   2. For $x=\langle0, 0, ..., 0\rangle$, every hash function in the family produces the same result and cannot be 2-universal. However, because every element is unique mod p, the hash class is universal.
   3. universality giving the $p$ separate paths plus the ability to range b provides $p$ starting points for a total of $p^2$ equally-likely paths, fulfilling the requirement to be 2-universal.
   4. Since $\mathcal H$ is 2-universal, every pair of $\langle t,t'\rangle$ is equally likely to appear, thus $t'$ could be any value from $\mathbb Z_p$​. The probability of choosing a hash function that $h(k) = h(l)$ is at most $1/p$, therefore the probability is at most $1/p$.