#advanced-cryptography #third-semester #exam-paper-answer 

This is a **very common exam question**. The key idea is that **a field requires every non-zero element to have a multiplicative inverse**.

---

# Q. Why is $$Z_6$$ not a field but $$Z_7$$ is? Explain with the properties of a field. (5 Marks)

## Answer

A **field** is a set with two operations (addition and multiplication) satisfying the following properties:

1. Closure
2. Associativity
3. Commutativity - *change in order -> a+b = b+a*
4. Identity elements for addition and multiplication
5. Additive inverses
6. **Multiplicative inverses for every non-zero element**
7. Distributive law

---

## Why is $$Z_6$$ not a field?

$$
Z_6={0,1,2,3,4,5}
$$

Addition and multiplication are performed modulo 6.

A field requires that **every non-zero element has a multiplicative inverse**.

Let's check the element 2.

We need a number $x$ such that

$$
2x \equiv 1 \pmod 6
$$

Try every element:

$$
2 \times 1 = 2
$$

$$
2 \times 2 = 4
$$

$$
2 \times 3 = 6 \equiv 0 \pmod 6
$$

$$
2 \times 4 = 8 \equiv 2 \pmod 6
$$

$$
2 \times 5 = 10 \equiv 4 \pmod 6
$$

We never get

$$
1
$$

So, **2 has no multiplicative inverse**.

Similarly,

$$
3x \equiv 1 \pmod 6
$$

also has no solution.

Since not every non-zero element has a multiplicative inverse,

$$
\boxed{Z_6 \text{ is not a field}.}
$$

---

## Why is $$Z_7$$ a field?

$$
Z_7={0,1,2,3,4,5,6}
$$

Operations are performed modulo 7.

Since **7 is a prime number**, every non-zero element has a multiplicative inverse.

Examples:

$$
1^{-1}=1
$$

because

$$
1 \times 1 \equiv 1 \pmod 7
$$

$$
2^{-1}=4
$$

because

$$
2 \times 4 = 8 \equiv 1 \pmod 7
$$

$$
3^{-1}=5
$$

because

$$
3 \times 5 = 15 \equiv 1 \pmod 7
$$

$$
4^{-1}=2
$$

$$
5^{-1}=3
$$

$$
6^{-1}=6
$$

because

$$
6 \times 6 = 36 \equiv 1 \pmod 7
$$

Every non-zero element has an inverse.

Therefore,

$$
\boxed{Z_7 \text{ is a field}.}
$$

---

# Shortcut Rule (Very Important)

For modular arithmetic:

* If $n$ is **prime**, then $$Z_n$$ is a **field**.
* If $n$ is **composite**, then $$Z_n$$ is **not** a field.

Examples:

| Set        | Prime? | Field? |
| ---------- | ------ | ------ |
| $$Z_5$$    | ✅      | ✅      |
| $$Z_6$$    | ❌      | ❌      |
| $$Z_7$$    | ✅      | ✅      |
| $$Z_8$$    | ❌      | ❌      |
| $$Z_{11}$$ | ✅      | ✅      |

---

# Exam Conclusion

> $Z_6$ is **not** a field because some non-zero elements (such as 2 and 3) do not have multiplicative inverses modulo 6. On the other hand, $Z_7$ is a field because 7 is a prime number, so every non-zero element has a unique multiplicative inverse modulo 7.
