
| Aspect              | Parallel Database System                                  | Distributed Database System                                           |
| ------------------- | --------------------------------------------------------- | --------------------------------------------------------------------- |
| Basic idea          | Uses multiple processors/memory to execute queries faster | Data is stored at different geographical sites connected by a network |
| Location            | Usually in a single location                              | Spread across multiple locations                                      |
| Main goal           | Improve performance and speed                             | Improve availability, reliability, and locality                       |
| Data storage        | Data is stored centrally but processed in parallel        | Data is physically distributed among sites                            |
| Communication       | Fast inter-processor communication                        | Network communication, slower and failure-prone                       |
| Failure handling    | Failure affects whole system                              | Failure of one site should not stop the whole system                  |
| Concurrency control | Simpler, centralized control                              | More complex, needs distributed control                               |
| Commit protocol     | Normal commit                                             | Requires distributed commit (2PC, 3PC)                                |
| Transparency        | Looks like a single DB system                             | Should appear as a single DB to the user                              |
| Cost                | High hardware cost                                        | High network and management cost                                      |
