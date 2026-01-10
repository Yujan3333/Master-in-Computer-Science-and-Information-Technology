Attributes can be classified based on the type of values they take into four main types:

1. **Nominal Attributes**

* Values are names, symbols, or categories.
* No meaningful order exists among them.
* Numbers can be used as codes, but they have **no quantitative meaning(*cannot be used in add, sub etc*)**.
* Only **mode(*most frequently occurring value*)** can be calculated.

Examples:

* Hair_color = {black, brown, red, grey, white}
* Marital_status = {Married, Single, Divorced, Widowed}
* Customer_ID

---

2. **Ordinal Attributes**

* Values have a meaningful **order or ranking**.
* The difference between values is not measurable.
* Median and mode can be calculated, but **mean cannot**.

Examples:

* Grades = {A+, A, A−, B+, B, B−, …}
* Height = {Tall, Medium, Short}

Nominal and ordinal attributes are **qualitative** (descriptive, not numeric).

---

3. **Interval-Scaled Attributes**

* Numeric attributes with meaningful order and measurable differences.
* No true zero-point.
* Cannot express values as ratios (no “twice as much”).
* Mean, median, and mode can be calculated.

Examples:

* Temperature in Celsius or Fahrenheit
* Calendar dates

Reason:
0°C does not mean “no temperature,” so 20°C is not twice as hot as 10°C.

---

4. **Ratio-Scaled Attributes**

* Numeric attributes with a **true zero-point**.
* Allow comparison using ratios.
* All statistical measures can be computed (mean, median, mode, differences, ratios).

Examples:

* Temperature in Kelvin
* Length, weight, height
* Counts, elapsed time

---

### Quick Comparison Table

| Attribute Type | Order | Difference | True Zero | Ratios Possible | Measures           |
| -------------- | ----- | ---------- | --------- | --------------- | ------------------ |
| Nominal        | ❌     | ❌          | ❌         | ❌               | Mode               |
| Ordinal        | ✔️    | ❌          | ❌         | ❌               | Median, Mode       |
| Interval       | ✔️    | ✔️         | ❌         | ❌               | Mean, Median, Mode |
| Ratio          | ✔️    | ✔️         | ✔️        | ✔️              | All statistics     |
