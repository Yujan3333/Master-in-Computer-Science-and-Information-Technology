#first-semester #advanced-operating-system


| Feature             | **SLED (Single Large Expensive Disk)**            | **RAID (Redundant Array of Inexpensive Disks)**                   |
| ------------------- | ------------------------------------------------- | ----------------------------------------------------------------- |
| **Full Form**       | Single Large Expensive Disk                       | Redundant Array of Inexpensive (or Independent) Disks             |
| **Concept**         | Uses **one large, high-quality disk** for storage | Combines **multiple small, cheap disks** to act as one unit       |
| **Performance**     | Moderate                                          | Can offer **higher performance** (due to parallel access)         |
| **Cost**            | **Expensive per GB**                              | **Cheaper per GB** (uses commodity hardware)                      |
| **Reliability**     | If the disk fails, **all data is lost**           | **High reliability**, depending on RAID level (due to redundancy) |
| **Scalability**     | **Limited**                                       | **Highly scalable** (disks can be added)                          |
| **Fault Tolerance** | ❌ None                                            | ✅ Varies by RAID level (e.g., RAID 1, 5, 6)                       |
| **Usage**           | Older systems, special-purpose hardware           | Modern servers, cloud storage, data centers                       |

#### Mnemonics
FC-Reliable-PC-U-SF
- Football Club in Reliable PC U are my SF (Center Forward)