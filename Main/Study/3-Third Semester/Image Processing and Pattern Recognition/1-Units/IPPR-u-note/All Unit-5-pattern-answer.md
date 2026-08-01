#ippr #third-semester 


---

# UNIT 5: Pattern Recognition

---

# 1. What is Pattern Recognition?

## Definition

Pattern Recognition (PR) is the process of identifying an object or event and assigning it to one of several predefined classes based on its features.

> **Definition (Exam):**
>
> Pattern recognition is the science of automatically recognizing patterns and classifying data based on extracted features.

### Examples

* Face Recognition
* Fingerprint Recognition
* OCR (Handwritten Character Recognition)
* Speech Recognition
* Medical Disease Detection

---

# 2. Pattern vs Pattern Class ⭐⭐⭐

## Pattern

A **pattern** is an individual object or observation described by a set of measurable features.

Example

```
Image of digit "5"

Features:
Height
Width
Area
Boundary
```

This single digit image is one pattern.

---

## Pattern Class

A **pattern class** is a collection of similar patterns having common characteristics.

Example

```
All images of digit "5"

5
5
5
5
5

↓

One class
```

---

## Difference

| Pattern                      | Pattern Class                   |
| ---------------------------- | ------------------------------- |
| Single object                | Group of similar objects        |
| One feature vector           | Many feature vectors            |
| Example: One fingerprint     | All fingerprints of same person |
| Example: One handwritten "A" | All handwritten "A"s            |

---

# 3. Components of Pattern Recognition System ⭐⭐⭐⭐⭐

This is one of the **most repeated questions**.

## Block Diagram

```text
Input Image
     │
     ▼
Sensing
     │
     ▼
Preprocessing
     │
     ▼
Segmentation
     │
     ▼
Feature Extraction
     │
     ▼
Classification
     │
     ▼
Post Processing
     │
     ▼
Output
```

---

## (1) Sensing

Collects raw data.

Examples

* Camera
* Scanner
* MRI
* Sensor

Output

Raw image.

---

## (2) Preprocessing

Improves image quality.

Operations

* Noise removal
* Contrast enhancement
* Filtering

Goal

Produce a cleaner image.

---

## (3) Segmentation

Separates the object from the background.

Example

```
Background

□□□□□□
□□111□□
□□111□□
□□□□□□

Extract only

111
111
```

---

## (4) Feature Extraction

Extracts important information.

Examples

* Area
* Perimeter
* Shape
* Texture
* Color
* Edges

Instead of storing the whole image,

```
Store

Height = 20
Width = 10
Area = 180
```

---

## (5) Classification

Assigns the object to a class.

Example

```
Feature vector

↓

Classifier

↓

Cat
Dog
Bird
```

Methods

* Minimum Distance
* Neural Network
* SVM
* Decision Tree

---

## (6) Post Processing

Improves classification result.

Example

Correct spelling

```
"HE11O"

↓

HELLO
```

---

# Diagram for Exam

```text
Image
   │
   ▼
Sensing
   │
   ▼
Preprocessing
   │
   ▼
Segmentation
   │
   ▼
Feature Extraction
   │
   ▼
Classifier
   │
   ▼
Post Processing
   │
   ▼
Output
```

---

# 4. Pattern Recognition Strategies ⭐⭐⭐⭐

Three major strategies are commonly discussed.

---

## A. Statistical Pattern Recognition

Uses numerical features and probability.

Examples

* Minimum Distance Classifier
* Bayesian Classifier
* KNN

Advantages

* Fast
* Simple
* Works well with numerical data

Disadvantages

* Needs good features
* Sensitive to noise

---

## B. Structural Pattern Recognition

Represents patterns by relationships among components instead of only numerical features.

Example

A character can be described using

```
Lines
Curves
Connections
```

Used for

* Character recognition
* Symbol recognition
* Shape analysis

Advantages

* Captures structural information
* Useful for complex shapes

Disadvantages

* Complex implementation
* Computationally expensive

---

## C. Neural Network Pattern Recognition

Uses artificial neural networks to learn patterns from examples.

Example

```
Image

↓

Neural Network

↓

Cat
Dog
Bird
```

Advantages

* Learns automatically
* High accuracy
* Handles nonlinear problems

Disadvantages

* Requires large datasets
* Training can be slow

---

# 5. Minimum Distance Classifier ⭐⭐⭐⭐⭐

Frequently asked.

## Idea

