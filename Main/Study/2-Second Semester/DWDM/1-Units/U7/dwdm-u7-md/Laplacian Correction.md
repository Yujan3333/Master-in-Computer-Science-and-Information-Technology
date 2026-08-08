## Laplacian Correction (Laplace Smoothing) – Working

Used mainly in **Naive Bayes** to avoid zero probability when a class–feature combination is not seen in training data.

If probability becomes 0, then the whole posterior probability becomes 0.
Laplacian correction fixes this by adding 1 to all counts.

---

## Formula

For categorical data:

$$P(x|C)=\frac{count(x,C)+1}{count(C)+k}$$

Where:

* $count(x,C)$ = number of times feature value $x$ appears in class $C$
* $count(C)$ = total samples in class $C$
* $k$ = number of possible values of that feature

---

## Example

Suppose we are classifying emails as **Spam** or **Not Spam** using one feature:

Feature: *Contains word “Offer”*
Values: {Yes, No} → so $k=2$

Training data:

| Class    | Total emails | "Offer"=Yes | "Offer"=No |
| -------- | ------------ | ----------- | ---------- |
| Spam     | 6            | 4           | 2          |
| Not Spam | 4            | 0           | 4          |

Notice:
For Not Spam, "Offer"=Yes never appears → probability becomes 0.

---

## Without Laplacian Correction

For Not Spam:

$$P(Offer=Yes|NotSpam)=\frac{0}{4}=0$$

This makes classification impossible if Offer=Yes occurs.

---

## With Laplacian Correction

Apply:

$$P(x|C)=\frac{count(x,C)+1}{count(C)+k}$$

### For Spam

$$P(Offer=Yes|Spam)=\frac{4+1}{6+2}=\frac{5}{8}$$

$$P(Offer=No|Spam)=\frac{2+1}{6+2}=\frac{3}{8}$$

---

### For Not Spam

$$P(Offer=Yes|NotSpam)=\frac{0+1}{4+2}=\frac{1}{6}$$

$$P(Offer=No|NotSpam)=\frac{4+1}{4+2}=\frac{5}{6}$$

---

## Final Answer

After Laplacian correction:

| Probability  | Value     |               |
| ------------ | --------- | ------------- |
| $P(Offer=Yes | Spam)$    | $\frac{5}{8}$ |
| $P(Offer=No  | Spam)$    | $\frac{3}{8}$ |
| $P(Offer=Yes | NotSpam)$ | $\frac{1}{6}$ |
| $P(Offer=No  | NotSpam)$ | $\frac{5}{6}$ |

Now no probability is zero, and Naive Bayes can work correctly.

---

### One-line exam definition:

**Laplacian correction adds 1 to all frequency counts and adds $k$ to the denominator to prevent zero probabilities in probabilistic classifiers like Naive Bayes.**
