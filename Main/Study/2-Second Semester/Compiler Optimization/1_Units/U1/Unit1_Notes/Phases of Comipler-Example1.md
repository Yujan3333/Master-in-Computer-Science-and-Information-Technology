
## ⚙️ `area = 3.14 & pow(r, 2)`

### 1. Lexical Analysis (Scanning)

**Input:** Stream of characters: `a r e a = 3 . 1 4 & p o w ( r , 2 )`
**Process:** The Lexical Analyzer (Scanner) reads the characters, removes whitespace, and groups them into meaningful units called **tokens**. It also builds or updates the **Symbol Table** with information about identifiers (like `area`, `pow`, `r`).

| Lexeme | Token Name | Attribute Value |
| :--- | :--- | :--- |
| `area` | **ID** | Pointer to Symbol Table for "area" |
| `=` | **ASSIGN\_OP** | |
| `3.14` | **NUM** | Value $3.14$ (Type: `float`/`double`) |
| `&` | **OP** | Operator (bitwise AND in C/C++, but its use here might be a logical error) |
| `pow` | **ID** | Pointer to Symbol Table for "pow" (Function) |
| `(` | **LPAREN** | |
| `r` | **ID** | Pointer to Symbol Table for "r" |
| `,` | **COMMA** | |
| `2` | **NUM** | Value $2$ (Type: `int`) |
| `)` | **RPAREN** | |

**Output:** A stream of tokens passed to the next phase:
$$\langle \text{ID}, \text{area} \rangle \langle \text{ASSIGN\_OP} \rangle \langle \text{NUM}, 3.14 \rangle \langle \text{OP}, \& \rangle \langle \text{ID}, \text{pow} \rangle \langle \text{LPAREN} \rangle \langle \text{ID}, \text{r} \rangle \langle \text{COMMA} \rangle \langle \text{NUM}, 2 \rangle \langle \text{RPAREN} \rangle$$

-----

### 2. Syntax Analysis (Parsing)

**Input:** Stream of tokens.
**Process:** The Parser checks if the token sequence adheres to the language's formal grammar rules. It imposes a hierarchical structure on the tokens and generates a **Parse Tree** or an **Abstract Syntax Tree (AST)**.

**Output:** An AST, which structurally represents the expression.

### 3. Semantic Analysis

**Input:** Abstract Syntax Tree.
**Process:** This phase checks for logical consistency and meaning. Key checks for this statement include:

  * **Type Checking:**
      * `3.14` is a `float`/`double`.
      * `pow(r, 2)`: If `r` is a number, the function returns a number (e.g., `double`).
      * **Potential Error:** The `&` operator is typically used for **bitwise AND** on integers or for taking the address of a variable. If `3.14` and the result of `pow()` are floating-point numbers, the use of `&` is a **Semantic Error** (type mismatch) in most languages. If the language has type coercion rules, it might attempt to convert the operands (e.g., to integers) before applying `&`.
  * **Identifier Checks:** Ensures `area`, `pow`, and `r` are all declared and used correctly (e.g., `pow` is defined as a function).

**Output:** An **Annotated AST**, which is the original tree with type information and any necessary type coercions added. For example, if `r` and `2` were integers, coercions would be added to convert them to `double` for the `pow` function.

-----

### 4. Intermediate Code Generation

**Input:** Annotated AST.
**Process:** The compiler translates the high-level language structure into a simple, machine-independent representation, often **Three-Address Code (TAC)**. This makes optimization easier.

**Example of Three-Address Code (assuming the `&` is an error and the compiler continues):**

1.  `T1 = pow(r, 2)` (Calculate $r^2$)
2.  `T2 = 3.14 & T1` (Perform the operation, possibly using coerced types)
3.  `area = T2` (Assignment)

-----

### 5. Code Optimization

**Input:** Intermediate Code (TAC).
**Process:** This optional phase attempts to improve the code's efficiency (speed and space) without changing its meaning.

  * If the compiler detects that `pow(r, 2)` can be simplified to `r * r`, it might perform **Function Inlining/Strength Reduction**.
      * `T1 = r * r`
  * If `3.14` is a known constant, the expression might be subject to **Constant Folding** if the operation was `*` instead of `&`. (Optimization of the erroneous `&` operation is unlikely).
  * If the code were inside a loop and `r` was loop-invariant, the calculation could be moved outside (Loop-Invariant Code Motion).

**Output:** Optimized Intermediate Code.

-----

### 6. Code Generation

**Input:** Optimized Intermediate Code.
**Process:** The final phase translates the intermediate code into the target machine's instruction set (Assembly or Machine Code). It involves tasks like **Register Allocation** and **Instruction Selection**.

**Example of Generated Assembly-like Code (simplified):**

```assembly
# T1 = pow(r, 2)
LOAD R1, r      # Load value of 'r' into Register 1
CALL pow, R1, 2 # Call the pow function, store result in R1 (or a temp reg)

# T2 = 3.14 & T1
LOADF R2, 3.14  # Load float 3.14 into Register 2
AND R2, R1      # Perform the bitwise AND operation (likely on integer representations)

# area = T2
STORE R2, area  # Store the result from R2 into the memory location for 'area'
```

-----
