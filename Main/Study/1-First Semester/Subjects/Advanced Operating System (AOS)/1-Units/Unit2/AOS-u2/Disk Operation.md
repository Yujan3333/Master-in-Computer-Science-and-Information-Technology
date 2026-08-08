#first-semester #advanced-operating-system
## 🧭 Disk Access Time Components
![](../../../../../../../../Images/First_Sem_Images/Disk%20Operation-disk%20access%20time.png)

To access data on a disk, the OS must coordinate **three main actions**:

---

### 🔹 1. Seek Time

> **Time to move the read/write head to the correct cylinder.**

- Controlled by the **arm assembly**.
    
- Usually the **largest** component of disk access time.
    
- Faster seeks = better performance.
    

---

### 🔹 2. Rotational Latency (Latency Time)

> **Time for the disk to rotate the desired sector under the read/write head.**

- Average latency ≈ **half a full rotation**.
    
- Depends on **rotation speed** of the disk (e.g., 7200 RPM).
    

---

### 🔹 **3. Transmission Time**

> **Time to actually read/write the data once the head is in position.**

- Starts after seek + latency are complete.
    
- Depends on **data transfer rate**.
    

---

### 📌 **Accessing a Record**

To access a record:

1. Move arm to the correct **cylinder** → **Seek Time**
    
2. Wait for sector to rotate under the head → **Latency Time**
    
3. Read the data → **Transmission Time**
    

---

### 🧠 Key Insight

> **Seek time dominates** overall access time on most disks.  
> So, **minimizing seek time** (e.g., through good disk scheduling) significantly **improves performance**.

---

### ✅ Summary Line for Exams:

> Disk access time = **Seek Time + Latency Time + Transmission Time**  
> Seek time is the most significant, and OS aims to reduce it using scheduling.
