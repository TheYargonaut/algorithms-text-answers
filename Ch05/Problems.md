# Ch 5 Problems

1. Subproblems
   1. Induction, each increment occurs after expected time $n_{k+1}-n_k$. Using linearity of expectation, this implies that $E[n_i|n]=n$
   2. $Var(n_i|n)=E[(E[n_i|n]-n_i|n)^2]=E[n_i^2|n]-{E[n_i|n]}^2=\sum_{k=1}^n\frac{100^2}{100}-n^2=100n-n^2$

2. tedious, elide