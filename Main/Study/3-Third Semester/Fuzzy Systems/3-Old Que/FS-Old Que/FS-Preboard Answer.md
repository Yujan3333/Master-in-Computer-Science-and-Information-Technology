#fuzzy-system #third-semester 

[FS-Qno1](FS-Qno1.md)
Consider a fuzzy spectrometer which generates different kinds of waves. Since the fuzzy spectrometer may not generate the accurate output as the SetPoint (SP), we may require a fuzzy controller. Consider the controller is TagakiSugeno Fuzzy Controller defined by the rules. 

Rule 1: If $\text{error}$ is Negative or $\text{change\_error}$ is Positive then output is $$\text{error} - \frac{\text{change\_in\_error}}{\text{error}}$$

Rule 2: If $\text{error}$ is Positive and $\text{change\_error}$ Zero then output is $$\text{error} + 0.3 \times \text{change\_in\_error s}$$

Now define the linguistic variables Positive, Negative and Zero in the interval $[0.1, 1]$, $[-0.6, 0.6]$ and $[-1, 1]$ respectively using triangular membership function and find the output of the controller if error is 0.06 and change in error is 0.3.

---
[FS-Qno2](FS-Qno2.md)

Construct a fuzzy controller with a set of fuzzy rules. 

How Mamdani inference is used to infer result in the controller? Illustrate with example. Configure the required rules, fuzzy sets and the inputs for executing the rules. $[10]$

---
[FS-Qno3](FS-Qno3.md)

Consider a problem of **minimizing** x defined by a function $f(x) = x/2$, where x can vary from 1 to 15. Now show a single iteration of genetic algorithm with encoding, selection, crossover and mutation operations. You can start with a random initial population. Use your own assumptions as required. $[10]$


---

[FS-Short Questions](FS-Short%20Questions.md)

FS-Qno4

FS-Qno5

FS-Qno6

FS-Qno7

FS-Qno8
