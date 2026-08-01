#ippr #third-semester 
### LZW (Lempel–Ziv–Welch) Example

**Input String:** `ABABABA`

**Initial Dictionary**

| Code | Symbol |
| ---- | ------ |
| 65   | A      |
| 66   | B      |

(Assume ASCII codes for simplicity.)

| Step | Current String (W) | Next Char (K) | WK in Dictionary? | Output    | Add to Dictionary |
| ---- | ------------------ | ------------- | ----------------- | --------- | ----------------- |
| 1    | A                  | B             | No                | A (65)    | 256 → AB          |
| 2    | B                  | A             | No                | B (66)    | 257 → BA          |
| 3    | A                  | B             | Yes               | -         | W = AB            |
| 4    | AB                 | A             | No                | AB (256)  | 258 → ABA         |
| 5    | A                  | B             | Yes               | -         | W = AB            |
| 6    | AB                 | A             | Yes               | -         | W = ABA           |
| End  | ABA                | -             | -                 | ABA (258) | -                 |

### Final Output Codes

```
65, 66, 256, 258
```

### Final Dictionary

| Code | String |
| ---- | ------ |
| 256  | AB     |
| 257  | BA     |
| 258  | ABA    |

### Exam Tip (5 Marks)

**Algorithm**

1. Initialize dictionary with all single characters.
2. Read the longest string already in the dictionary.
3. Output its code.
4. Add **(matched string + next character)** to the dictionary.
5. Repeat until the input ends.


