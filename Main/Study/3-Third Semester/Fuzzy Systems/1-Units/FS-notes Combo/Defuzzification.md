#fuzzy-system #third-semester 


> "The second inference method, generally referred to as the **Sugeno method, or the TSK method (Takagi, Sugeno, and Kang)**..." 

---

# 1. Mamdani Model

The Mamdani model is the **most common** fuzzy inference method. According to your book, each rule has **fuzzy antecedents and a fuzzy consequent**. 

### Rule Format

```text
IF Temperature is Hot
AND Humidity is High
THEN Fan Speed is Fast
```

Notice:

* **Temperature is Hot** → Fuzzy input
* **Humidity is High** → Fuzzy input
* **Fan Speed is Fast** → Fuzzy output

Everything is described using **linguistic terms**.

---

### How it works

Suppose

```text
Temperature = 32°C
Humidity = 70%
```

After fuzzification,

```text
Hot = 0.8
High = 0.6
```

Using **AND**, the firing strength is

```text
min(0.8,0.6)=0.6
```

The output fuzzy set **Fast** is **truncated** (or scaled, depending on the implication method).

After combining all rules, we still have a **fuzzy output**.

Therefore,

**Defuzzification is required** (usually centroid).

Final result

```text
Fan Speed = 78%
```

---

### Flow

```text
Crisp Inputs
      ↓
Fuzzification
      ↓
Rule Evaluation
      ↓
Fuzzy Output
      ↓
Defuzzification
      ↓
Crisp Output
```

---

## Main Point

✔ Uses fuzzy words in the THEN part.

```text
THEN Fan is Fast
```

---

# 2. Sugeno Model

Your book says that in the Sugeno model:

> "The consequent is a **crisp function**." 

Instead of

```text
THEN Fan is Fast
```

it becomes

```text
THEN Fan = f(x,y)
```

where **f(x,y)** is a mathematical function.

---

### Rule Format

```text
IF Temperature is Hot
AND Humidity is High

THEN

Fan = 2×Temperature + Humidity +10
```

or

```text
THEN Fan =80
```

Both are Sugeno rules.

---

### Example

Suppose

```text
Hot =0.7
High =0.8
```

Rule output

```text
Fan =80
```

Another rule

```text
Warm =0.3

Fan =50
```

Final output

Weighted average

$$[
\frac{0.7(80)+0.3(50)}{0.7+0.3}=71
]$$

Notice:

There is **no fuzzy output**.

So,

No centroid defuzzification is needed.

---

### Flow

```text
Crisp Inputs
      ↓
Fuzzification
      ↓
Rules
      ↓
Numbers from each rule
      ↓
Weighted Average
      ↓
Final Output
```

---

## Main Point

✔ Uses **numbers or equations** in the THEN part.

```text
THEN Fan =80
```

or

```text
THEN Fan =2x+10
```

---

# 3. TSK Model

TSK means

* **T** → Takagi
* **S** → Sugeno
* **K** → Kang

Your textbook clearly says:

> **Sugeno method = TSK method.** 

TSK is simply the full name of the Sugeno approach.

The book also mentions:

* **Zero-order Sugeno:** output is a **constant**.
* **First-order Sugeno:** output is a **linear function** of the inputs. 

### Zero-order TSK

```text
IF Temperature is Hot

THEN Fan =80
```

### First-order TSK

```text
IF Temperature is Hot

THEN

Fan =2×Temperature+10
```

---

# Difference Between Zero-order and First-order TSK

| Zero-order      | First-order            |
| --------------- | ---------------------- |
| THEN Fan = 80   | THEN Fan = 2×Temp + 10 |
| Constant output | Linear equation output |

---

# Comparison

| Feature                  | Mamdani                      | Sugeno / TSK                       |
| ------------------------ | ---------------------------- | ---------------------------------- |
| Rule output              | Fuzzy set (Fast, Slow, High) | Constant or mathematical function  |
| Example                  | THEN Fan is Fast             | THEN Fan = 80 or Fan = 2×Temp + 10 |
| Output before final step | Fuzzy                        | Crisp                              |
| Final computation        | Defuzzification (Centroid)   | Weighted Average                   |
| Speed                    | Slower                       | Faster                             |
| Human readability        | Easy                         | Less intuitive                     |
| Common use               | Expert systems               | Control systems and optimization   |

---

# Easy Memory Trick

Imagine your teacher asks:

**"How fast should the fan rotate?"**

### Mamdani answers using words:

```text
Teacher:
How fast?

System:
FAST
```

You still need to convert **FAST** into a number (e.g., 80%).

---

### Sugeno answers using a number:

```text
Teacher:
How fast?

System:
80%
```

No conversion is needed.

---

### TSK answers using a formula:

```text
Teacher:
How fast?

System:
2 × Temperature + 10
```

The formula is evaluated directly to get the final output.

---

## Exam Tip

If your exam asks **"Differentiate Mamdani and Sugeno (TSK)"**, remember just one sentence:

* **Mamdani:** `THEN` contains a **fuzzy word** (e.g., *Fast*, *High*, *Slow*).
* **Sugeno/TSK:** `THEN` contains a **constant or mathematical equation**, and the final output is obtained using a **weighted average** instead of centroid defuzzification.
