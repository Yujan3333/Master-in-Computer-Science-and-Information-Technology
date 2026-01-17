
| Feature           | **Inmon Approach**                              | **Kimball Approach**                   |
| ----------------- | ----------------------------------------------- | -------------------------------------- |
| Basic Type        | Top–down                                        | Bottom–up                              |
| First Step        | Build **Enterprise Data Warehouse (EDW)** first | Build **Data Marts** first             |
| Data Model        | Normalized (3NF)                                | Dimensional (Star/Snowflake schema)    |
| Focus             | Enterprise-wide integration                     | Business process and user requirements |
| Data Marts        | Created from EDW                                | Integrated together to form DW         |
| Development Speed | Slow                                            | Fast                                   |
| Initial Cost      | High                                            | Low                                    |
| Complexity        | High                                            | Moderate                               |
| Flexibility       | Less flexible                                   | More flexible                          |
| Query Performance | Moderate                                        | Very fast (optimized for OLAP)         |
| Data Consistency  | Very strong                                     | Depends on conformed dimensions        |
| User Friendliness | Less user-friendly                              | Highly user-friendly                   |
