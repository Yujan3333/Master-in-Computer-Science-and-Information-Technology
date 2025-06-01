- **RDD** is about _defining_ what objects do and how they interact based on their roles.
	- Designing objects based on their responsibilities, collaborations, and contracts rather than focusing primarily on data or hierarchy.

	- It uses a client-server model where objects fulfill responsibilities and collaborate to achieve system goals.

- Popularized by **Rebecca Wirfs-Brock**

## Process
- Involves identifying candidate objects, assigning responsibilities to them, and defining how they collaborate with other objects to fulfill those responsibilities. 
- *CRC (Class-Responsibility-Collaborator)* cards are a key technique used in RDD to explore and document these aspects

## Strengths
- Promotes strong *encapsulation* by focusing on an object's public interface (its responsibilities) rather than its internal data structure.
- Promotes loose coupling 
- high cohesion 
- clear separation of concerns

## Limitations
- May require a shift in thinking for developers accustomed to data-centric or hierarchical approaches. 

- The focus on responsibilities might sometimes make it less immediately obvious how to structure the overall system architecture compared to HOOD.