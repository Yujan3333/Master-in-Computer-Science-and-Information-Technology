| Feature             | **Online Algorithm**                                  | **Offline Algorithm**                       |
| ------------------- | ----------------------------------------------------- | ------------------------------------------- |
| **Input Access**    | Receives input **step by step**                       | Has access to **entire input in advance**   |
| **Decision Making** | Must make decisions **without knowing future inputs** | Can **optimize decisions using full input** |
| **Example**         | Paging (LRU), Load Balancing, Ski Rental              | Sorting, Shortest Path (Dijkstra), Knapsack |
| **Efficiency**      | May be **less optimal** than offline                  | Often gives the **best possible solution**  |
| **Use Cases**       | Real-time systems, streaming, memory management       | Planning, optimization, batch processing    |
