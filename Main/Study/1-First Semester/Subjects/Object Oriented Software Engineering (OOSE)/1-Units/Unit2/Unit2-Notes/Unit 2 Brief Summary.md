### Unit 2: Introduction to Object-Orientation and Object-Oriented System Development (Based on Ivar Jacobson's Textbook)

This unit delves into the fundamental concepts of object-orientation and how they are applied in system development, particularly through the lens of Ivar Jacobson's "Object-Oriented Software Engineering: A Use Case Driven Approach."

#### 1. Introduction to Object-Orientation

The book introduces object-orientation as a powerful paradigm for structuring systems to better manage complexity and improve adaptability. It moves beyond traditional procedural or data-centric views by emphasizing the concept of an **object** as a fundamental building block.

Key ideas presented as part of object-orientation:

- **Objects:** Entities that encapsulate both data (attributes) and behavior (methods or services). They represent things in the real world or conceptual entities within the system.
- **Classes:** Blueprints or templates from which objects are created. A class defines the common structure and behavior shared by all objects of that type.
- **Encapsulation:** The principle of bundling data and the methods that operate on that data within a single unit (the object), and hiding the internal details from the outside world. This promotes modularity and reduces interdependencies.
- **Message Passing:** Objects communicate with each other by sending messages, requesting services to be performed.
- **Inheritance:** A mechanism where a new class (subclass) can inherit attributes and behaviors from an existing class (superclass), promoting code reuse and establishing "is-a" relationships.
- **Polymorphism:** The ability of different objects to respond to the same message in their own unique way, depending on their specific type.

#### 2. Object-Oriented System Development - Function/Data Methods

Jacobson's approach to object-oriented system development fundamentally integrates functions (behaviors/methods) with data (attributes) within objects. This is a significant departure from older procedural development where data structures and the functions that operate on them were often kept separate.

- **Unified View:** The core idea is that an object is a coherent unit where data and the operations that can be performed on that data are inseparable. This unification is what makes objects powerful for modeling real-world entities.
- **Reduced Complexity and Increased Robustness:** By ensuring that data can only be accessed and modified through an object's defined methods, the system becomes more robust against unintended side effects and easier to understand and maintain. This controlled interaction is a hallmark of the "function/data method" within an OO context.

#### 3. Object-Oriented Analysis (OOA)

In Jacobson's Objectory process, Object-Oriented Analysis is the phase where the focus shifts from understanding requirements to building a conceptual object model of the system. This phase is heavily influenced by **use cases**.

- **Purpose:** To define the system's conceptual classes and objects, their relationships, and responsibilities, based on the requirements. It abstracts away implementation details.
- **Use Case Driven:** OOA in Objectory is driven by the use cases identified in the requirements phase. The analysis model is built to support the identified use cases, ensuring that the system's objects collectively fulfill the user's needs.
- **Model Building:** The outcome is an **Analysis Model** that represents the system's essential properties and behavior in object-oriented terms. This model typically includes:
    - **Boundary Objects:** Represent interactions with external actors and systems (e.g., user interfaces, interfaces to other systems).
    - **Entity Objects:** Represent information or persistent data (e.g., customer, order, product).
    - **Control Objects:** Coordinate the flow of logic for a use case, encapsulating specific behavior tied to a use case.
- **Refinement:** The analysis phase refines the understanding of the problem domain and prepares it for design.

#### 4. Construction and Testing

In Objectory, "Construction" (often referred to as Implementation) and "Testing" are distinct, yet closely integrated, phases that bring the object-oriented design to life and validate its correctness.

- **Construction (Implementation Model):** This phase involves the actual programming of the system based on the refined object-oriented design. The objects and classes defined during design are translated into executable code using an object-oriented programming language. The focus is on implementing the methods, attributes, and relationships defined in the design model.
- **Testing (Test Model):** Testing is crucial throughout the Objectory process, with a dedicated **Test Model**. The use cases play a vital role here, as test cases are often derived directly from them.
    - **Unit Testing:** Testing individual objects or small groups of closely related objects. It verifies that each object behaves correctly in isolation according to its design.
    - **Integration Testing:** Tests the interactions between different objects, classes, or subsystems. It ensures that components work together as expected when combined.
    - **System Testing:** Tests the complete, integrated system to ensure it meets all specified requirements and performs as expected in its operational environment. This level often involves testing against the original use cases and user scenarios.
    - The goal is to ensure the implemented system correctly fulfills the specified requirements and adheres to the design.

#### 5. Object-Oriented Programming with Examples

While the textbook focuses on the engineering process (Objectory) rather than specific code examples, the principles discussed are directly applied through Object-Oriented Programming (OOP) languages. OOP is the practical realization of the object-oriented concepts.

- **Key OOP Concepts in Practice:**
    - **Defining Classes:** Creating blueprints for objects (e.g., `class Customer { ... }`).
    - **Creating Objects (Instantiation):** Making instances of classes (e.g., `Customer myCustomer = new Customer();`).
    - **Implementing Attributes:** Defining the data held by objects (e.g., `string name; int customerId;`).
    - **Implementing Methods:** Writing the code for behaviors (e.g., `void placeOrder(); void updateAddress(string newAddress);`).
    - **Utilizing Inheritance:** Creating specialized classes from general ones (e.g., `class PremiumCustomer : public Customer { ... }`).
    - **Applying Polymorphism:** Allowing objects of different classes to be treated through a common interface (e.g., a `display()` method behaving differently for `Product` and `Service` objects).