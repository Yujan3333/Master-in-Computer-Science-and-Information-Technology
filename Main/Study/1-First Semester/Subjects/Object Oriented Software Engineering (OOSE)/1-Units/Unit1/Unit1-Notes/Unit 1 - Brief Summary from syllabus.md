

## 1. Software Life Cycle Models

### Introduction to SDLC

Software Development Life Cycle (SDLC) is a systematic approach to developing software that ensures quality and correctness. It provides a structured framework for planning, creating, testing, and deploying software systems.

### Classical SDLC Models

#### 1.1 Waterfall Model

**Characteristics:**

- Sequential phases with no overlap
- Each phase must be completed before the next begins
- Documentation-driven approach
- Linear progression through phases

**Phases:**

1. Requirements Analysis
2. System Design
3. Implementation
4. Testing
5. Deployment
6. Maintenance

**Advantages:**

- Simple and easy to understand
- Well-documented process
- Clear milestones and deliverables
- Good for small, well-understood projects

**Disadvantages:**

- Inflexible to changes
- No working software until late in cycle
- High risk and uncertainty
- Not suitable for complex projects

#### 1.2 Iterative Model

**Characteristics:**

- Develops software through repeated cycles
- Each iteration produces a working version
- Feedback incorporated in subsequent iterations

**Process:**

- Initial planning and requirements
- Multiple iterations of design-code-test
- Each iteration adds functionality
- Final integration and deployment

**Advantages:**

- Early delivery of partial working product
- Easier to manage risk
- Flexibility to accommodate changes
- Continuous user feedback

#### 1.3 Spiral Model

**Characteristics:**

- Risk-driven approach
- Combines iterative development with systematic risk analysis
- Four main activities in each spiral

**Four Quadrants:**

1. **Planning:** Determine objectives, alternatives, constraints
2. **Risk Analysis:** Identify and resolve risks
3. **Engineering:** Develop and test product
4. **Evaluation:** Customer evaluation and planning for next iteration

**Advantages:**

- Strong risk management
- Good for large, complex projects
- Accommodates changing requirements
- Early user involvement

### Agile Methodologies

#### 1.4 Agile Model

**Core Principles:**

- Individuals and interactions over processes and tools
- Working software over comprehensive documentation
- Customer collaboration over contract negotiation
- Responding to change over following a plan

**Key Practices:**

- Short iterations (sprints)
- Continuous customer involvement
- Adaptive planning
- Self-organizing teams

#### 1.5 Scrum Framework

**Roles:**

- **Product Owner:** Defines requirements and priorities
- **Scrum Master:** Facilitates process and removes obstacles
- **Development Team:** Creates the product

**Artifacts:**

- **Product Backlog:** Prioritized list of features
- **Sprint Backlog:** Work selected for current sprint
- **Increment:** Potentially shippable product increment

**Events:**

- Sprint Planning
- Daily Standups
- Sprint Review
- Sprint Retrospective

## 2. Requirement Analysis and Specification

### 2.1 Introduction to Requirements Engineering

Requirements engineering is the process of establishing the services that the customer requires from a system and the constraints under which it operates and is developed.

### 2.2 Types of Requirements

#### Functional Requirements

- Define what the system should do
- Describe system services and functions
- Specify system behavior for particular inputs
- May state what system should not do

**Examples:**

- User authentication and authorization
- Data processing and calculations
- Report generation
- System interfaces

#### Non-Functional Requirements

- Define system properties and constraints
- Often more critical than functional requirements
- Can be difficult to verify

**Categories:**

- **Performance:** Response time, throughput, memory usage
- **Security:** Access control, data protection, authentication
- **Usability:** User interface design, ease of use
- **Reliability:** Fault tolerance, availability, recoverability
- **Portability:** Platform independence, scalability

### 2.3 Requirements Engineering Process

#### Requirements Elicitation

**Techniques:**

- **Interviews:** Structured and unstructured discussions
- **Questionnaires:** Large-scale information gathering
- **Observation:** Studying current work practices
- **Workshops:** Collaborative requirement sessions
- **Prototyping:** Building early system versions
- **Scenarios and Use Cases:** Describing system interactions

#### Requirements Analysis and Negotiation

