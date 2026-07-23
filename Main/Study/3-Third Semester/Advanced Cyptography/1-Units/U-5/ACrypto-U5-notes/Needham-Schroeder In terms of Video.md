#advanced-cryptography #needham-schroeder #third-semester 

![](../../../../../../../Images/Third_Sem_Images/Needham-Schroeder%20In%20terms%20of%20Video.png)
## **Entities Involved**

* **Initiator A**
* **Key Distribution Center (KDC)**
* **Responder B**

---

## **Protocol Steps**

### **Step 1: Initiator A $\rightarrow$ KDC**

$$1. \ \text{ID}_A \parallel \text{ID}_B \parallel N_1$$

> **Explanation:** Initiator $A$ sends a request to the KDC containing its identity ($\text{ID}_A$), Responder $B$'s identity ($\text{ID}_B$), and a unique nonce ($N_1$).

---

### **Step 2: KDC $\rightarrow$ Initiator A**

$$2. \ E\left(K_a, [K_s \parallel \text{ID}_A \parallel \text{ID}_B \parallel N_1]\right) \parallel E\left(K_b, [K_s \parallel \text{ID}_A]\right)$$

> **Explanation:** The KDC generates a session key ($K_s$) and sends it back to $A$ encrypted with $A$'s master key ($K_a$), along with a ticket encrypted with $B$'s master key ($K_b$).

---

### **Step 3: Initiator A $\rightarrow$ Responder B**

$$3. \ E\left(K_b, [K_s \parallel \text{ID}_A]\right)$$

> **Explanation:** Initiator $A$ forwards the encrypted ticket to Responder $B$.

---

### **Step 4: Responder B $\rightarrow$ Initiator A**

$$4. \ E(K_s, N_2)$$

> **Explanation:** Responder $B$ decrypts the ticket to obtain $K_s$, generates a new nonce ($N_2$), encrypts it with $K_s$, and sends it to $A$.

---

### **Step 5: Initiator A $\rightarrow$ Responder B**

$$5. \ E(K_s, f(N_2))$$

> **Explanation:** Initiator $A$ applies a function $f$ to $N_2$, encrypts the result using $K_s$, and sends it back to $B$ to complete mutual authentication.