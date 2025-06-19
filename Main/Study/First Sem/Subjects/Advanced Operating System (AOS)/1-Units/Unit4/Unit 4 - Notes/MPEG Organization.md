## 🎞️ **MPEG Frame Types**

---

### 1. **I-Frame (Intra-coded Frame)**

- Complete, **independent frame** (like a JPEG image)
    
- Contains **all image data** for that frame
    
- Used as a **reference point** for other frames
    
- Occurs every second or at scene changes
    
- **Biggest size** among the three frames
    

---

### 2. **P-Frame (Predictive Frame)**

- Encodes **only the changes** (differences) from the **previous I- or P-frame**
    
- Smaller than I-frames since it stores **less data**
    
- Depends on previous frames to be decoded
    

---

### 3. **B-Frame (Bidirectional Frame)**

- Stores differences **using both previous and next frames**
    
- Most compressed/smallest size
    
- Depends on both past and future frames to decode
    

---

## 🧠 **Why These Frames?**

- This structure **reduces video size** drastically by avoiding storing full frames every time.
    
- I-frames give full info, P- and B-frames only store changes.
    

---

### 🔄 **Frame Order Example:**

I — B — B — P — B — B — P — I — …