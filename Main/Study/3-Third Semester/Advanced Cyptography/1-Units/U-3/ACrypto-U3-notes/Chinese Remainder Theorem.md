#advanced-cryptography #third-semester #rabin-cypto-system

- [CRT](https://www.youtube.com/watch?v=Fyr9rUWhhTM&list=PL9FuOtXibFjV77w2eyil4Xzp8eooqsPp8&index=41)

---

![](../../../../../../../Images/Third_Sem_Images/Chinese%20Remainder%20Theorem.png)


# Example: Using CRT in Rabin Cryptosystem

Given:

$$
p=7,\qquad q=11
$$

Compute:

$$
n=pq=77
$$

Suppose after decryption we obtain:

$$
m_p=\pm2 \pmod7
$$

and

$$
m_q=\pm4 \pmod{11}
$$

Since each modulus has two square roots, there are **4 possible plaintexts**.

---

## Step 1: Compute CRT Constants

Find:

$$
q^{-1}\pmod p
$$

Since

$$
11\equiv4\pmod7
$$

and

$$
4\times2=8\equiv1\pmod7
$$

we get

$$
q^{-1}=2.
$$

Now find

$$
p^{-1}\pmod q.
$$

Since

$$
7\times8=56\equiv1\pmod{11}
$$

we get

$$
p^{-1}=8.
$$

---

## Step 2: Compute

$$
a=q\times q^{-1}=11\times2=22
$$

$$
b=p\times p^{-1}=7\times8=56
$$

---

## Step 3: First Root

Take

$$
m_p=2,\qquad m_q=4.
$$

Apply CRT:

$$
M=(a,m_p+b,m_q)\bmod77
$$

$$
=(22\times2+56\times4)\bmod77
$$

$$
=(44+224)\bmod77
$$

$$
268\bmod77=37.
$$

First solution:

$$
M=37.
$$

---

## Step 4: Remaining Three Roots

Using all sign combinations:

| $m_p$ | $m_q$ | Plaintext |
| ----- | ----- | --------- |
| $2$   | $4$   | $37$      |
| $2$   | $-4$  | $51$      |
| $-2$  | $4$   | $26$      |
| $-2$  | $-4$  | $40$      |

Thus, Rabin decryption gives the four possible plaintexts:

$$
\boxed{26,;37,;40,;51}
$$

The receiver uses **padding or message redundancy** to identify the correct plaintext.

---

## Exam Tip (5 marks)

You only need to show **one CRT calculation** (like the first root above) and then mention:

> "Since there are two square roots modulo $p$ and two modulo $q$, CRT combines them to produce **four possible plaintexts**. The correct plaintext is selected using redundancy or padding."

This is usually sufficient for a 5-mark answer.
