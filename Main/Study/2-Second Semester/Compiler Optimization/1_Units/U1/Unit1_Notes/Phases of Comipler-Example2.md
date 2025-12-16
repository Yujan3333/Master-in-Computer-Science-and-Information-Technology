
## ⚙️ `Position = initial + rate * 60`

### 1. Lexical Analysis (Scanning)

**Input:** Stream of characters: `P o s i t i o n = i n i t i a l + r a t e * 6 0`
**Process:** The Lexical Analyzer reads the characters and groups them into meaningful tokens. It uses rules to distinguish identifiers, constants, and operators.

| Lexeme | Token Name | Attribute Value |
| :--- | :--- | :--- |
| `Position` | **ID** | Pointer to Symbol Table for "Position" |
| `=` | **ASSIGN\_OP** | |
| `initial` | **ID** | Pointer to Symbol Table for "initial" |
| `+` | **ADD\_OP** | |
| `rate` | **ID** | Pointer to Symbol Table for "rate" |
| `*` | **MUL\_OP** | |
| `60` | **NUM** | Value $60$ (Type: `int`) |

**Output:** A stream of tokens passed to the next phase:
$$\langle \text{ID}, \text{Position} \rangle \langle \text{ASSIGN\_OP} \rangle \langle \text{ID}, \text{initial} \rangle \langle \text{ADD\_OP} \rangle \langle \text{ID}, \text{rate} \rangle \langle \text{MUL\_OP} \rangle \langle \text{NUM}, 60 \rangle$$

-----

### 2. Syntax Analysis (Parsing)

**Input:** Stream of tokens.
**Process:** The Parser checks if the token sequence forms a valid statement according to the language's grammar. It recognizes the order of operations (*multiplication* before *addition*) and constructs an **Abstract Syntax Tree (AST)**.
**Output:** An AST, structured as follows:

  * **Root:** `ASSIGN_OP`
  * **Left Child:** `ID: Position`
  * **Right Child (Expression):** `ADD_OP`
      * **Left Child of ADD:** `ID: initial`
      * **Right Child of ADD:** `MUL_OP`
          * **Left Child of MUL:** `ID: rate`
          * **Right Child of MUL:** `NUM: 60`

-----

### 3. Semantic Analysis

**Input:** Abstract Syntax Tree.
**Process:** The analyzer checks for type compatibility and declaration correctness.

  * **Declaration Check:** Ensures `Position`, `initial`, and `rate` have all been declared.
  * **Type Checking:**
      * If `rate` is a `float` and `60` is an `int`, the `*` operation will likely result in a `float` (due to type coercion).
      * The `+` operation will then involve `initial` (e.g., `float`) and the result of the multiplication (`float`). The result will be a `float`.
      * Finally, the assignment `=` ensures the final computed value's type is compatible with the type of `Position`.

**Output:** An **Annotated AST**, including type information and any implicit type conversion nodes.

-----

### 4. Intermediate Code Generation

**Input:** Annotated AST.
**Process:** The statement is translated into a simple, three-address code (TAC) format, which explicitly names the temporary results.

**Example of Three-Address Code:**

1.  `T1 = rate * 60` (Calculate the product first due to precedence)
2.  `T2 = initial + T1` (Add the product to `initial`)
3.  `Position = T2` (Assign the final result)

-----

### 5. Code Optimization

**Input:** Intermediate Code (TAC).
**Process:** The optimizer attempts to make the code faster or smaller.

  * **Constant Folding:** If `60` were a complex constant expression, it would be simplified here, but here it is already a simple constant.
  * If `rate` and `initial` are variables whose values don't change inside a surrounding loop, the calculations could be subject to **Loop-Invariant Code Motion**.

**Output:** Optimized Intermediate Code (likely the same TAC in this simple case).

-----

### 6. Code Generation

**Input:** Optimized Intermediate Code.
**Process:** The code is translated into the target machine's instruction set (Assembly or Machine Code), including register allocation.

**Example of Generated Assembly-like Code (simplified for a floating-point calculation):**

```assembly
# T1 = rate * 60
LOADF R1, rate       # Load value of 'rate' into floating-point Register 1
LOADF R2, 60.0       # Load the constant 60 (as a float) into Register 2
MUL R1, R1, R2       # R1 = R1 * R2 (T1 now in R1)

# T2 = initial + T1
LOADF R3, initial    # Load value of 'initial' into Register 3
ADD R1, R3, R1       # R1 = R3 + R1 (T2 now in R1)

# Position = T2
STORE R1, Position   # Store the result from R1 into the memory location for 'Position'
```

-----
