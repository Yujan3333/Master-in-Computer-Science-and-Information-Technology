#general-note
### Primitive Root (Generator) — Simple Definition

A **primitive root (generator)** is a number that can generate **all possible non-zero numbers modulo (p)** by repeatedly raising it to different powers.

In simple words:

> A **primitive root** is a number that can produce every possible value (except 0) when raised to different powers modulo (p).

![](../../../../Images/Third_Sem_Images/Primitive%20Root.png)

---

### Example

Let

$$
p = 7
$$

Choose

$$
g = 3
$$

Now calculate:

$$
3^1 \bmod 7 = 3
$$

$$
3^2 \bmod 7 = 2
$$

$$
3^3 \bmod 7 = 6
$$

$$
3^4 \bmod 7 = 4
$$

$$
3^5 \bmod 7 = 5
$$

$$
3^6 \bmod 7 = 1
$$

The results are:

$$
3,;2,;6,;4,;5,;1
$$

Notice that we got **every number from 1 to 6 exactly once**.

So,

**3 is a primitive root (generator) modulo 7.**

---

### Why is it used in Schnorr?

The generator $$g$$ is chosen so that it can generate **all the values needed** in the cryptographic group. This makes the protocol secure and mathematically correct.

### Exam Definition (2 Marks)

> A **primitive root (generator)** is a number whose powers generate **all non-zero integers modulo (p)** before repeating. It is used in cryptographic algorithms like Schnorr, ElGamal, and Diffie–Hellman to generate group elements.
