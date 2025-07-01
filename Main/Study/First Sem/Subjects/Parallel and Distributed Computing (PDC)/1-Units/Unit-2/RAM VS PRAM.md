| Feature                      | **RAM (Random Access Machine)**                   | **PRAM (Parallel RAM)**                                               |
| ---------------------------- | ------------------------------------------------- | --------------------------------------------------------------------- |
| **Type**                     | Sequential computation model                      | Parallel computation model                                            |
| **Processors**               | Single processor                                  | Multiple processors                                                   |
| **Memory**                   | Single memory unit                                | Shared memory accessible by all processors                            |
| **Execution**                | One instruction at a time                         | Multiple instructions simultaneously (in parallel)                    |
| **Concurrency**              | No concurrency                                    | High concurrency (parallel execution)                                 |
| **Use Case**                 | Used to model traditional single-threaded systems | Used to model parallel algorithms and theoretical speedup             |
| **Access Conflict Handling** | Not applicable                                    | Different PRAM models handle conflicts differently (EREW, CREW, CRCW) |
