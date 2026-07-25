#advanced-cryptography #third-semester #exam-paper-answer 

# Strong Collision Resistance vs Weak Collision Resistance **[5 Marks]**

## Strong Collision Resistance

**Definition:**

Strong collision resistance means it is computationally infeasible to find **any two different messages** that produce the same hash value.

Mathematically,

$$
M_1 \ne M_2
$$

such that

$$
H(M_1)=H(M_2).
$$

**Example:**

The attacker is free to choose both messages and tries to find:

$$
H(M_1)=H(M_2).
$$

---

## Weak Collision Resistance (Second Preimage Resistance)

**Definition:**

Weak collision resistance means that, given a message $M_1$, it is computationally infeasible to find another message $M_2$ such that both produce the same hash value.

Mathematically,

Given $M_1$, find

$$
M_2 \ne M_1
$$

such that

$$
H(M_1)=H(M_2).
$$

**Example:**

Given a document and its hash, the attacker tries to create another document with the **same hash**.

---

## Differences


| **Strong Collision Resistance**                                                       | **Weak Collision Resistance (Second Preimage Resistance)**                             |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| It is difficult to find **any two different messages** with the same hash.            | It is difficult to find **another message** with the same hash as a **given message**. |
| The attacker is free to choose **both messages**.                                     | One message is **already fixed**; the attacker chooses only the second message.        |
| Goal is to find **any collision**.                                                    | Goal is to find a **second preimage** for a specific message.                          |
| Mathematical form: Find $$M_1 \ne M_2$$ such that $$H(M_1)=H(M_2).$$                  | Given $$M_1$$, find $$M_2 \ne M_1$$ such that $$H(M_1)=H(M_2).$$                       |
| The attacker has **more freedom** because both messages can be chosen.                | The attacker has **less freedom** because one message is fixed.                        |
| It provides protection against **general collision attacks**.                         | It provides protection against **message substitution attacks**.                       |
| Strong collision attacks require finding **any colliding pair**.                      | Weak collision attacks require matching the hash of a **specific message**.            |
| It is generally **harder** to satisfy and is considered a stronger security property. | It is comparatively **easier** than strong collision resistance.                       |


---

## Conclusion

A secure cryptographic hash function should provide both **strong collision resistance** and **weak collision resistance**. Strong collision resistance prevents an attacker from finding any pair of messages with the same hash, while weak collision resistance prevents finding a second message that matches the hash of a given message. These properties are essential for ensuring the integrity and authenticity of data.
