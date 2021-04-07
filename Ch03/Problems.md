# Ch 3 Problems

1. Subproblems
   1. Obvious, elide
   2. Obvious, elide
   3. Obvious, elide
   4. Obvious, elide
   5. Obvious, elide

2. |part|O|o|$\Omega$|$\omega$|$\Theta$|
   |----|-|-|--------|--------|--------|
   |a|y|y|n|n|n|
   |b|y|y|n|n|n|
   |c|n|n|n|n|n|
   |d|n|n|y|y|n|
   |e|y|n|y|n|y|
   |f|y|y|n|n|n|

3. Tedious, elide

4. Subproblems, informal proofs
   1. No, $f(n)=O(g(n))$ implies $g(n)=\Omega(f(n))$; both conditions would be true if and only if $f(n)=\Theta(g(n))$, which does not follow. (counterexample $f(n)=n^2$ and $g(n)=1$)
   2. No, should be max (counterexample $f(n)=n^2$ and $g(n)=1$)
   3. Yes, monotonicity of $\lg$
   4. Yes, monotonicity of $2^x$
   5. No, couterexample $f(n)=n$
   6. Yes, by definintion
   7. No, counterexample $f(n)=2^n$
   8. Yes, by definitions

5. Subproblems, informal proofs
   1. both where oscillates, otherwise must be one or other because infinite integers regardless
   2. elide
   3. If $f(n)$ may be negative, $\Theta$ no longer follows, but the reverse is preserved.
   4. Tedious, elide

6. Subproblems
   1. $n$
   2. ?
   3. $\Theta(\lg{n})$
   4. $\Theta(\lg{n} - 1)$
   5. $\lg\lg{n}$
   6. $\infty$
   7. $\frac{1}{\lg{3}}\lg\lg{n}$
   8. ?