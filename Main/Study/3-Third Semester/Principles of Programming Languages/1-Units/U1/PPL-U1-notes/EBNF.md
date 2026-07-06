#PPL 

# EBNF (Extended Backus–Naur Form)

**EBNF (Extended Backus–Naur Form)** is an **extended version of BNF** used to describe the **syntax (grammar)** of programming languages in a simpler and more compact way.

It adds extra symbols to make grammar rules easier to write and read.

---

# Why do we need EBNF?

In BNF, if something can repeat or is optional, we need many production rules.

For example, in BNF:

```text
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

<number> ::= <digit>
           | <digit><number>
```

In EBNF, we can write it more simply:

```text
<number> = <digit> {<digit>}
```

This means:

* Start with one digit.
* Then **zero or more** additional digits.

So `5`, `42`, and `12345` are all valid numbers.

---

# Common EBNF Symbols

| Symbol | Meaning                   | Example         |              |
| ------ | ------------------------- | --------------- | ------------ |
| `=`    | is defined as             | `<digit> = "0"` |              |
| `      | `                         | OR              | `"+" \| "-"` |
| `[ ]`  | Optional (0 or 1 time)    | `["-"]`         |              |
| `{ }`  | Zero or more repetitions  | `{<digit>}`     |              |
| `( )`  | Group expressions         | `("+" \| "-")`  |              |
| `"`    | Terminal (literal symbol) | `"if"`          |              |

---

# Meaning of Each Symbol

## 1. Optional `[ ]`

Grammar:

```text
<number> = ["-"] <digit>
```

This means the minus sign is optional.

Valid examples:

```text
5
-7
```

---

## 2. Repetition `{ }`

Grammar:

```text
<number> = <digit> {<digit>}
```

Examples:

```text
7
45
1234
987654
```

`{<digit>}` means repeat `<digit>` **zero or more times**.

---

## 3. Choice `|`

Grammar:

```text
<operator> = "+" | "-" | "*" | "/"
```

Valid:

```text
+
-
*
/
```

---

## 4. Grouping `( )`

Grammar:

```text
<expression> = <number> { ("+" | "-") <number> }
```

This means:

* Start with one number.
* Then repeat:

  * either `+` or `-`
  * followed by another number.

Example:

```text
5+3
10-2+8
7+4-1
```

---

# Example 1: Identifier

Grammar:

```text
<identifier> = <letter> { <letter> | <digit> }
```

where

```text
<letter> = "A" | ... | "Z" | "a" | ... | "z"

<digit> = "0" | ... | "9"
```

Valid identifiers:

```text
age

student

x1

count25

ABC123
```

Invalid:

```text
1abc

-name

%
```

---

# Example 2: Integer

Grammar:

```text
<integer> = ["-"] <digit> {<digit>}
```

Valid:

```text
7

123

-98

45678
```

Invalid:

```text
--

A12

12A
```

---

# Example 3: Arithmetic Expression

Grammar:

```text
<expression> = <term> { ("+" | "-") <term> }

<term> = <factor> { ("*" | "/") <factor> }

<factor> = <number> | "(" <expression> ")"

<number> = <digit> {<digit>}
```

Valid expressions:

```text
5+3

10*4

8*(5+2)

100/20-3
```

---

# Example 4: If Statement

Grammar:

```text
<if-statement> =
"if" "(" <condition> ")" <statement> [ "else" <statement> ]
```

This means:

* Every `if` has a condition and a statement.
* The `else` part is optional.

Valid:

```java
if (x > 0)
    y = 1;
```

Also valid:

```java
if (x > 0)
    y = 1;
else
    y = 0;
```

---

# BNF vs EBNF

| BNF                    | EBNF                      |
| ---------------------- | ------------------------- |
| Basic grammar notation | Extended grammar notation |
| Longer rules           | Shorter and easier rules  |
| No built-in repetition | `{}` for repetition       |
| No optional notation   | `[]` for optional parts   |
| Harder to read         | Easier to read and write  |

---

## Example Comparison

### BNF

```text
<number> ::= <digit>
           | <digit><number>
```

### EBNF

```text
<number> = <digit> {<digit>}
```

Both define the same language, but the EBNF version is much shorter.

---

# Advantages of EBNF

* Easier to read and understand.
* Shorter grammar definitions.
* Built-in support for optional and repeated parts.
* Widely used for programming language specifications.

---

# Disadvantages of EBNF

* Different EBNF dialects use slightly different symbols.
* Not as universally standardized as basic BNF.
* Beginners must learn the meanings of symbols like `[]` and `{}`.

---

# Exam Answer (5 Marks)

**EBNF (Extended Backus–Naur Form)** is an extension of **BNF** used to define the syntax of programming languages in a more concise and readable way. It introduces additional symbols such as **`[]`** for optional elements, **`{}`** for repetition, **`|`** for alternatives, and **`()`** for grouping.

**Example:**

```text
<integer> = ["-"] <digit> {<digit>}
```

This grammar defines an integer as:

* an optional minus sign,
* followed by one digit,
* followed by zero or more additional digits.

Valid examples are `5`, `123`, and `-98`. EBNF is widely used in compiler design because it makes grammar specifications shorter, clearer, and easier to maintain.
