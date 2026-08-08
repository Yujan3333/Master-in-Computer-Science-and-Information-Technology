#first-semester #advanced-operating-system

| **Aspect**         | **Multiprogramming OS**                                                                                  | **Multiprocessing OS**                                                                      |
| ------------------ | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Definition**     | OS that supports **multiple programs** in memory and executes them one by one using **CPU time-sharing** | OS that supports the use of **multiple processors** for simultaneous execution of processes |
| **CPU**            | Uses a **single CPU**                                                                                    | Uses **two or more CPUs**                                                                   |
| **Execution**      | Executes **one process at a time**, switching between programs when one waits for I/O                    | Executes **multiple processes in parallel**, each on a separate CPU/core                    |
| **Goal**           | Maximize **CPU utilization** and minimize idle time by overlapping CPU and I/O operations                | Achieve **faster execution**, **load sharing**, and **fault tolerance**                     |
| **Concurrency**    | **Pseudo-concurrent** execution via context switching                                                    | **True concurrent** execution using multiple CPUs                                           |
| **Complexity**     | Less complex to implement                                                                                | More complex due to inter-CPU communication, synchronization, and scheduling                |
| **System Example** | Early UNIX systems, MS-DOS with TSRs (Terminate and Stay Resident)                                       | Modern OS like Linux, Windows Server, and macOS on multi-core systems                       |
| **Use Case**       | Best for systems with limited hardware (e.g., single-core PCs)                                           | Best for high-performance systems like servers, scientific computing, and data centers      |

Mnenomics
- DCE - GC - Example