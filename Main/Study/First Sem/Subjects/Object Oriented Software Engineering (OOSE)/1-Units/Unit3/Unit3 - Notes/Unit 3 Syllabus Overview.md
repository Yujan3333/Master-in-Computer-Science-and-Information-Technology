- [Brief](Brief.md)
### Unit 3: Architecture, Real-Time Systems, Databases, Components, and Testing (Based on Ivar Jacobson's Textbook)
#### 1. Architecture - Model Architecture, Requirements, Analysis, Design, Implementation, and Test Model

Jacobson's Objectory methodology emphasizes a model-driven approach, where the architecture of the system evolves through a series of interconnected models. The "model architecture" refers to how these distinct models form a comprehensive view of the system throughout its lifecycle.

- **Model Architecture:** Objectory structures the software development process around several key models that represent different views or levels of abstraction of the system:
    - **Requirements Model:** Captures the functional requirements, primarily through **use cases**, defining what the system should do from the user's perspective. This forms the initial architectural understanding based on external behavior.
    - **Analysis Model:** Transforms the requirements into a conceptual object model, identifying problem-domain objects (entity, boundary, control objects) and their relationships. This starts to define the logical architecture.
    - **Design Model:** Refines the analysis model into a detailed solution-domain design, considering implementation constraints, architectural patterns, and technology choices. This is where the concrete software architecture (e.g., layers, subsystems, component interfaces) is defined.
    - **Implementation Model (or Construction):** Represents the actual executable code and physical structure of the system, directly derived from the design model. This is the realization of the architectural plan.
    - **Test Model:** Focuses on verifying and validating the system against the requirements and design, often using test cases derived directly from use cases. The test model is intrinsically linked to the architecture, as testing often validates architectural decisions.
- **Architectural Significance:** In Objectory, architecture is not a separate phase but rather an evolving aspect refined through these models. A well-defined model architecture ensures consistency, traceability, and manageability throughout the development lifecycle.

#### 2. Analysis

As previously discussed, **Object-Oriented Analysis (OOA)** in Jacobson's book is a critical phase following requirements capture.

- **Purpose:** To build a robust, conceptual, object-oriented model of the system based on the use cases. It aims to deeply understand the problem domain and represent it using object concepts, independent of specific implementation technologies.
- **Key Deliverables:** The **Analysis Model**, composed of **Boundary, Entity, and Control objects**, which together describe the system's responsibilities and interactions from a logical perspective.
- **Use Case Driving:** The analysis process is fundamentally driven by the use cases, ensuring that the object model directly supports the system's required functionalities.

#### 3. Construction

In Objectory, "Construction" refers to the phase where the design model is translated into executable software components.

- **Implementation Model:** This phase involves writing the actual code for the classes and objects defined during the design phase. It's the physical realization of the system's architecture and design.
- **Focus:** Ensuring that the code accurately reflects the design, adhering to object-oriented programming principles like encapsulation, inheritance, and polymorphism. It involves writing methods, defining attributes, and implementing object interactions.

#### 4. Real-time - Classification of Real-Time Systems

While Jacobson's book "Object-Oriented Software Engineering: A Use Case Driven Approach" provides a general framework for large-scale industrial systems, it might not delve into a detailed academic classification of real-time systems. However, Objectory is designed to be applicable to complex systems, which can include real-time aspects.

- **Objectory's Applicability:** Objectory, with its emphasis on concurrent objects and robust modeling, can be adapted for real-time applications. The use of control objects and interaction diagrams (which can represent message passing and synchronization) supports the modeling of dynamic, time-critical behaviors.
- **General Classification (not explicitly detailed in the provided snippets of this book):** Typically, real-time systems are classified based on the strictness of their deadlines:
    - **Hard Real-time Systems:** Failure to meet a deadline is catastrophic (e.g., flight control).
    - **Soft Real-time Systems:** Missing a deadline is undesirable but not catastrophic; degraded performance is acceptable (e.g., multimedia streaming).
    - **Firm Real-time Systems:** Deadlines are important, but occasional misses can be tolerated without complete system failure, though results are useless after the deadline (e.g., networked games).
- **Modeling Real-time in OO:** An object-oriented approach can help manage the complexity of real-time systems by encapsulating time-sensitive behaviors within specific objects and defining their synchronization and communication mechanisms.

#### 5. Database - RDBMS, Object DBMS

Jacobson's book, while not a database textbook, addresses the persistent storage of objects.

- **Data Persistence:** In an object-oriented system, the state of entity objects often needs to be stored persistently.
- **RDBMS (Relational Database Management Systems):** The book would likely acknowledge the prevalence of RDBMS for persistence. When using an RDBMS with an object-oriented system, an "Object-Relational Mapping (ORM)" layer is often necessary to translate between the object model and the relational database schema. This involves mapping objects to tables, attributes to columns, and relationships to foreign keys.
- **Object DBMS (Object Database Management Systems):** The book, being from 1992, would also likely discuss Object DBMS (ODBMS) as an alternative. ODBMSs are designed specifically to store and retrieve objects directly, maintaining their object identity and relationships without the need for mapping. While ODBMS had significant promise in the early days of OO, RDBMS with ORM tools became the dominant approach for most business applications.
- **Objectory's Role:** Objectory would guide the design of entity objects that need to be persistent and inform the decision on how these objects are managed by the chosen database technology, potentially through a dedicated persistence layer in the design.

#### 6. Components - Use of Components, Component Management

Jacobson's Objectory framework inherently supports the idea of building systems from well-defined, reusable parts, which aligns with component-based development.

- **Components as Building Blocks:** Objectory's emphasis on modularity, clear interfaces, and the independent evolution of parts means that objects and groups of objects can be seen as components. The Design Model in Objectory focuses on how objects collaborate and how they can be grouped into larger, cohesive units that act as components.
- **Reuse:** A core benefit of object-orientation, strongly supported by Objectory, is the reuse of software components (objects, classes, subsystems).
- **Component Management:** The book would advocate for managing these components, which includes:
    - **Version Control:** Managing different versions of components.
    - **Configuration Management:** Tracking which versions of components are used in a particular system build.
    - **Component Libraries/Repositories:** Storing and making components accessible for reuse across projects.
    - **Clear Interfaces:** Defining precise interfaces for components is crucial for their independent development and integration.

#### 7. Testing - On Testing, Unit, Integration, System, and the Testing Process

Testing is an integral and continuous part of the Objectory process, not just a final phase. Jacobson emphasizes that testing should be driven by the same artifacts (especially use cases) that drive development.

- **On Testing (General Philosophy):** Testing in Objectory is seen as a means to ensure quality, verify requirements fulfillment, and validate the system's behavior from a user's perspective. It's integrated throughout the lifecycle.
- **The Testing Process:** Objectory defines a structured testing process often tied directly to use cases. Test cases are derived from use cases, ensuring that all specified functionalities are verified.
- **Levels of Testing:**
    - **Unit Testing:** Focuses on individual objects or small groups of closely related objects. It verifies that each object behaves correctly in isolation according to its design.
    - **Integration Testing:** Tests the interactions between different objects, classes, or subsystems. It ensures that components work together as expected when combined.
    - **System Testing:** Tests the complete, integrated system to ensure it meets all specified requirements and performs as expected in its operational environment. This level often involves testing against the original use cases and user scenarios.
- **Traceability:** The use case-driven approach provides strong traceability from requirements to test cases, making it easier to ensure comprehensive testing.
- **Test Model:** Objectory includes a Test Model that provides the framework for planning, designing, and executing tests, and for documenting test results.