![](../../../../../../../../Images/First_Sem_Images/Numerical%20Petri%20nets.png)
## 🧾 Problem Summary

### 🍬 Vending Machine Behavior:

* **Input coins:** 5¢, 10¢
* **Outputs (candy bars):** 15¢ and 20¢ candy bars
* **Maximum coin hold:** 20¢
* Accepts up to 20¢ total and gives a candy bar when value matches 15¢ or 20¢

---

## ✅ Petri Net Design Plan

### 🔹 **Places** (represent coin total held):

Let’s represent different total coin values as **places**:

* `P0` = 0¢ (initial state)
* `P5` = 5¢
* `P10` = 10¢
* `P15` = 15¢
* `P20` = 20¢

### 🔹 **Transitions** (events):

* **Coin insertions:**

  * `T5`: insert 5¢
  * `T10`: insert 10¢

* **Candy dispense:**

  * `T15C`: dispense 15¢ candy bar
  * `T20C`: dispense 20¢ candy bar

---

## 🧠 Token Movement

A **token** represents the current amount of money inserted. Transitions move the token through the places as coins are inserted.

---

## 🧩 Petri Net Components

### 🟢 Initial Marking:

* One token at `P0` (machine starts at 0¢)

### 🔹 Insert Coin Transitions:

| From  | Coin | To    | Transition |
| ----- | ---- | ----- | ---------- |
| `P0`  | 5¢   | `P5`  | `T5`       |
| `P0`  | 10¢  | `P10` | `T10`      |
| `P5`  | 5¢   | `P10` | `T5`       |
| `P5`  | 10¢  | `P15` | `T10`      |
| `P10` | 5¢   | `P15` | `T5`       |
| `P10` | 10¢  | `P20` | `T10`      |
| `P15` | 5¢   | `P20` | `T5`       |

> Any attempt to exceed 20¢ is **disallowed** (i.e., no transition)

---

### 🍬 Candy Bar Transitions:

| From  | Value | To   | Transition |
| ----- | ----- | ---- | ---------- |
| `P15` | 15¢   | `P0` | `T15C`     |
| `P20` | 20¢   | `P0` | `T20C`     |

These transitions **reset** the machine by consuming the token and placing it back at `P0`.

---

## 🖼️ Diagram Suggestion (You can draw like this):

```
[P0] --T5--> [P5] --T5--> [P10] --T5--> [P15] --T5--> [P20]
  |            |           |           |             |
 T10          T10         T10         T10         (no more coins allowed)
  |            |           |           |
[P10]       [P15]       [P20]       [BLOCK]

[P15] --T15C--> [P0]
[P20] --T20C--> [P0]
```

* Circles = places (P0, P5, ...)
* Boxes = transitions (T5, T10, T15C, ...)
* Arrows = token flow

---

## ✅ Summary

> The Petri Net simulates a vending machine that accepts 5¢ and 10¢ coins, keeps track of total value up to 20¢, and sells candy bars worth 15¢ or 20¢.
> The **transitions** represent inserting coins and vending candy, and the **places** represent current total inserted value.
> A **token** moves through the network to simulate coin accumulation and candy purchase.

---
