A rule-based classifier has **rules**, and the **class is decided based on which rule is satisfied**.

Form:
$$IF\ condition\ THEN\ class$$

So when a new data object comes:

1. Check the IF part of each rule.
2. If the condition is true,
3. Assign the class given in the THEN part.

Example:

```
IF (Marks ≥ 40)
THEN Class = Pass
```

Input: Marks = 55
→ Condition true
→ Class = Pass

Another:

```
IF (Age < 18)
THEN Category = Minor
```

So simply:

> Rule-based classifier = *“If this condition is true, then assign this class.”*