Each class is represented by a **prototype (mean feature vector)**.

A new sample is assigned to the class whose prototype is nearest.

---

## Formula

For Euclidean distance,

$$
d=\sqrt{\sum_{i=1}^{n}(x_i-m_i)^2}
$$

where

* $x_i$ = test sample feature
* $m_i$ = class mean
* $d$ = distance

Choose the class with the **minimum distance**.

---

## Example

Suppose

```
Class A mean = (2,3)

Class B mean = (8,7)

Unknown = (3,4)
```

Distance to A

$$
d_A=\sqrt{(3-2)^2+(4-3)^2}
=\sqrt2
$$

Distance to B

$$
d_B=\sqrt{(3-8)^2+(4-7)^2}
=\sqrt{34}
$$

Since

$$
\sqrt2<\sqrt{34}
$$

Unknown belongs to **Class A**.

---

## Advantages

* Very simple
* Fast
* Easy implementation

---

## Disadvantages

* Assumes spherical classes
* Sensitive to feature scaling
* Poor for overlapping classes

---

# 6. Neural Network in Pattern Recognition ⭐⭐⭐

## Definition

A Neural Network is a computational model inspired by the human brain that learns from examples and classifies unknown patterns.

---

## Working

```text
Training Data

↓

Hidden Layers Learn

↓

Weights Updated

↓

Classifier Ready

↓

Unknown Pattern

↓

Predicted Class
```

---

## Advantages

* Learns automatically
* High accuracy
* Robust
* Handles nonlinear data

---

## Disadvantages

* Needs training
* Large data required
* Difficult to interpret

---

# 7. Confusion Matrix ⭐⭐⭐⭐⭐

Most recent exam favorite.

Suppose

```text
                  Predicted

              Positive   Negative

Actual Positive    TP         FN

Actual Negative    FP         TN
```

---

## Meaning

### TP

Actually positive

Predicted positive

Correct

---

### TN

Actually negative

Predicted negative

Correct

---

### FP

Actually negative

Predicted positive

False alarm

---

### FN

Actually positive

Predicted negative

Missed detection

---

# Accuracy

Measures overall correctness.

$$
Accuracy=\frac{TP+TN}{TP+TN+FP+FN}
$$

---

# Precision

Out of predicted positives,

how many are actually positive?

$$
Precision=\frac{TP}{TP+FP}
$$

---

# Recall (Sensitivity)

Out of actual positives,

how many are detected?

$$
Sensitivity=\frac{TP}{TP+FN}
$$

High sensitivity means **few false negatives**.

---

# Specificity

Out of actual negatives,

how many are correctly rejected?

$$
Specificity=\frac{TN}{TN+FP}
$$

High specificity means **few false positives**.

---

# F1 Score (Extra)

$$
F1=
\frac{2\times Precision\times Recall}
{Precision+Recall}
$$

---

# Example

Suppose

```
TP = 90

TN = 80

FP = 10

FN = 20
```

Accuracy

$$
\frac{90+80}{200}
=0.85
=85%
$$

Precision

$$
\frac{90}{90+10}
=90%
$$

Sensitivity

$$
\frac{90}{90+20}
=81.8%
$$

Specificity

$$
\frac{80}{80+10}
=88.9%
$$

---

# Uses of Sensitivity & Specificity

**Sensitivity**

* Important when missing a positive case is costly.
* Example: disease detection, cancer screening.

**Specificity**

* Important when false alarms should be minimized.
* Example: spam filtering, fraud detection.

---

# Frequently Asked Theory Question

## What is the strategy for Pattern Recognition?

The general strategy is:

1. Acquire data using sensors.
2. Preprocess the data to improve quality.
3. Segment the object of interest.
4. Extract discriminative features.
5. Classify the pattern using an appropriate classifier (statistical, structural, or neural).
6. Perform post-processing to refine the result.

---

# Exam Priority

| Topic                                                            | Importance   |
| ---------------------------------------------------------------- | ------------ |
| Components of Pattern Recognition System                         | 🔴 Very High |
| Pattern vs Pattern Class                                         | 🔴 Very High |
| Minimum Distance Classifier                                      | 🔴 Very High |
| Confusion Matrix (Accuracy, Precision, Sensitivity, Specificity) | 🔴 Very High |
| Pattern Recognition Strategies                                   | 🟠 High      |
| Neural Network-based Classification                              | 🟠 High      |
| Structural Pattern Recognition                                   | 🟡 Medium    |

