## 🧠 PRAM Memory Access Models
- EREW
- CREW
- ERCW
- CRCW
---


| Model                                          | Read Access                                     | Write Access                                 | Meaning                                     | Use Case / Notes                                                       |
| ---------------------------------------------- | ----------------------------------------------- | -------------------------------------------- | ------------------------------------------- | ---------------------------------------------------------------------- |
| **EREW**<br>(Exclusive Read Exclusive Write)   | ❌ Only one processor can read a cell at a time  | ❌ Only one processor can write at a time     | **Most restrictive and realistic**          | Must avoid all memory conflicts                                        |
| **CREW**<br>(Concurrent Read Exclusive Write)  | ✅ Many processors can read the same memory cell | ❌ Only one can write to a cell               | **More flexible** — used in many algorithms | Writing must be carefully managed                                      |
| **ERCW**<br>(Exclusive Read Concurrent Write)  | ❌ Only one processor can read a memory cell     | ✅ Multiple can write to the same memory cell | 👎 **Rare and impractical**                 | Not studied seriously because reading is more fundamental than writing |
| **CRCW**<br>(Concurrent Read Concurrent Write) | ✅ Many processors can read a cell               | ✅ Many can write to the same cell            | **Most powerful but complex to manage**     | Needs rules to handle **write conflicts**                              |

---

## ⚠️ CRCW Conflict Resolution Rules

When **multiple processors write to the same memory cell at the same time**, different **conflict resolution rules** can be used:

| Rule          | Meaning                                                                       |
| ------------- | ----------------------------------------------------------------------------- |
| **Common**    | All processors must be writing the **same value** — otherwise, error          |
| **Priority**  | The processor with the **highest or lowest ID** wins and its value is written |
| **Arbitrary** | Any one of the competing writes is chosen (randomly or arbitrarily)           |

---

## 💡 Practical Insights:

* **EREW** is safest but often requires extra work to avoid conflicts (more logic and copying).
* **CREW** is widely used because concurrent reads are realistic.
* **CRCW** is powerful for **theoretical lower bounds** (e.g., constant-time operations), but not always realistic in hardware.
* **ERCW** is usually ignored in theory and practice.

---
