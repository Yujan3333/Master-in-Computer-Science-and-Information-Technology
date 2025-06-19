What are the types of security breaches ? Define different levels of protection of OS?

## 🔓 **Types of Security Breaches**

Security breaches occur when unauthorized users gain access to data or system resources. These can be classified as:

### 1. **Breach of Confidentiality**

- Unauthorized access to **private data**.
    
- 📌 Example: Reading another user’s emails or files.
    

### 2. **Breach of Integrity**

- Unauthorized **modification of data** or programs.
    
- 📌 Example: Tampering with system logs or financial records.
    

### 3. **Breach of Availability**

- Disrupting the system so that **legitimate users can’t access** services or data.
    
- 📌 Example: Denial of Service (DoS) attacks.
    

### 4. **Breach of Authenticity**

- **Impersonating** another user or system.
    
- 📌 Example: Logging in using someone else’s credentials.
    

### 5. **Breach of Authorization**

- Gaining access to **resources or actions beyond one's privileges**.
    
- 📌 Example: A normal user executing admin-only commands.
    

---

## 🛡️ **Levels of Protection in Operating Systems**

Operating systems use several **layers of protection** to guard against these breaches:

---

### 🔑 **1. Physical Security**

- Protects the **hardware** from tampering.
    
- 📌 Example: Locked server rooms, surveillance, access cards.
    

---

### 🧾 **2. Human/User Security**

- Focuses on **authorized personnel only** using the system.
    
- 📌 Example: Strong passwords, two-factor authentication (2FA), training users against phishing.
    

---

### 🔐 **3. Network Security**

- Protects against **external attacks** via the internet or LAN.
    
- 📌 Example: Firewalls, intrusion detection systems (IDS), encryption.
    

---

### 💾 **4. OS-Level Security**

- Built-in OS mechanisms to protect **resources**.
    

|Component|Role|
|---|---|
|**Authentication**|Verifies identity (e.g., login credentials)|
|**Authorization**|Grants rights based on roles (e.g., file permissions)|
|**Access Control**|Manages who can do what (e.g., ACLs, capabilities)|
|**Auditing**|Keeps logs of actions for accountability|

---

### 🛠️ **5. Application-Level Security**

- Secures individual programs or services.
    
- 📌 Example: Sandboxing browsers, setting file permissions in apps.
    

---

### ✅ **Summary Table**

|Security Breach Type|Description|
|---|---|
|Confidentiality|Data leakage|
|Integrity|Unauthorized data change|
|Availability|Denial of access to resources|
|Authenticity|Identity forgery|
|Authorization|Privilege misuse|

| OS Protection Level | Focus                                   |
| ------------------- | --------------------------------------- |
| Physical            | Hardware access control                 |
| Human               | User behavior & authentication          |
| Network             | Communication security                  |
| OS-Level            | Internal resource access control        |
| Application         | App-specific restrictions and isolation |