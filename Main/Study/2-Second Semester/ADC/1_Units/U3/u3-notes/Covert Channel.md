
## **Covert Channels**

**1. Definition**

* A **covert channel** is a method of transferring information that **violates security policy**.
* Specifically, it allows information to pass from a **higher classification level** to a **lower classification level** through **improper or unintended means**.

**2. Types of Covert Channels**

| Type                | Description                                                                                                                |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Storage channel** | Information is conveyed by **accessing system objects or storage locations**. Does **not require timing synchronization**. |
| **Timing channel**  | Information is conveyed through the **timing of events or processes**.                                                     |

**3. Prevention Measures**

* One suggested approach: prevent programmers or processes from **directly accessing sensitive data** after the program is operational.
* Proper system design and access restrictions help **reduce covert channel risks**.

---

### **Key Takeaways**

* Covert channels **bypass normal security controls**.
* They can leak information **without explicit permission**.
* **Storage channels** rely on system state; **timing channels** rely on event timing.
* Prevention requires careful **program and system design**.

---

