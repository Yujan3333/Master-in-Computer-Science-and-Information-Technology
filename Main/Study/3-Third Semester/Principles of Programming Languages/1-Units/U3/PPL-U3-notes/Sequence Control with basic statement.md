#PPL #third-semester 

# Unit 3.1: Sequence Control (According to C.Sc. 618 Syllabus)

Sequence control refers to **the order in which program statements are executed**. It determines the flow of execution in a program. Every programming language provides mechanisms to control this execution order.

---

# Definition

**Sequence Control** is the set of language features that determine the order in which instructions are executed during program execution.

Without sequence control, a program would execute statements only from top to bottom.

Example:

```c
printf("A");
printf("B");
printf("C");
```

Output

```
A
B
C
```

This is **simple sequential execution**.

---

# Types of Sequence Control (According to Syllabus)

The syllabus divides sequence control into four parts:

1. Sequence Control with Basic Statements
2. Sequence Control with Arithmetic Statements
3. Sequence Control with Non-Arithmetic Statements
4. Sequence Control Between Statements

---

# 1. Sequence Control with Basic Statements

These are the fundamental constructs that control execution.

## A. Sequential Execution

Statements execute one after another.

Example

```c
int a = 5;
int b = 10;
int c = a + b;
printf("%d", c);
```

Execution order

```
Statement 1
     ↓
Statement 2
     ↓
Statement 3
     ↓
Statement 4
```

### Advantages

* Simple
* Easy to understand
* Fast execution

---

## B. Selection (Decision Making)

Allows choosing one path among many.

Examples

### if

```c
if (x > 0)
    printf("Positive");
```

Flow

```
Condition
   |
True → Execute
False → Skip
```

---

### if-else

```c
if (x > 0)
    printf("Positive");
else
    printf("Negative");
```

Flow

```
Condition
  /   \
True False
 |      |
Stmt1 Stmt2
```

---

### switch

```c
switch(choice)
{
case 1:
    printf("One");
    break;

case 2:
    printf("Two");
    break;

default:
    printf("Invalid");
}
```

Used when many alternatives exist.

---

## C. Iteration (Looping)

Repeats a statement multiple times.

### for loop

```c
for(int i=1;i<=5;i++)
    printf("%d",i);
```

Output

```
1 2 3 4 5
```

---

### while loop

```c
while(i<5)
{
    i++;
}
```

Condition checked before execution.

---

### do-while

```c
do
{
    i++;
}
while(i<5);
```

Condition checked after execution.

Runs at least once.

---

# 2. Sequence Control with Arithmetic Statements

Arithmetic expressions also influence execution.

They determine

* order of evaluation
* precedence
* associativity
* side effects

---

## Operator Precedence

Example

```c
x = 5 + 3 * 2;
```

Execution

```
3 × 2 = 6
5 + 6 = 11
```

Not

```
(5+3)×2
```

because multiplication has higher precedence.

---

## Associativity

Example

```c
20 - 5 - 3
```

Left associative

```
(20-5)-3 = 12
```

---

## Parentheses

```c
(5+3)*2
```

Output

```
16
```

Parentheses override precedence.

---

## Increment and Decrement

### Pre-increment

```c
++x
```

Increase first, then use.

Example

```c
x=5;
y=++x;
```

Result

```
x=6
y=6
```

---

### Post-increment

```c
x++
```

Use first, then increase.

```c
x=5;
y=x++;
```

Result

```
x=6
y=5
```

---

## Short-circuit Arithmetic Evaluation

Sometimes arithmetic expressions stop early.

Example

```c
x!=0 && y/x>2
```

If

```
x==0
```

Second part is not evaluated.

This prevents divide-by-zero.

---

# 3. Sequence Control with Non-Arithmetic Statements

These statements alter normal execution without arithmetic calculations.

---

## goto

Transfers control directly.

Example

```c
goto End;

printf("Hello");

End:
printf("Bye");
```

Output

```
Bye
```

### Advantages

* Simple jumps

### Disadvantages

* Difficult debugging
* Spaghetti code

Usually discouraged.

---

## break

Terminates loop or switch.

```c
for(i=1;i<=10;i++)
{
    if(i==5)
        break;
}
```

Loop stops at

```
5
```

---

## continue

Skips current iteration.

```c
for(i=1;i<=5;i++)
{
    if(i==3)
        continue;

    printf("%d",i);
}
```

Output

```
1 2 4 5
```

---

## return

Ends function execution.

```c
int sum()
{
    return 10;
}
```

Control returns to caller.

---

## exit()

Terminates entire program.

```c
exit(0);
```

---

# 4. Sequence Control Between Statements

This refers to how execution moves from one statement block to another.

---

## Function Calls

```c
main()
{
    display();
}

display()
{
    printf("Hello");
}
```

Execution

```
main()
   ↓
display()
   ↓
return
```

---

## Nested Statements

```c
if(a>0)
{
    while(b>0)
    {
        printf("Hi");
    }
}
```

Execution enters one block inside another.

---

## Nested Function Calls

```c
A()
{
    B();
}

B()
{
    C();
}
```

Flow

```
A
↓
B
↓
C
↑
B
↑
A
```

---

## Recursion

Function calls itself.

```c
fact(n)
{
    if(n==0)
        return 1;

    return n*fact(n-1);
}
```

Execution

```
fact(4)
 ↓
fact(3)
 ↓
fact(2)
 ↓
fact(1)
 ↓
fact(0)
```

Returns in reverse order.

---

## Exception Transfer (Modern Languages)

Languages like Java and C++ can transfer control when an exception occurs.

Example

```java
try
{
    ...
}
catch(Exception e)
{
    ...
}
```

Control moves directly to the handler.

---

# Flow of Sequence Control

```
Start
  |
Sequential Statements
  |
Decision (if/switch)
  |
Loop (for/while/do-while)
  |
Function Call
  |
Return
  |
End
```

---

# Advantages of Sequence Control

* Controls program flow.
* Supports decision making.
* Enables repetition through loops.
* Improves modularity using functions.
* Makes programs efficient and readable.

# Disadvantages

* Improper use of `goto` reduces readability.
* Complex nested control structures are harder to debug.
* Incorrect flow may lead to infinite loops or unreachable code.

---

# Exam-Oriented Short Notes

**Q. What is Sequence Control?**
**Ans:** Sequence control is the mechanism that determines the order in which program statements are executed.

**Q. What are the four types of sequence control in the syllabus?**
**Ans:** Sequence control with basic statements, arithmetic statements, non-arithmetic statements, and between statements.

**Q. Give examples of basic sequence control statements.**
**Ans:** Sequential execution, `if`, `if-else`, `switch`, `for`, `while`, and `do-while`.

**Q. What is sequence control with arithmetic statements?**
**Ans:** It controls execution through arithmetic expression evaluation using operator precedence, associativity, parentheses, increment/decrement, and short-circuit evaluation.

**Q. What are non-arithmetic sequence control statements?**
**Ans:** `goto`, `break`, `continue`, `return`, and `exit()`.

**Q. What is sequence control between statements?**
**Ans:** It refers to transferring control among statement blocks using function calls, nested statements, recursion, and exception handling.

These points cover the **Sequence Control** topic as outlined in the TU MSc CSIT **Principles of Programming Languages (C.Sc. 618)** syllabus and are suitable for both short-answer and long-answer exam questions.
