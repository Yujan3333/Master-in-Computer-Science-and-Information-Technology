
| Basis                             | **Database**                             | **Data Warehouse**                      |
| --------------------------------- | ---------------------------------------- | --------------------------------------- |
| **1. Purpose**                    | Used for **daily operations**            | Used for **analysis & decision making** |
| **2. Main Goal**                  | Run the business                         | Analyze the business                    |
| **3. Type of Processing**         | **OLTP** (Online Transaction Processing) | **OLAP** (Online Analytical Processing) |
| **4. Users**                      | Clerks, users, applications              | Managers, analysts, decision makers     |
| **5. Type of Data**               | **Current, live data**                   | **Historical + current data**           |
| **6. Time Dimension**             | Stores **present state**                 | Stores **time-variant data**            |
| **7. Data Volume**                | Smaller (MBs–GBs)                        | Very large (GBs–TBs–PBs)                |
| **8. Data Source**                | Single application                       | Multiple databases, files, APIs         |
| **9. Data Nature**                | Highly **normalized**                    | Mostly **denormalized**                 |
| **10. Schema Design**             | ER model                                 | Star / Snowflake schema                 |
| **11. Updates**                   | Frequent INSERT, UPDATE, DELETE          | Rare updates, mostly **read-only**      |
| **12. Query Type**                | Simple, short queries                    | Complex, long analytical queries        |
| **13. Query Speed**               | Fast for transactions                    | Optimized for large scans               |
| **14. Data Consistency**          | Very strict (ACID)                       | Less strict, optimized for analysis     |
| **15. Redundancy**                | Minimal redundancy                       | Redundancy allowed                      |
| **16. Data Refresh**              | Real-time                                | Periodic (daily, weekly)                |
| **17. Example Operations**        | Add order, update customer               | Find yearly sales trend                 |
| **18. Example Tools**             | MySQL, PostgreSQL, Oracle                | Snowflake, Redshift, BigQuery           |
| **19. Index Usage**               | Limited indexes                          | Heavy indexing                          |
| **20. Aggregation**               | Rare                                     | Common (SUM, AVG, COUNT)                |
| **21. Join Complexity**           | Few tables                               | Many large tables                       |
| **22. Data Stability**            | Changes continuously                     | Stable once loaded                      |
| **23. Backup Strategy**           | Frequent backups                         | Large batch backups                     |
| **24. Performance Focus**         | Transaction speed                        | Query performance                       |
| **25. Data Granularity**          | Detailed, row-level                      | Summarized + detailed                   |
| **26. Failure Impact**            | High (business stops)                    | Low (analysis delayed)                  |
| **27. Typical Size of Records**   | Small                                    | Large                                   |
| **28. Security Level**            | User-level security                      | Role-based analytical access            |
| **29. Real-Time Requirement**     | Mandatory                                | Not mandatory                           |
| **30. Example Question Answered** | “What is the balance now?”               | “How did sales grow in 5 years?”        |
