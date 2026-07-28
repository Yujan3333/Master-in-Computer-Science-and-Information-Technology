#fuzzy-system #third-semester #old-que #exam-paper-answer 

# Question 1 (10 Marks)
Consider a fuzzy spectrometer which generates different kinds of waves. Since the fuzzy spectrometer may not generate the accurate output as the SetPoint (SP), we may require a fuzzy controller. Consider the controller is TagakiSugeno Fuzzy Controller defined by the rules. 

Rule 1: If $\text{error}$ is Negative or $\text{change\_error}$ is Positive then output is $$\text{error} - \frac{\text{change\_in\_error}}{\text{error}}$$

Rule 2: If $\text{error}$ is Positive and $\text{change\_error}$ Zero then output is $$\text{error} + 0.3 \times \text{change\_in\_error s}$$

Now define the linguistic variables Positive, Negative and Zero in the interval $[0.1, 1]$, $[-0.6, 0.6]$ and $[-1, 1]$ respectively using triangular membership function and find the output of the controller if error is 0.06 and change in error is 0.3.

### Consider a Takagi–Sugeno Fuzzy Controller

**Rules**

**Rule 1**

IF **error is Negative** OR **change_error is Positive**

THEN

$$[
Output = error-\frac{change_error}{error}
]$$

**Rule 2**

IF **error is Positive** AND **change_error is Zero**

THEN

$$[
Output=error+0.3\times change_error
]$$

Given

* Error, (e=0.06)
* Change in Error, (ce=0.3)

Linguistic variables are defined by triangular membership functions:

* Positive : ([0.1,1])
* Negative : ([-0.6,0.6])
* Zero : ([-1,1])

Find the controller output.

---

# Step 1: Draw/Define Membership Functions

We assume symmetric triangular membership functions.

### Positive

Triangle:

$$
(0.1,1,1)
$$

Membership equation

$$
\mu_P(x)=
\begin{cases}
0,&x<0.1\\ \\
\dfrac{x-0.1}{1-0.1},&0.1\le x\le1
\end{cases}
$$

Since


$$e=0.06<0.1$$


therefore


$$\boxed{\mu_P(e)=0}$$


---

### Negative

Triangle


$$(-0.6,0,0.6)$$


Membership equation

$$
\mu_N(x)=
\begin{cases}
\dfrac{x+0.6}{0.6},&-0.6\le x\le0 \\\\
\dfrac{0.6-x}{0.6},&0\le x\le0.6
\end{cases}
$$

Since


$$e=0.06$$



$$\mu_N(e)
\\=

\frac{0.6-0.06}{0.6}

\\=

\frac{0.54}{0.6}


\\=

0.9
$$

Hence

$$[
\boxed{\mu_N(e)=0.9}
]$$

---

### Zero

Triangle


$$(-1,0,1)$$


Membership equation


$$\mu_Z(x)
\\=

\frac{1-|x|}{1}
$$

For


$$ce=0.3$$



$$\mu_Z(0.3)
\\=

1-0.3
\\=
0.7$$


Hence


$$\boxed{\mu_Z(ce)=0.7}$$


---

### Positive membership of change error

Since


$$ce=0.3$$



$$\mu_P(0.3)
\\=

\frac{0.3-0.1}{0.9}
\\=
0.222$$


Therefore


$$\boxed{\mu_P(ce)=0.222}$$


---

# Step 2: Rule Firing Strengths

---

## Rule 1

IF error is Negative OR change_error is Positive

OR means

$$
\max
$$

Therefore


$$w_1
\\=

\max(0.9,;0.222)
\\=
0.9$$


---

## Rule 2

IF error is Positive AND change_error is Zero

AND means


$$\min$$


$$w_2
\\=

 \min(0,0.7)
\\=
0$$


---

# Step 3: Rule Outputs

---

## Rule 1 Output

Formula


$$y_1
\\=

e-\frac{ce}{e}$$


Substitute



$$\\=0.06-\frac{0.3}{0.06}$$



$$\\=0.06-5$$




$$\\=-4.94$$


Hence


$$\boxed{y_1=-4.94}$$


---

## Rule 2 Output

Formula


$$y_2
\\=

e+0.3\times ce
$$

$$\\=0.06+0.3(0.3) \\

$$$$\\=0.06+0.09 \\$$

$$$$\\=0.15$$


But

Rule 2 does **not fire**

because

$$
w_2=0
$$

---

# Step 4: Sugeno Weighted Average

Takagi–Sugeno output

$$[
Output
=
\frac{w_1y_1+w_2y_2}
{w_1+w_2}
]$$

Substitute

$$[

\frac{0.9(-4.94)+0(0.15)}
{0.9+0}
]$$

$$[

-4.94
]$$

---

# Final Answer

$$[
\boxed{Output=-4.94}
]$$

---

# Final Exam Answer (Write this)

**Membership values**

$$
\mu_N(e)=0.9,\qquad
\mu_P(e)=0,
$$

$$\mu_Z(ce)=0.7,\qquad
\mu_P(ce)=0.222
$$

**Rule firing strengths**

Rule 1:

$$[
w_1=\max(0.9,0.222)=0.9
]$$

$$Rule 2:

[
w_2=\min(0,0.7)=0
]$$

**Rule outputs**

$$[
y_1=0.06-\frac{0.3}{0.06}=-4.94
]$

$$[
y_2=0.06+0.3(0.3)=0.15
]$$

**Overall Sugeno Output**

$$[
\boxed{
Output=
\frac{0.9(-4.94)+0(0.15)}
{0.9}
=-4.94
}
]$$

---

### **Exam Tip ⚠️**

The question says **"Use your own assumptions as required."** Since the exact triangular membership functions are not fully specified (only intervals are given), different teachers or textbooks may define the triangles slightly differently. The **procedure** (finding memberships → rule firing → rule outputs → weighted average) is what earns most of the marks, even if the exact numerical values differ slightly.
