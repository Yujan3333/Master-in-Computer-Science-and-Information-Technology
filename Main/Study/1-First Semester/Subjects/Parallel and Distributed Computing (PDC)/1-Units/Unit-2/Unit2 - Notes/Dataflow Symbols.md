Here are concrete examples of all the dataflow operators:

## **1. General Operator (Addition)**
```
Inputs: 15, 25
Function: f(a,b) = a + b
Output: 40
```

## **2. General Operator (Comparison)**
```
Inputs: 15, 25
Function: f(a,b) = a > b
Output: FALSE
```

## **3. Predicate Operator**
```
Inputs: 17
Function: isPrime(n) - checks if number is prime
Output: TRUE (17 is prime)
```

## **4. Merge Operator**
```
Data Input 1: "Hello"
Data Input 2: "World"
Control Input: TRUE
Output: "Hello" (selected based on TRUE condition)
```

## **5. Switch Operator**
```
Data Input: 100
Control Input: FALSE
Outputs: 
- T path: (nothing)
- F path: 100 (routed to FALSE path)
```

## **6. Copy Operator**
```
Input: 42
Outputs: 
- Output 1: 42
- Output 2: 42
- Output 3: 42
(Same value duplicated to all outputs)
```

## **Real-World Scenario Example**:
```
Temperature Sensor Reading: 85°F

1. Predicate: isHot(85) → TRUE
2. Switch: Routes 85 to "Hot" path based on TRUE
3. Copy: Duplicates 85 to multiple systems
   - Display: 85
   - Logger: 85  
   - Alert System: 85
4. Operator: Convert to Celsius: (85-32)*5/9 → 29.4°C
5. Merge: Choose display format based on user preference
   - Input 1: "85°F"
   - Input 2: "29.4°C" 
   - Condition: showFahrenheit = TRUE
   - Output: "85°F"
```

Each operator has a distinct role in processing and routing data through the dataflow network!