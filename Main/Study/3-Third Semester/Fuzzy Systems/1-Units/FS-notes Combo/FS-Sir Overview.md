#fuzzy-system #third-semester 

- [ALL THE TOPICS](#ALL%20THE%20TOPICS)

---
# Fuzzy Systems (CSc. 613) 

# What this course teaches

The course gradually builds from **probability** to **fuzzy logic**, then shows how fuzzy logic is used in **control systems**, **adaptive controllers**, and finally how it combines with **neural networks**.

The flow of the course is:

```
Uncertainty
       │
       ▼
Probability & Bayes
       │
       ▼
Fuzzy Logic
       │
       ▼
Fuzzy Sets & Linguistic Variables
       │
       ▼
Fuzzy Controllers
       │
       ▼
Adaptive Fuzzy Controllers
       │
       ▼
Hybrid Systems
(Fuzzy + Neural Networks)
```

---
# Real-world applications covered

According to the notes, fuzzy systems have been successfully applied in:

* Subway train control
* Washing machines
* Air conditioners
* Cameras (auto-focus)
* Industrial process control
* Robots
* Pattern recognition
* Medical diagnosis
* Decision support systems 

---

# What is the main idea of the entire course?

The central idea is:

* **Probability** answers: **"How likely is an event to occur?"**
* **Fuzzy logic** answers: **"To what degree does something belong to a concept?"**

Probability deals with **chance**, while fuzzy logic deals with **vagueness**. Together, they enable intelligent systems to make decisions in uncertain, imprecise, and real-world environments. 

---
# ALL THE TOPICS
**Main Headings**. 

---

# Unit 1: Introduction to Fuzzy Set Theory

1. [Probabilistic Reasoning](Probabilistic%20Reasoning.md)
2. [Uncertain Knowledge](Uncertain%20Knowledge.md)
3. [Handling Uncertainty](Handling%20Uncertainty.md)
4. [Making Decisions under Uncertainty](Making%20Decisions%20under%20Uncertainty.md)
5. [Basic Statistical Methods – Probability](Basic%20Statistical%20Methods%20%E2%80%93%20Probability.md)
6. [Random Variables](Random%20Variables.md)
7. [Atomic Event](Atomic%20Event.md)
8. [Propositions](Propositions.md)
9. Types of Random Variables
   * Boolean Random Variables
   * Discrete Random Variables
   * Continuous Random Variables
10. Prior Probability
11. Conditional Probability
12. Joint Probability Distribution
13. Inference Using Full Joint Probability Distribution
14. Marginalization (Summing Out)
15. Calculating Conditional Probability
16. Independence
17. Bayes' Rule (Theorem)
18. Example of Bayes' Rule
19. Fuzzy vs Probability
20. Fuzzy Logic
21. Linguistic Variables
22. Why Fuzzy Logic?
23. Usages in Real World
24. Extension Principle
25. History of Fuzzy Logic
26. First Applications
27. Truth or Falsity 

---

# Unit 5: Fuzzy Controller

1. [Control theory](Control%20theory.md)
2. [Open-loop and closed-loop control](Open-loop%20and%20closed-loop%20control.md)
	1. Control Loop Basics

3. [Fuzzy control systems](Fuzzy%20control%20systems.md)
	1. Assumptions in a Fuzzy Control System Design
	2. Steps in Designing a Simple Fuzzy Control System

4. [Types of controllers](Types%20of%20controllers.md)
   * [On-Off Controller](On-Off%20Controller.md)
	   * Process Gain - *General Concept*
	   * Control - *General Concept*

   * P Controller

   * [PID Controller](PID%20Controller.md)
	   * Proportional Term
	   * Integral Term
	   * Derivative Term

   * [Adaptive Controllers](Adaptive%20Controllers.md)
     * Need of Adaptive Controllers
     * Components of Adaptive Controllers
     * Design and Performance Evaluation

   * Model Based Controller
   * Model Predictive Controllers
   * MRAC (Model Reference Adaptive Control) Controllers 

---

# Unit 6: Nonlinear Systems and Adaptive Fuzzy Controller

1. Nonlinear Systems
2. The Nonlinearity of Controller
   * Additivity Property
   * Scaling (Homogeneity) Property
3. Sliding Mode FKBC
4. Sliding Mode Control 

---

# Unit 7: Hybrid Systems

1. Fuzzy Systems and Neural Networks
2. Universal Approximators
3. Fuzzy Neural Network 
4. [Genetic Algorithm](Genetic%20Algorithm.md)
	- [Numerical of GA](Numerical%20of%20GA.md)
---
# ---
# ---
---

# Unit 5: Fuzzy Controller

### Control Theory & Systems:
* Basics of dynamical systems, inputs, outputs, and feedback loops


* Control loop functions (Measure, Compare, Compute, Correct) and elements


* Process Variables (PV), Setpoints (SP), Manipulated/Control Variables (MV/CV), and Error


* Open-loop control vs. Closed-loop (feedback) control




### Fuzzy Control Systems:
* Conceptual stages: Input stage, Processing stage (IF-THEN rules/antecedent-consequent), Output stage


* Assumptions in fuzzy control system design


* Step-by-step design procedure for fuzzy controllers




### Types of Controllers:
* **On-Off / Bang-Bang Controllers:** Hysteresis and deadband concepts


* **Process Gain ($K$):** Definition, sensitivity, and mathematical formula


* **Error-Based Controllers:** Example of CSTR temperature regulation


* **Proportional (P) Controller:** Proportional gain ($K_p$), formulas, and output characteristics


* **PID Controller:** Proportional, Integral, and Derivative terms (mathematical formulation, behavior, tuning parameters)


* **Adaptive Controllers:** Need for handling nonlinearity/time-varying systems, parameter estimation, Feedforward/Feedback, and Direct/Indirect methods


* **Model-Based Controllers:** Fuzzy process models, performance measures, and decision makers


* **Model Predictive Controllers (MPC):** Dynamic model prediction and trajectory tracking


* **Model Reference Adaptive Control (MRAC):** MIT rule, reference models, and tracking error calculation





---

# Unit 6: Nonlinear Systems and Adaptive Fuzzy Controller

### Linearity vs. Nonlinearity

* Mathematical conditions for linear functions: Additivity (Superposition) and Homogeneity (Scaling)


* Definition of linear and nonlinear differential equations


* Linearity properties of controllers




### Sliding Mode FKBC (Fuzzy Knowledge-Based Controller):


* Handling model uncertainties, parameter fluctuations, and disturbances


* Chattering problem and boundary layer introduction


* Sliding surface / switching line formulation and state vector tracking





---

# Unit 7: Hybrid Systems

### Fuzzy Systems and Neural Networks Integration:

* Interconnection between fuzzy logic and artificial neural networks (ANNs)

* Universal approximators theorem for feedforward neural networks and fuzzy expert systems




### Fuzzy Neural Networks (FNN):

* Characteristics (fuzzy inputs, fuzzy outputs, fuzzy weights, alternative aggregation operators)


* Classification of Fuzzy Neural Nets (Types 1 through 7 based on crisp/fuzzy weights, inputs, and targets)


* Regular Fuzzy Neural Networks


* Logic Gate Fuzzy Neurons: AND Neuron (min-max composition) and OR Neuron (max-min composition)




### Generation of Membership Functions Using Neural Networks:

* Training and checking datasets


* Architecture ($2 \times 3 \times 3 \times 2$) for membership generation


* Sigmoidal activation function calculations and thresholding


* Error calculation, error backpropagation to hidden layers, and weight updating




### **Genetic Algorithms (GAs):**
* Fundamentals: Natural selection principles, search space, populations, chromosomes, genes, genotype vs. phenotype, and encoding/decoding


* **Encoding Types:** Binary, Permutation, Value, and Tree encoding


* **Fitness Function:** Purpose and evaluation


### **Genetic Operators:**
* *Selection Methods:* Roulette Wheel Selection (weighted fitness probability), Stochastic Universal Sampling, Tournament Selection, Rank-based Selection


* *Crossover:* One-Point, Multi-Point, and Tree Crossover


* *Mutation:* Bit Flip, Random Resetting, Swap Mutation, Single-node, and Subtree Replacement




### * **GA Parameters & Execution:** 
Crossover probability, mutation probability, termination conditions, and the step-by-step GA algorithm


### **Numerical Example:** 
Step-by-step optimization of $f(x) = x^2$ over one generation (encoding, initial population, selection/expected count, crossover, mutation, and evaluation)