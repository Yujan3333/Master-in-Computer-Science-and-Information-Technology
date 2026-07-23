#advanced-cryptography #third-semester #denning-sacco

Mainly 2 Versions
### Version 1 (Most Common in Exams)

The **Denning–Sacco protocol** removes the nonce challenge-response between A and B and **uses timestamps instead**.

Protocol:

1.

$$
A \rightarrow KDC :
\text{ID}_A \parallel \text{ID}_B
$$

2.

$$
KDC \rightarrow A :
E(K_a,[K_s \parallel \text{ID}_B \parallel T])
\parallel
E(K_b,[K_s \parallel \text{ID}_A \parallel T])
$$

3.

$$
A \rightarrow B :
E(K_b,[K_s \parallel \text{ID}_A \parallel T])
$$

4.

B decrypts the ticket, verifies the timestamp $T$, and if it is fresh, accepts $K_s$.

Then A and B start secure communication using $K_s$.

### Why are there no Steps 4 and 5 like Needham–Schroeder?

Because the **timestamp itself proves freshness**. There is no need for Bob to send a nonce challenge ($N_2$) and for Alice to return $f(N_2)$.

---

## Version 2 (Some Books)

Some books **keep the challenge-response** for explicit mutual authentication while **also adding timestamps**.

It looks like:

1.

$$
A \rightarrow KDC :
\text{ID}_A \parallel \text{ID}_B
$$

2.

$$
KDC \rightarrow A :
E(K_a,[K_s \parallel \text{ID}_B \parallel T])
\parallel
E(K_b,[K_s \parallel \text{ID}_A \parallel T])
$$

3.

$$
A \rightarrow B :
E(K_b,[K_s \parallel \text{ID}_A \parallel T])
$$

4.

$$
B \rightarrow A :
E(K_s,N_2)
$$

5.

$$
A \rightarrow B :
E(K_s,f(N_2))
$$

This version gives **both freshness (timestamp)** and **mutual authentication (challenge-response)**.

---

## Are all nonces replaced with timestamps?

**No.**

* The **nonce between A and KDC** (used in Needham–Schroeder to ensure freshness) is typically **replaced by the timestamp**.
* The **challenge nonce $N_2$ between B and A** may:

  * **be omitted** in the standard Denning–Sacco protocol because the timestamp provides freshness, **or**
  * **be retained** in some textbook versions to provide explicit mutual authentication.

### For  exams

Most questions expect the **simpler Denning–Sacco protocol**, where:

* $N_1$ is replaced by **timestamp $T$**.
* The challenge-response ($N_2$, $f(N_2)$) is **removed**.
* The main difference from Needham–Schroeder is the addition of **timestamp $T$** to prevent replay attacks.

If your class notes contain **five protocol messages**, share that page (or a photo), and I'll explain **that exact version**, since instructors sometimes teach a variant rather than the original protocol.
