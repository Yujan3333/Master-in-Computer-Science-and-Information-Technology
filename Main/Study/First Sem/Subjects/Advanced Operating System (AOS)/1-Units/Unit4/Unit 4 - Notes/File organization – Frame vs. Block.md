## 🎞️ **Frame Organization vs. Block Organization**

---

### 📁 **1. Frame Organization**

- **Disk block size**: Small (e.g., **4–16 KB**)
    
- Each **frame** is stored **individually**
    
- **Frame index**: Points to the **starting block** of each frame
    

#### ✅ **Advantages:**

- **Very little fragmentation** (frames neatly stored)
    
- Great for **random access** to individual frames (like pause/rewind)
    

#### ❌ **Disadvantages:**

- Needs a **large index table** in **RAM**
    
    - One entry **per frame**
        

---

### 📦 **2. Block Organization**

- **Disk block size**: Large (e.g., **256 KB** or more)
    
- Each block stores **multiple frames**
    
    - Usually starts with an **I-frame**
        
- **Block index**: Points to the **first frame** in each block
    

#### ✅ **Advantages:**

- **Smaller index table** in RAM (fewer entries)
    
- Good for **sequential playback**
    

#### ❌ **Disadvantages:**

- Causes **more storage fragmentation**
    
    - Some block space may be wasted
        
- Not ideal for skipping to individual frames
    

---

## 🧠 **Summary Table**

|Feature|Frame Organization|Block Organization|
|---|---|---|
|Block Size|Small (4–16 KB)|Large (256 KB+)|
|Index Points To|Each individual frame|First I-frame in block|
|RAM Usage|Large table|Small table|
|Fragmentation|Very little|More|
|Best Use Case|Random access (pause/seek)|Sequential streaming|
