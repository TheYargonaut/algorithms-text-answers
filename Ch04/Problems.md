# Ch 4 Problems

1. Subproblems
   1. $a=2,b=2,f(n)=n^4,n^{\log_b{a}+\epsilon}=n^{1+\epsilon}=f(n)$ where $\epsilon=3,\therefore T(n)=\Theta(n^4)$
   2. $a=1,b=\frac{10}{7},f(n)=n,n^{\log_b{a}+\epsilon}=n^{\epsilon}=f(n)$ where $\epsilon=0,\therefore T(n)=\Theta(\lg{n})$
   3. $a=16,b=4,f(n)=n^2,n^{\log_b{a}+\epsilon}=n^{2+\epsilon}=f(n)$ where $\epsilon=0,\therefore T(n)=\Theta(n^2\lg{n})$
   4. $a=7,b=3,f(n)=n^2,n^{\log_b{a}+\epsilon}=n^{\log_3{7}+\epsilon}=f(n)$ where $\epsilon=2-\log_3{7}>0,\therefore T(n)=\Theta(n^2)$
   5. $a=7,b=2,f(n)=n^2,n^{\log_b{a}+\epsilon}=n^{\log_2{7}+\epsilon}=f(n)$ where $\epsilon=2-\log_2{7}<0,\therefore T(n)=\Theta(n^{\log_2{7}})$
   6. $a=2,b=4,f(n)=n^{\frac{1}{2}},n^{\log_b{a}+\epsilon}=n^{\frac{1}{2}+\epsilon}=f(n)$ where $\epsilon=0,\therefore T(n)=\Theta(\sqrt{n}\lg{n})$
   7. $T(n)=\Theta(n^3)$ by recursion tree

2. Subproblems
   1. binary search
      1. $T(n)=T(n/2)+\Theta(1)=O(\lg{n})$
      2. $T(n)=T(n/2)+\Theta(n)=O(n)$
      3. $T(n)=T(n/2)+\Theta(n/2)=O(n)$
   2. merge sort
      1. $T(n)=2T(n/2)+\Theta(n)=O(n\lg{n})$
      2. $T(n)=2T(n/2)+\Theta(n)=O(n\lg{n})$
      3. $T(n)=2T(n/2)+\Theta(n)=O(n\lg{n})$

3. Subproblems
   1. $z+z\bold{F}(z)+z^2\bold{F}(z)$\
      $=z+z\displaystyle\sum_{i=0}^{\infty}F_iz^i+z^2\displaystyle\sum_{i=0}^{\infty}F_iz^i$\
      $=z+\displaystyle\sum_{i=0}^{\infty}F_iz^{i+1}+\displaystyle\sum_{i=0}^{\infty}F_iz^{i+2}$\
      $=z+\displaystyle\sum_{i=0}^{\infty}F_{i+1}z^{i+2}+\displaystyle\sum_{i=0}^{\infty}F_iz^{i+2}$\
      $=z+\displaystyle\sum_{i=0}^{\infty}(F_i + F_{i+1})z^{i+2}$\
      $=z+\displaystyle\sum_{i=0}^{\infty}F_{i+2}z^{i+2}$\
      $=\displaystyle\sum_{i=0}^{\infty}F_{i+1}z^{i+1}$\
      $=\displaystyle\sum_{i=0}^{\infty}F_iz^i$\
      $=\bold{F}(z)$\
      Q.E.D
   2. $\bold{F}(z)=z+z\bold{F}(z)+z^2\bold{F}(z)$\
      $\bold{F}(z)-z\bold{F}(z)-z^2\bold{F}(z)=z$\
      $(1-z-z^2)\bold{F}(z)=z$\
      $\bold{F}(z)=\frac{z}{1-z-z^2}$\
      Remaining (factorization) tedious, elide
   3. Tedious, elide
   4. Tedious, elide

4. It's almost the consensus problem. Solution [here](http://cseweb.ucsd.edu/classes/su99/cse101/sample1.pdf), I didn't figure it out before looking it up

5. Tedious, elide