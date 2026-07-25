#advanced-cryptography #third-semester #exam-paper-answer 

We need to find the **discrete logarithm** of 4 modulo 13 with base 3.

That is,

$$
\log_3 4 \pmod{13}
$$

This means we need to find an exponent (x) such that

$$
3^x \equiv 4 \pmod{13}.
$$

---

## Step 1: Compute powers of 3 modulo 13

| (x) | $(3^x)$ | $(3^x \bmod 13)$ |
| --: | ------: | ---------------: |
|   0 |       1 |                1 |
|   1 |       3 |                3 |
|   2 |       9 |                9 |
|   3 |      27 |                1 |
|   4 |      81 |                3 |
|   5 |     243 |                9 |
| ... |     ... |              ... |

Notice the values repeat:

$$
1,;3,;9,;1,;3,;9,\ldots
$$

The value **4 never appears**.

---

## Step 2: Conclusion

There is **no integer (x)** such that

$$
3^x \equiv 4 \pmod{13}.
$$

Therefore,

$$
\boxed{\log_3 4 \pmod{13}\ \text{does not exist}.}
$$

### Why?

The powers of 3 modulo 13 generate only the set

$$
{1,3,9},
$$

so 3 is **not a primitive root modulo 13**. Since 4 is not in this set, no discrete logarithm exists for this base and modulus.

**Answer:**

$$
\boxed{\text{No solution (discrete logarithm does not exist).}}
$$
