
### **Hoare Triple in Concurrent Programming**

The Hoare triple **`{P} S {Q}`** still holds, but with additional considerations:

|Part|Meaning|
|---|---|
|`P`|**Precondition** — what must be true **before** `S` runs|
|`S`|**Statement or Program** — code being executed|
|`Q`|**Postcondition** — what must be true **after** `S` runs|

> "If the precondition `P` is true before executing statement `S`, and `S` runs correctly (terminates), then the postcondition `Q` will be true afterwards."

---
### [Numerical of Sir Slide](Numerical%20of%20Sir%20Slide.md)
