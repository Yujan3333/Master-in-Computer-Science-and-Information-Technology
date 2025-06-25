## 🎲 Randomized Algorithms

Randomized algorithms use **random numbers** at one or more steps during computation.  
This randomness helps to:

- Simplify the algorithm.
    
- Improve average-case performance.
    
- Escape from worst-case inputs.
    

> 🔑 **Key Idea:** The algorithm's behavior is not fixed—it may change for the same input because it uses randomness.

---

## 🎰 1. Monte Carlo Algorithms

### 📌 Characteristics:

- **Fast and efficient**.
    
- The algorithm **always terminates** within a fixed time.
    
- It may produce a **wrong result with small probability**.
    

> You **sacrifice accuracy** slightly to get **speed and simplicity**.

### ✅ Used When:

- Exact answer isn’t essential.
    
- You want fast results with very high probability of being correct.

### 🖥️Pseudo Code

```md 
ALGORITHM MonteCarlo(input, trials):
    successes = 0
    for i = 1 to trials:
        result = RandomizedAttempt(input)
        if result meets criteria:
            successes++
    return successes / trials  // Probability estimate
```

### ⚙️ Examples:

1. **Primality Testing** – e.g., **Miller-Rabin Test**
    
    - Says a number is "probably prime" or "composite".
        
    - Fast, but could be wrong with very low probability.
        
2. **Monte Carlo integration** – used in estimating areas or volumes using random sampling.
    

---

## 🎲 2. Las Vegas Algorithms

### 📌 Characteristics:

- **Always gives the correct answer**.
    
- But the **running time may vary** depending on the random choices.
    

> You **sacrifice guaranteed speed** to get **guaranteed accuracy**.

### ✅ Used When:

- Accuracy is essential.
    
- You are okay with the algorithm running longer occasionally.

### 🖥️Pseudo Code
```md 
ALGORITHM LasVegas(input):
    repeat:
        result = RandomizedAttempt(input)
        if IsCorrect(result):
            return result
    // Always returns correct answer, runtime varies
```


### ⚙️ Examples:

1. **Randomized QuickSort**
    
    - Pivot is chosen randomly.
        
    - Output is always correct (sorted array).
        
    - Runtime may vary depending on pivot choices.
        
2. **Randomized algorithms for Min Cut in graphs** (with repetition till correctness is achieved).
    

---

## 🔁 DIFFERENCE

|Feature|**Monte Carlo Algorithm**|**Las Vegas Algorithm**|
|---|---|---|
|**Correctness**|Not always guaranteed (may give incorrect result)|Always correct|
|**Running Time**|Always fixed or bounded|Varies (randomized)|
|**Use-case**|When approximate answer is okay|When exact answer is required|
|**Reliability**|High probability of correctness|100% correctness|
|**Example**|Miller-Rabin Primality Test|Randomized QuickSort|

---

## 🧠 Visualization Analogy:

> Imagine you're solving a puzzle:

- **Monte Carlo**: You guess quickly and say, “I’m **pretty sure** this is right.” (even if you're wrong sometimes).
    
- **Las Vegas**: You take your time and try until you're **completely sure** the puzzle is solved correctly.
    

---

## Summary

### ✅ Randomized Algorithm Types:

- **Monte Carlo**: Fast, may be incorrect.
    
- **Las Vegas**: Correct, but time may vary.