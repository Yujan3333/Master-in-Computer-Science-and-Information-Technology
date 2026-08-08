#first-semester #advanced-operating-system

## ⚙️ **Three Levels of QoS**

---

### 1. **Best-effort Service**

- The system tries its best to deliver data or service.
    
- **No guarantees** on speed, latency, or delivery.
    
- Used in normal internet browsing or email.
    

---

### 2. **Soft QoS**

- Traffic streams get **prioritized** (some data is treated more important).
    
- Still **no strict guarantees** — performance can vary.
    
- Example: Video calls may get higher priority than downloads but no absolute guarantee.
    

---

### 3. **Hard QoS**

- The system **guarantees** that QoS requirements are met.
    
- Ensures things like:
    
    - Guaranteed bandwidth
        
    - Maximum latency (delay) limits
        
    - Reliable delivery
        
- Needed in **critical systems** like voice over IP, real-time control, or medical devices.
    

---

### ⚙️ **Mechanisms for Hard QoS**

- **Prioritization**: Assign priority levels to traffic
    
- **Admission Control**: Decide whether to accept a new traffic stream based on resources
    
- **Bounded Latency**: Make sure delays in interrupts and processing never exceed limits
    

---

### 🧠 **Summary**

|QoS Level|Guarantees|Usage Example|
|---|---|---|
|**Best-effort**|None|Regular web browsing|
|**Soft QoS**|Prioritization only|Streaming video or voice|
|**Hard QoS**|Strict guarantees|Real-time control systems|