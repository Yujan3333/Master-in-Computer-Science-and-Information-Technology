#first-semester #advanced-operating-system

### ✅ **What is Intrusion Detection?**

Intrusion Detection Systems (IDS) monitor computer systems or networks to **detect unauthorized access**, misuse, or anomalies that suggest an attack.

---

## 🔐 **Guarded Models – Concept Overview**

**Guarded Models** are a type of **behavioral or model-based intrusion detection** approach.  
They use a **formal model of expected (legal) behavior** of a system or user and detect **deviations** from that model.

---

## 📘 **Main Idea:**

- A **guard** monitors actions in the system.
    
- A **model** defines what behavior is **normal** (safe, permitted).
    
- If an action **violates the model**, the guard **raises an alert**.
    

---

### 🔄 **How It Works:**

1. **Define system policy/model**:
    
    - Specify legal operations, resources, access rules
        
2. **Monitor actions**:
    
    - The guard watches all system events (file access, process creation, etc.)
        
3. **Check for violations**:
    
    - If an event breaks the rules of the model ➝ **Intrusion Detected**
        

---

## 🧠 **Key Features:**

|Feature|Description|
|---|---|
|**Model-Based**|Uses formal specification of valid behavior|
|**Guard-Driven**|Guard acts as a filter/enforcer|
|**Real-Time Detection**|Monitors live actions for immediate response|
|**Policy-Oriented**|Tied to system’s access control policies|

---

## 🔎 **Types of Models Used:**

1. **State-Based Models**:
    
    - Model allowed states and transitions (like Finite State Machines)
        
2. **Access Control Models**:
    
    - Based on role-based or mandatory access rules
        
3. **Behavioral Models**:
    
    - Model usual user behavior (time of login, command patterns)
        

---

## 🧪 **Example:**

Suppose a policy says:

> “Only Admins can access `/etc/shadow`.”

If a **non-admin** tries to read it, the **guard detects this violation**, flags it as **intrusion**, and takes action (like logging or blocking).

---

## ✅ **Advantages:**

- High **accuracy** (since it uses formal models)
    
- Can detect **policy violations** in real-time
    
- Easier to **audit** and **understand behavior**
    

---

## ❌ **Disadvantages:**

- Requires **complete and correct models** (hard to build)
    
- May generate **false positives** if behavior changes
    
- Less effective against **novel attacks** not covered by the model
    

---

## 📌 **Applications:**

- Secure operating systems
    
- Network intrusion detection
    
- File and access monitoring
    
- Enforcing **role-based access policies**
    

---

## ✍️ **Paper-Based Study Focus Areas:**

| Focus                        | Description                                       |
| ---------------------------- | ------------------------------------------------- |
| **Design of Guarded Models** | How models are specified and verified             |
| **Detection Logic**          | How guards check operations against the model     |
| **Case Studies**             | Implementation examples in OS or networks         |
| **Comparison**               | Strengths vs Signature-based or Anomaly-based IDS |

---
[Paper Based Review -Guarded Models for Intrusion Detection](Paper%20Based%20Review%20-Guarded%20Models%20for%20Intrusion%20Detection.md)