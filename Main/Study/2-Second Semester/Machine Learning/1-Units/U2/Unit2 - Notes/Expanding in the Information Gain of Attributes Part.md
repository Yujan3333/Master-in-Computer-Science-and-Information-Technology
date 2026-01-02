## Step 1: Entropy formula

For a binary class problem (Yes / No):

$$
Entropy(S) = -p_+ \log_2 p_+ - p_- \log_2 p_-
$$

---

## Step 2: Entropy of each Age group

### (a) Entropy(Youth)

From the dataset (standard ID3 example):

* Yes = 2
* No = 3
* Total = 5

$$
p_{Yes} = \frac{2}{5}, \quad p_{No} = \frac{3}{5}
$$

Substitute into entropy formula:

$$
Entropy(Youth) = -\frac{2}{5}\log_2\frac{2}{5} - \frac{3}{5}\log_2\frac{3}{5}
$$

$$
Entropy(Youth) = -(0.4)(-1.322) - (0.6)(-0.737)
$$

$$
Entropy(Youth) = 0.5288 + 0.4422 = 0.971
$$

✅ **Entropy(Youth) = 0.971**

---

### (b) Entropy(Middle_aged)

* Yes = 4
* No = 0

$$
p_{Yes} = 1, \quad p_{No} = 0
$$

$$
Entropy(Middle_aged) = -1\log_2(1) - 0\log_2(0)
$$

$$
Entropy(Middle_aged) = 0
$$

✅ **Entropy(Middle_aged) = 0**

---

### (c) Entropy(Senior)

* Yes = 3
* No = 2

$$
p_{Yes} = \frac{3}{5}, \quad p_{No} = \frac{2}{5}
$$

$$
Entropy(Senior) = -\frac{3}{5}\log_2\frac{3}{5} - \frac{2}{5}\log_2\frac{2}{5}
$$

$$
Entropy(Senior) = -(0.6)(-0.737) - (0.4)(-1.322)
$$

$$
Entropy(Senior) = 0.4422 + 0.5288 = 0.971
$$

✅ **Entropy(Senior) = 0.971**

---

## Step 3: Expected Entropy for Age

Formula:

$$
Entropy_{Age}(D) = \sum_{v \in Age} \frac{|D_v|}{|D|} \times Entropy(D_v)
$$

Substitute values:

$$
Entropy_{Age}(D) = \frac{5}{14}(0.971) + \frac{4}{14}(0) + \frac{5}{14}(0.971)
$$

$$
Entropy_{Age}(D) = \frac{9.71}{14} = 0.694
$$

✅ **Entropy(_{Age}(D)) = 0.694**

---

## Step 4: Information Gain formula

$$
Gain(A) = Entropy(D) - Entropy_A(D)
$$

Given:

$$
Entropy(D) = 0.940
$$

Substitute:

$$
Gain(Age) = 0.940 - 0.694
$$

$$
Gain(Age) = 0.246
$$

---

## ✅ Final Answer (Exam-ready)

* **Entropy(Youth) = 0.971**
* **Entropy(Middle_aged) = 0**
* **Entropy(Senior) = 0.971**
* **Expected Entropy(Age) = 0.694**
* **Information Gain(Age) = 0.246**
