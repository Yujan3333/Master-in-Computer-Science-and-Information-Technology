**Concurrent programming** is a programming technique in which **multiple tasks (or computations) are executed during overlapping time periods**, instead of sequentially. 

These tasks can start, run, and complete in overlapping time frames, which improves responsiveness and efficiency — especially on systems with **multiple processors or cores**.

| Term                    | Meaning                                                                |
| ----------------------- | ---------------------------------------------------------------------- |
| **Task/Thread/Process** | A unit of work that runs concurrently with others.                     |
| **Concurrency**         | Tasks make progress **independently**, possibly interleaving on a CPU. |
| **Parallelism**         | Tasks run **at the same time**, typically on multiple cores.           |
| **Synchronization**     | Coordination of access to shared resources (like memory).              |
| **Race condition**      | A bug that occurs when tasks access shared data **unsafely**.          |