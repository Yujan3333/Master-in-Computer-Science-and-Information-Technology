## ⚙️ **QoS Negotiation and Admission Control**
   
   ---
   
   ### ✅ **QoS Negotiation**
   
   - **Client and server agree** on the quality level for a service (like video streaming).
       
   - Negotiation happens **before starting** the service.
       
   - Ensures both sides understand the resource needs and limits.

---

### ✅ **Admission Control**

- The operating system or server **checks if it has enough resources** (CPU, bandwidth, memory) to handle the request.
    
- **If yes:** The request is accepted, and QoS guarantees can be met.
    
- **If no:** The request is rejected or delayed to avoid degrading existing services.
    

---

### 🧠 **Why Admission Control is Important**

- Prevents **overloading** the system.
    
- Maintains **quality for existing users**.
    
- Helps **meet QoS guarantees** for accepted requests.
    

---

## 📝 **Summary**

> Before providing service, the system negotiates QoS and only admits requests if resources are available, ensuring reliable and consistent quality.