- Checking requirements for conflicts and inconsistencies
- Prioritizing requirements
- Resolving conflicts between stakeholders
- Analyzing feasibility (technical, economic, operational)

#### Requirements Documentation

**Common Formats:**

- Natural language specifications
- Structured specifications
- Use case diagrams
- User stories
- Formal specifications

#### Requirements Validation

**Validation Techniques:**

- Requirements reviews and inspections
- Prototyping
- Test case generation
- Automated consistency analysis

### 2.4 Use Case Modeling

**Components:**

- **Actors:** External entities that interact with system
- **Use Cases:** Specific ways actors use the system
- **Relationships:** Associations, includes, extends, generalizes

**Use Case Description Elements:**

- Use case name and ID
- Primary actor
- Preconditions and postconditions
- Main success scenario
- Alternative flows
- Exception handling

## 3. Object-Oriented Software Development

### 3.1 Object-Oriented Paradigm Fundamentals

#### Core Concepts

**Object:**

- Real-world entity with state and behavior
- Encapsulates data (attributes) and operations (methods)
- Has unique identity

**Class:**

- Template or blueprint for creating objects
- Defines structure and behavior common to all objects
- Specifies attributes and methods

**Key Principles:**

#### 3.2 Encapsulation

- Bundling data and methods that operate on data
- Hiding internal implementation details
- Providing controlled access through interfaces
- Reduces complexity and increases maintainability

**Benefits:**

- Data protection and security
- Modularity and code organization
- Easier maintenance and debugging
- Interface stability

#### 3.3 Inheritance

- Mechanism for creating new classes based on existing classes
- Child class inherits attributes and methods from parent class
- Enables code reuse and hierarchical organization

**Types:**

- **Single Inheritance:** One parent class
- **Multiple Inheritance:** Multiple parent classes
- **Multilevel Inheritance:** Chain of inheritance
- **Hierarchical Inheritance:** Multiple child classes from one parent

**Benefits:**

- Code reusability
- Hierarchical classification
- Polymorphism support
- Easier maintenance

#### 3.4 Polymorphism

- Ability of objects to take multiple forms
- Same interface, different implementations
- Enables dynamic method binding

**Types:**

- **Compile-time Polymorphism:** Method overloading
- **Runtime Polymorphism:** Method overriding
- **Interface Polymorphism:** Multiple classes implementing same interface

#### 3.5 Abstraction

- Hiding complex implementation details
- Focusing on essential features
- Providing simplified interfaces

**Levels:**

- **Data Abstraction:** Abstract data types
- **Process Abstraction:** Abstract operations
- **Control Abstraction:** Abstract control structures

### 3.6 Object-Oriented Analysis and Design (OOAD)

#### Object-Oriented Analysis (OOA)

**Objectives:**

- Understand problem domain
- Identify objects and their relationships
- Define system requirements from OO perspective

**Activities:**

- Domain modeling
- Use case analysis
- Object identification
- Relationship modeling
- Behavior modeling

#### Object-Oriented Design (OOD)

**Objectives:**

- Transform analysis model into design model
- Define system architecture
- Specify implementation details

**Activities:**

- System architecture design
- Object design
- Interface design
- Database design
- Algorithm design

### 3.7 Benefits of Object-Oriented Development

**Development Benefits:**

- **Modularity:** Systems broken into manageable pieces
- **Reusability:** Code can be reused across projects
- **Maintainability:** Easier to modify and extend
- **Scalability:** Easier to add new features

**Quality Benefits:**

- **Reliability:** Encapsulation reduces errors
- **Flexibility:** Polymorphism enables adaptability
- **Testability:** Individual objects can be tested independently

**Management Benefits:**

- **Productivity:** Faster development through reuse
- **Quality:** Better software quality through proven practices
- **Risk Reduction:** Iterative development reduces project risks

### 3.8 Object-Oriented Development Process

1. **Requirements Analysis:** Identify use cases and actors
2. **Domain Modeling:** Create conceptual object model
3. **System Design:** Define system architecture
4. **Object Design:** Detailed design of classes and interfaces
5. **Implementation:** Code classes and methods
6. **Testing:** Unit, integration, and system testing
7. **Deployment:** System installation and configuration