#third-semester #advanced-cryptography 

# Passive vs Active Attacks ⭐⭐⭐⭐⭐

## Passive Attack

### Definition

A **passive attack** is an attack in which the attacker **only listens, observes, or copies information** without changing the data.

### Simple Definition (2 Marks)

> **A passive attack is an attack in which an attacker monitors or intercepts data without modifying it.**

---

### Easy Example

Imagine two friends are talking.

👨 Alice → 👨 Bob

A third person, Eve, secretly listens to their conversation.

She **does not interrupt** or change anything.

She only gathers information.

This is a **Passive Attack**.

```text
Alice -------------> Bob
         👂 Eve
      (Listening only)
```

---

### Characteristics

* Only observes data
* Does not modify data
* Hard to detect
* Goal is to steal information

---

### Examples

* Eavesdropping
* Traffic analysis
* Packet sniffing
* Reading confidential emails

---

# Active Attack

### Definition

An **active attack** is an attack where the attacker **modifies, inserts, deletes, or interrupts** data.

### Simple Definition (2 Marks)

> **An active attack is an attack in which an attacker alters, inserts, deletes, or disrupts data or system operations.**

---

### Easy Example

Alice sends

```text
Transfer $100
```

Attacker changes it to

```text
Transfer $10,000
```

Bob receives the modified message.

This is an **Active Attack**.

```text
Alice -----> Eve -----> Bob

Transfer $100

↓

Transfer $10,000
```

---

### Characteristics

* Modifies data
* Can delete or insert messages
* Easier to detect than passive attacks
* Goal is to damage or manipulate communication

---

### Examples

* Message modification
* Replay attack
* Denial of Service (DoS)
* Masquerade (pretending to be another user)
* Session hijacking

---

# Types of Passive Attacks ⭐⭐⭐⭐

## 1. Release of Message Contents

The attacker reads confidential information.

Example

Reading someone's email.

---

## 2. Traffic Analysis

Even if messages are encrypted, the attacker studies:

* Who is communicating
* How often
* Message size
* Timing

Example

Seeing that a bank communicates with its server every minute, even without reading the encrypted content.

---

# Types of Active Attacks ⭐⭐⭐⭐

## 1. Masquerade

Pretending to be another user.

Example

Logging in using someone else's account.

---

## 2. Replay Attack

Recording a valid message and sending it again later.

Example

Recording a payment request and replaying it to make another payment.

---

## 3. Message Modification

Changing the original message.

Example

```text
Original:

Pay $500

↓

Modified:

Pay $5000
```

---

## 4. Denial of Service (DoS)

Flooding a server with requests so legitimate users cannot access it.

Example

A website crashes because millions of fake requests are sent to it.

---

# Passive vs Active Attack Comparison ⭐⭐⭐⭐⭐

| Passive Attack                | Active Attack                              |
| ----------------------------- | ------------------------------------------ |
| Only observes data            | Modifies data                              |
| Does not change information   | Changes, inserts, or deletes information   |
| Difficult to detect           | Easier to detect                           |
| Goal: gather information      | Goal: damage or disrupt communication      |
| No effect on system resources | Can affect system performance              |
| Example: Eavesdropping        | Example: DoS, Replay, Message Modification |

---

# Easy Memory Trick ⭐⭐⭐⭐⭐

### Passive = Observe 👀

Think of a spy hiding behind a wall, listening to conversations.

**Action:** Only watches and listens.

---

### Active = Attack ⚔️

Think of a thief intercepting a letter, changing its contents, and sending it onward.

**Action:** Changes or disrupts data.

---

# Real-Life Analogy

Imagine sending a letter.

### Passive Attack

Someone secretly photocopies your letter and puts it back in the mailbox.

✔ Letter reaches the receiver unchanged.

❌ Your privacy is lost.

---

### Active Attack

Someone opens the letter, changes the contents, and reseals it.

Receiver gets a modified letter.

---

# How to Prevent Them

### Passive Attacks

* Encryption (AES, RSA)
* Secure communication (HTTPS, VPN)
* Strong access control

---

### Active Attacks

* Digital signatures
* Message Authentication Codes (MAC)
* Hash functions
* Firewalls
* Intrusion Detection Systems (IDS)

---

# Exam Definitions ⭐⭐⭐⭐⭐

### Passive Attack

> A passive attack is an attack in which an attacker only monitors or intercepts data without altering it.

### Active Attack

> An active attack is an attack in which an attacker modifies, inserts, deletes, or disrupts data or communication.

---

# Frequently Asked Exam Questions ⭐⭐⭐⭐⭐

### 2 Marks

1. Define passive attack.
2. Define active attack.
3. Give one example of each.

### 5 Marks

1. Differentiate passive and active attacks.
2. Explain the types of passive attacks.
3. Explain the types of active attacks with examples.

---

# One-Minute Revision ⭐⭐⭐⭐⭐

```text
PASSIVE ATTACK
✔ Only listens
✔ No data modification
✔ Hard to detect

Examples:
• Eavesdropping
• Traffic Analysis

----------------------------

ACTIVE ATTACK
✔ Changes data
✔ Inserts or deletes messages
✔ Easier to detect

Examples:
• Replay Attack
• Message Modification
• Masquerade
• Denial of Service (DoS)
```

## Super Easy Memory

* **Passive Attack = "Read only"** 📖 → The attacker secretly watches or listens but does **not** change anything.
* **Active Attack = "Read + Write"** ✏️ → The attacker **changes**, **adds**, **deletes**, or **blocks** information.
