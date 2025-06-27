# Perceptron and MLP Implementations

## 1. NOT Function Using Perceptron

**Truth Table:**

| x | NOT(x) |
|---|--------|
| 0 |   1    |
| 1 |   0    |

**Perceptron Implementation:**
- **Weight:** w = -2
- **Bias:** b = 1
- **Activation:** y = step(wx + b) = step(-2x + 1)

**Verification:**
- x = 0: y = step(-2(0) + 1) = step(1) = 1 ✓
- x = 1: y = step(-2(1) + 1) = step(-1) = 0 ✓

```
Input(x) --[-2]--> [+1] --> [Step] --> Output
                   ^bias
```

---

## 2. NAND Function Using Perceptron

**Truth Table:**

| x1 | x2 | NAND |
|----|----|----- |
| 0  | 0  |  1   |
| 0  | 1  |  1   |
| 1  | 0  |  1   |
| 1  | 1  |  0   |

**Perceptron Implementation:**
- **Weights:** w1 = -1, w2 = -1
- **Bias:** b = 1.5
- **Activation:** y = step(w1x1 + w2x2 + b) = step(-x1 - x2 + 1.5)

**Verification:**
- (0,0): y = step(0 + 0 + 1.5) = step(1.5) = 1 ✓
- (0,1): y = step(0 - 1 + 1.5) = step(0.5) = 1 ✓
- (1,0): y = step(-1 + 0 + 1.5) = step(0.5) = 1 ✓
- (1,1): y = step(-1 - 1 + 1.5) = step(-0.5) = 0 ✓

```
x1 --[-1]--\
            [+1.5] --> [Step] --> Output
x2 --[-1]--/
           ^bias
```

---

## 3. XNOR Function - Cannot Use Single Perceptron!

**Truth Table:**

| x1 | x2 | XNOR |
|----|----|----- |
| 0  | 0  |  1   |
| 0  | 1  |  0   |
| 1  | 0  |  0   |
| 1  | 1  |  1   |

**Why Single Perceptron Fails:**
XNOR is NOT linearly separable. No single line can separate the classes:
- Class 1: (0,0) and (1,1)
- Class 0: (0,1) and (1,0)

These points form an "X" pattern that requires a non-linear decision boundary.

---

## 4. XNOR Function Using MLP

**Method 1: Using AND and NOR decomposition**
XNOR(x1,x2) = OR(AND(x1,x2), NOR(x1,x2))

**Architecture:**
- **Hidden Layer:** 2 neurons (AND and NOR)
- **Output Layer:** 1 neuron (OR)

**Hidden Layer Weights:**
```
Neuron 1 (AND): w11=1, w12=1, b1=-1.5
Neuron 2 (NOR): w21=-1, w22=-1, b2=0.5
```

**Output Layer Weights:**
```
OR gate: w1=1, w2=1, b=-0.5
```

**Complete MLP Structure:**
```
x1 ----[1]---\     /--[1]--\
             AND--/        OR --> Output
x2 ----[1]---/            /
                         /
x1 ---[-1]--\     /--[1]-/
            NOR--/
x2 ---[-1]--/
```

**Method 2: Direct Implementation**
```
Hidden Layer:
h1 = step(x1 + x2 - 1.5)     # AND-like
h2 = step(-x1 - x2 + 0.5)    # NOR-like

Output Layer:
y = step(h1 + h2 - 0.5)      # OR of hidden units
```

**Verification:**
- (0,0): h1=0, h2=1 → y=step(0+1-0.5)=1 ✓
- (0,1): h1=0, h2=0 → y=step(0+0-0.5)=0 ✓
- (1,0): h1=0, h2=0 → y=step(0+0-0.5)=0 ✓
- (1,1): h1=1, h2=0 → y=step(1+0-0.5)=1 ✓

## Summary
- **NOT & NAND:** Can be implemented with single perceptron
- **XNOR:** Requires MLP (minimum 2 hidden neurons) due to non-linear separability