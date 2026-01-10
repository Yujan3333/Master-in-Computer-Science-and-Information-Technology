![](../../../../../../../Images/Second_Sem_Images/Multiclass%20Classification-1.png)

---
I'll help you find the TP, FP, FN, and TN for each class from this confusion matrix.

## 📊 **Confusion Matrix Structure**
From your data, it appears to be a **3×3 confusion matrix**:

| | **Actual A** | **Actual B** | **Actual C** | **Total Predicted** |
|---|---|---|---|---|
| **Predicted A** | 2 | 2 | 0 | 4 |
| **Predicted B** | 1 | 2 | 0 | 3 |
| **Predicted C** | 0 | 0 | 3 | 3 |
| **Total Actual** | 3 | 4 | 3 | **10** |

---

## 🧮 **Calculations for Each Class**

### **For Class A:**
- **TP (True Positive)** = 2 (A predicted as A)
- **FP (False Positive)** = 2 (B predicted as A) + 0 (C predicted as A) = 2
- **FN (False Negative)** = 1 (A predicted as B) + 0 (A predicted as C) = 1
- **TN (True Negative)** = All other correct predictions = 2 (B as B) + 0 + 0 + 3 (C as C) = **5**
  *Alternatively: Total - (TP+FP+FN) = 10 - (2+2+1) = 5*

### **For Class B:**
- **TP** = 2 (B predicted as B)
- **FP** = 2 (B predicted as A) + 0 (B predicted as C) = 2
- **FN** = 1 (B predicted as A? Wait check: Actually, B was predicted as A 2 times, but that's FP for A, not FN for B. Let me recalculate.)  
  Looking at **Actual B column**: Predicted as A (2), Predicted as B (2), Predicted as C (0)  
  So **FN for B** = Predicted as A (2) + Predicted as C (0) = 2
- **TN** = Correct predictions for non-B = 2 (A as A) + 0 + 0 + 3 (C as C) = **5**


---

## ✅ **Correct Calculations:**

**Total instances = 10**

### **Class A:**
- **TP** = 2 (A→A)
- **FP** = (A predicted as B=1) + (A predicted as C=0) = **1**? No, that's wrong.

Actually, **FP for class A** = All predictions as A that were NOT actually A =  
From Predicted A row: 2 (were B) + 0 (were C) = **2**

**FN for class A** = All actual A that were predicted as NOT A =  
From Actual A column: 1 (predicted as B) + 0 (predicted as C) = **1**

**TN for class A** = All cases that were NOT A and were NOT predicted as A =  
Total - (TP + FP + FN) = 10 - (2 + 2 + 1) = **5**

---

### **Class B:**
- **TP** = 2 (B→B)
- **FP** = All predictions as B that were NOT actually B =  
  From Predicted B row: 1 (was A) + 0 (was C) = **1**
- **FN** = All actual B that were predicted as NOT B =  
  From Actual B column: 2 (predicted as A) + 0 (predicted as C) = **2**
- **TN** = Total - (TP+FP+FN) = 10 - (2+1+2) = **5**

---

### **Class C:**
- **TP** = 3 (C→C)
- **FP** = All predictions as C that were NOT actually C =  
  From Predicted C row: 0 (were A) + 0 (were B) = **0**
- **FN** = All actual C that were predicted as NOT C =  
  From Actual C column: 0 (predicted as A) + 0 (predicted as B) = **0**
- **TN** = Total - (TP+FP+FN) = 10 - (3+0+0) = **7**

---

## 📋 **Final Results:**

| Class | TP | FP | FN | TN |
|-------|----|----|----|----|
| **A** | 2  | 2  | 1  | 5  |
| **B** | 2  | 1  | 2  | 5  |
| **C** | 3  | 0  | 0  | 7  |

---

## 🎯 **Verification:**
- **Sum of all TP** = 2+2+3 = 7 (should equal total correct predictions)
- Looking at matrix: Diagonal sum = 2+2+3 = 7 ✓
- **Sum of all cells** = 10 ✓
