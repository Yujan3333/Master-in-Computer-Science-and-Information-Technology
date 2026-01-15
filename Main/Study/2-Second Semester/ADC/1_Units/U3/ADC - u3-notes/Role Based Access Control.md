
## **Role-Based Access Control (RBAC)**

**1. Concept and Emergence**

* RBAC became widely used in the 1990s for managing security in large-scale enterprise systems.
* **Core idea:** Permissions are assigned to **roles**, and users are assigned to the appropriate **roles**.
* **Role management commands:**

  * `CREATE ROLE` – to create a new role.
  * `DESTROY ROLE` – to remove a role.
  * `GRANT` / `REVOKE` – assign or revoke privileges to/from roles.

**2. Advantages over DAC and MAC**

* RBAC is a **viable alternative** to Discretionary Access Control (DAC) and Mandatory Access Control (MAC).
* Ensures that **only authorized users** access specific data or resources.
* Provides a **role hierarchy**, reflecting organizational authority and responsibility.

**3. Advanced RBAC Features**

* **Temporal constraints:**

  * Limit roles by **time** or **duration of activation**.
  * Enable **timed triggering** of roles based on activation of other roles.
* Highly suitable for **web-based applications**, where dynamic and scalable access control is needed.

---

## **Access Control in E-Commerce Environments**

**1. New Requirements**

* Resources include **data, knowledge, and experience** – beyond traditional DBMS data.
* Access control must be **flexible** for **heterogeneous protection objects**.
* Need for **content-based access control**.

**2. User Heterogeneity**

* Users have varying **characteristics** and **qualifications**.
* Policies should be **user-profile aware**, using **credentials**.

  * A credential is a set of **properties of a user** relevant to security (e.g., age, position).

**3. Role of XML**

* XML can be instrumental in defining and enforcing access control policies for e-commerce applications.

---

### **Key Takeaways**

* RBAC is **structured, scalable, and hierarchical**, making it ideal for enterprise and web applications.
* Traditional DAC/MAC models are **less suitable** for dynamic and heterogeneous environments.
* E-commerce access control requires **flexibility, user-centric policies, and advanced object protection**.
* Credentials and XML-based policies provide a **modern solution** for these requirements.

---
