
| Feature                  | Internal Hashing                                     | External Hashing                                                            |
| ------------------------ | ---------------------------------------------------- | --------------------------------------------------------------------------- |
| **Where used**           | In-memory data structures                            | Disk-based files                                                            |
| **Data size**            | Small datasets that fit in main memory               | Large datasets that may not fit in memory                                   |
| **Structure**            | Hash table (array)                                   | Buckets (one or more disk blocks per bucket)                                |
| **Hash function output** | Maps key to array index (0 to M-1)                   | Maps key to bucket number (0 to M-1)                                        |
| **Collision handling**   | Open addressing, chaining, multiple hashing          | Overflow buckets/files, chaining, sometimes dynamic hashing                 |
| **Access speed**         | Very fast (RAM access)                               | Slower (disk I/O involved)                                                  |
| **Scalability**          | Limited; resizing hash table is costly               | Can handle large files; dynamic hashing allows growth/shrinkage             |
| **Ordering**             | Not suitable for ordered access                      | Not inherently suitable; needs extra sorting for ordered access             |
| **Typical usage**        | Temporary tables, internal buffers, in-memory caches | Database tables, large disk-based datasets                                  |
| **Capacity management**  | Keep load factor ~70–80% to avoid collisions         | Buckets and overflow files handle collisions; dynamic hashing for expansion |
