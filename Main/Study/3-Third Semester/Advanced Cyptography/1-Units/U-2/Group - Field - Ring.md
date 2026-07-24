#advanced-cryptography #third-semester 

---

# 1. Group

## Definition

A **Group** is a set of elements with one binary operation that satisfies **four properties**.

### Properties

1. **Closure** – The result of the operation is still in the group.
2. **Associativity** – The grouping of operations does not matter.
3. **Identity Element** – There exists an element $e$ such that

$$
a \times e = e \times a = a
$$

4. **Inverse Element** – Every element has an inverse.

$$
a \times a^{-1}=e
$$

### Example

Integers under addition

$$
(\mathbb{Z},+)
$$

Identity = 0

Inverse of 5 = -5

---

# 2. Ring

## Definition

A **Ring** is a set equipped with **two operations**:

* Addition
* Multiplication

Addition forms a **group**, while multiplication satisfies closure and associativity.

### Properties

* Addition forms a group.
* Multiplication is associative.
* Distributive law holds.

$$
a(b+c)=ab+ac
$$

### Example

Integers

$$
(\mathbb{Z},+,\times)
$$

Integers form a ring because:

* Addition forms a group.
* Multiplication works normally.
* Division is **not** always possible.

Example:

$$
3 \div 2
$$

is **not** an integer.

---

# 3. Field

## Definition

A **Field** is a ring in which **every non-zero element has a multiplicative inverse**.

This means you can perform:

* Addition
* Subtraction
* Multiplication
* Division (except by zero)

### Example

Rational numbers

$$
(\mathbb{Q},+,\times)
$$

Example

$$
\frac{3}{5}\div\frac{2}{7}
=

\frac{21}{10}
$$

Division is possible.

---

# Galois Field

A **Galois Field (GF)** is simply a **finite field**.

Example

$$
GF(2)={0,1}
$$

Only two elements exist.

Operations are performed modulo 2.

---

# Difference

| Group                      | Ring                                | Field                                             |
| -------------------------- | ----------------------------------- | ------------------------------------------------- |
| One operation              | Two operations                      | Two operations                                    |
| Addition or multiplication | Addition + Multiplication           | Addition + Multiplication + Division              |
| Inverse for one operation  | Multiplicative inverse not required | Every non-zero element has multiplicative inverse |
| Example: $(\mathbb{Z},+)$  | Example: $(\mathbb{Z},+,\times)$    | Example: $(\mathbb{Q},+,\times)$                  |

---

# Memory Trick

```text
Group
   │
   ▼
One Operation

↓

Ring
   │
   ▼
Two Operations

↓

Field
   │
   ▼
Two Operations + Division

↓

Galois Field
   │
   ▼
Finite Field
```

### Easy way to remember

* **Group** → One operation (e.g., addition).
* **Ring** → Addition + Multiplication.
* **Field** → Addition + Multiplication + Division (except by zero).
* **Galois Field** → A **finite** field used in cryptography (e.g., AES uses $GF(2^8)$).
