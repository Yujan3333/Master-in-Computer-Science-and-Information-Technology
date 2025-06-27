
## 🔍 Is a Perceptron always a **single neuron**?

### ✅ **Yes, the "original perceptron" refers to a single neuron.**

* Invented by **Frank Rosenblatt** in 1958
* It performs **binary classification**
* Takes **multiple inputs**, multiplies by **weights**, adds **bias**, and applies **activation** (usually sign function)

$$
y = \text{sign}(w \cdot x + b)
$$

So when people say "**the perceptron**," they usually mean **a single-layer, single-neuron model** used to classify inputs into **two classes** (+1 or −1).

---

## 🔁 But you can have **multiple perceptrons** in a layer

* If you want to classify into **more than 2 classes**, you can have:

  * **One perceptron per class**
  * This becomes a **single-layer neural network** with **multiple output neurons**

  Example:

  * For classifying into 3 classes (A, B, C), you can use:

    $$
    \text{Output: } [y_A, y_B, y_C]
    $$

  Each output neuron is a **perceptron**.

---

## 🧠 Key Terms:

| Term                            | Meaning                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------- |
| **Perceptron**                  | A single neuron with hard threshold (e.g., sign)                                       |
| **Single-layer perceptron**     | One layer of perceptrons; can have **many neurons**                                    |
| **Multilayer perceptron (MLP)** | More than one layer (i.e., with hidden layers); uses **sigmoid, ReLU**, etc., not sign |

---

## 📌 Summary

* A **perceptron** is a **single neuron**
* A **network of perceptrons** is a **single-layer neural network**
* If you **stack layers**, you get **MLP (multilayer perceptron)**
