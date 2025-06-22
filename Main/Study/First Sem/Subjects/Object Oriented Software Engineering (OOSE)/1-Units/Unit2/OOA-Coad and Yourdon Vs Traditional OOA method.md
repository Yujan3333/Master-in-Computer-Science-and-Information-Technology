

|**Feature**|**OOA – Coad/Yourdon**|**Traditional OOA Methods**|
|---|---|---|
|**Specificity**|A well-defined methodology with clear steps and unique terminology.|A broad collection of general object-oriented analysis ideas and techniques.|
|**Core Emphasis**|Focuses on five modeling layers: Subject, Class & Object, Structure, Attribute, Service.|Focuses on identifying entities, behaviors, and relationships in the problem domain.|
|**Notation/Diagrams**|Uses specific symbols for gen-spec, whole-part, subjects, and message connections.|Uses generic or varied notations, often informal before UML standardization.|
|**Identification Process**|Structured steps like finding classes, structures, attributes, and services.|General activities like identifying key objects and defining responsibilities.|
|**Separation from Design**|Clear boundary between analysis and design phases.|Often loosely separates analysis and design; may overlap in hybrid methods.|
|**Historical Role**|Influential early method that contributed to UML.|Represents foundational ideas from early OO thinking across multiple approaches.|




|**Aspect**|**OOA – Coad/Yourdon**|**Traditional Object-Oriented Analysis Methods**|
|---|---|---|
|**Model Layers**|Explicitly defines 5 modeling layers: Subject, Class & Object, Structure, Attribute, Service.|May not clearly separate layers; modeling is often mixed or informal.|
|**Use Case Integration**|Use cases ("threads") are handled **after** class modeling.|Use cases often drive the whole analysis (e.g., in Jacobson's OOSE).|
|**System Viewpoint**|Begins with **object structure** (static) and adds behavior later.|Often starts from **user interaction/behavior** and derives objects from that.|
|**Clarity and Simplicity**|Aimed for **simple, structured analysis** for medium-sized systems.|Some methods can be **complex**, especially those designed for real-time or large systems.|
|**Object Discovery**|Uses checklist and guidelines to **systematically discover classes and objects**.|Often relies on analyst's experience or domain knowledge without strict process.|
|**Relationships**|Focuses on **gen-spec (inheritance)** and **whole-part (composition)** as main structure types.|Other methods might emphasize **association**, **aggregation**, or **state behavior** more.|
|**Behavior Modeling**|Behavior added as "services" after structure is defined.|Behavior is sometimes modeled earlier or in parallel (e.g., through state machines).|
|**Notational Standard**|Coad/Yourdon had its **own diagramming language**.|Many used custom notations before UML (OMT, HOOD, etc.), which varied widely.|
|**Reuse Focus**|Encouraged reuse through **shared classes** and **subjects**.|Some methods emphasize reuse via **frameworks or libraries** rather than analysis-time reuse.|
|**Transition to Design**|Provides a **smooth path to Coad/Yourdon OOD** methodology.|Transition from analysis to design may vary or be handled by a different method altogether.|