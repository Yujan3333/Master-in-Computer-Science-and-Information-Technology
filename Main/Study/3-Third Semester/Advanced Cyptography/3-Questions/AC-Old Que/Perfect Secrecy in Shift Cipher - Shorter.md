#advanced-cryptography #third-semester #exam-paper-answer #perfect-secrecy 

# Q. Define Perfect Secrecy. Prove that the Shift cipher achieves perfect secrecy for any plaintext probability distribution. **[4+6]**

## (a) Perfect Secrecy (4 Marks)

A cryptosystem has **perfect secrecy** if observing the ciphertext gives **no information** about the plaintext.

$$
P(M=m \mid C=c)=P(M=m)
$$

for every plaintext $m$ and ciphertext $c$.

This means seeing the ciphertext does not change the probability of any plaintext.

### Conditions

* The ciphertext reveals no information about the plaintext.
* The key is chosen uniformly at random.
* Each key is used only once.

---

## (b) Proof

### Given

Plaintext space

$$
M={0,1,\ldots,25}
$$

Key space

$$
K={0,1,\ldots,25}
$$

Each key is equally likely.

$$
P(K=k)=\frac{1}{26}
$$

Encryption rule

$$
C=(M+K)\bmod 26
$$

---

### Step 1: Find the Required Key

For any plaintext $m$ and ciphertext $c$,

$$
k=(c-m)\bmod26
$$

**What is happening?**

For every plaintext-ciphertext pair, there is **exactly one key** that converts $m$ into $c$.

---

### Step 2: Probability of Getting Ciphertext

Since all 26 keys are equally likely,

$$
P(C=c\mid M=m)=\frac{1}{26}
$$

**What is happening?**

Every ciphertext can be produced with probability $\frac{1}{26}$ regardless of the plaintext.

---

### Step 3: Apply Bayes' Theorem

$$
\begin{aligned}
P(M=m\mid C=c)
&=
\frac{P(C=c\mid M=m),P(M=m)}
{P(C=c)}
\end{aligned}
$$

**What is happening?**

We use Bayes' theorem to find the probability of the plaintext **after seeing the ciphertext**.

---

Since

$$
P(C=c\mid M=m)=\frac{1}{26}
$$

and

$$
\begin{aligned}
P(C=c)
&=
\sum_m P(C=c\mid M=m),P(M=m)
\end{aligned}
$$

**What is happening?**

We calculate the total probability of receiving ciphertext $c$ by considering **all possible plaintexts**.

---

Substitute the value:

$$
\begin{aligned}
P(C=c)
&=
\frac{1}{26}\sum_m P(M=m)
\end{aligned}
$$

Since

$$
\sum_m P(M=m)=1
$$

we get

$$
P(C=c)=\frac{1}{26}
$$

**What is happening?**

The probabilities of all plaintexts add up to 1, so the ciphertext probability is also $\frac{1}{26}$.

---

Now,

$$
\begin{aligned}
P(M=m\mid C=c)
&=
\frac{\frac{1}{26}P(M=m)}
{\frac{1}{26}}\
&=
P(M=m)
\end{aligned}
$$

**What is happening?**

The $\frac{1}{26}$ terms cancel, leaving the original plaintext probability unchanged.

---

## Conclusion

Since

$$
P(M=m\mid C=c)=P(M=m)
$$

the ciphertext does not change the probability of the plaintext.

Therefore, the Shift cipher satisfies **perfect secrecy**, **provided the key is chosen uniformly at random and used only once**.

---

### Why each step?

| Step                  | Why?                                                        |
| --------------------- | ----------------------------------------------------------- |
| Find unique key       | Shows every plaintext-ciphertext pair has exactly one key.  |
| Compute $P(C\mid M)$  | Shows every ciphertext is equally likely.                   |
| Compute $P(C)$        | Required by Bayes' theorem.                                 |
| Apply Bayes           | Finds the probability of plaintext after seeing ciphertext. |
| Compare probabilities | If unchanged, perfect secrecy is proved.                    |


