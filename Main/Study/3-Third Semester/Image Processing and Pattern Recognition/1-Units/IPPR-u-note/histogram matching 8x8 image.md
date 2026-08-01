#ippr #third-semester #exam-paper-answer 

## Question Text

**3.** Consider the following two $8 \times 8$ images. Perform histogram matching for the image on the left using the reference image on the right and plot the histogram of the reference image and the resulting histogram of the matching. **(10)**

---

## Image Data Arrays

### **Original Image ($8 \times 8$)**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 5 | 7 | 7 | 5 | 8 | 7 | 8 |
| 7 | 2 | 6 | 2 | 6 | 5 | 6 | 8 |
| 6 | 9 | 7 | 7 | 0 | 7 | 2 | 7 |
| 6 | 6 | 1 | 7 | 6 | 7 | 7 | 5 |
| 9 | 6 | 0 | 7 | 8 | 2 | 6 | 7 |
| 2 | 8 | 8 | 2 | 7 | 6 | 7 | 8 |
| 7 | 3 | 2 | 6 | 1 | 7 | 5 | 8 |
| 9 | 9 | 5 | 6 | 7 | 7 | 7 | 7 |

---

### **Reference Image ($8 \times 8$)**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 6 | 7 | 8 | 5 | 0 | 6 | 8 |
| 7 | 2 | 6 | 2 | 6 | 2 | 6 | 7 |
| 8 | 6 | 9 | 2 | 0 | 7 | 3 | 7 |
| 7 | 6 | 1 | 4 | 6 | 0 | 5 | 9 |
| 9 | 7 | 0 | 9 | 8 | 4 | 6 | 7 |
| 9 | 8 | 9 | 4 | 7 | 1 | 7 | 8 |
| 7 | 3 | 5 | 5 | 1 | 3 | 5 | 7 |
| 5 | 8 | 8 | 4 | 6 | 2 | 7 | 6 |

---



To solve **Histogram Matching (Histogram Specification)**, follow these steps:

1. Compute the histogram of the **original image**.
2. Compute the histogram of the **reference image**.
3. Compute the PDF and CDF of both images.
4. Compute the transformation values.
5. Match each gray level of the original image to the closest gray level in the reference image using the CDFs.
6. Replace the pixels using the mapping.
7. Plot the reference histogram and the histogram of the matched image.

---
# ANSWER
# Step 1: Histogram of the Original Image

Count the occurrences of each gray level (0–9).

| Gray Level | Frequency |
| ---------- | --------: |
| 0          |         3 |
| 1          |         2 |
| 2          |         6 |
| 3          |         1 |
| 4          |         0 |
| 5          |         5 |
| 6          |        11 |
| 7          |        24 |
| 8          |         7 |
| 9          |         5 |

Total pixels

$$
N=64
$$

---

# Step 2: Histogram of the Reference Image

Count the occurrences of each gray level.

| Gray Level | Frequency |
| ---------- | --------: |
| 0          |         4 |
| 1          |         3 |
| 2          |         6 |
| 3          |         3 |
| 4          |         4 |
| 5          |         6 |
| 6          |        11 |
| 7          |        13 |
| 8          |         8 |
| 9          |         6 |

---

# Step 3: PDF of the Original Image

$$
p(r_k)=\frac{n_k}{64}
$$

| Gray | Frequency |    PDF |
| ---: | --------: | -----: |
|    0 |         3 | 0.0469 |
|    1 |         2 | 0.0313 |
|    2 |         6 | 0.0938 |
|    3 |         1 | 0.0156 |
|    4 |         0 | 0.0000 |
|    5 |         5 | 0.0781 |
|    6 |        11 | 0.1719 |
|    7 |        24 | 0.3750 |
|    8 |         7 | 0.1094 |
|    9 |         5 | 0.0781 |

---

# Step 4: CDF of the Original Image

| Gray |    CDF |
| ---: | -----: |
|    0 | 0.0469 |
|    1 | 0.0781 |
|    2 | 0.1719 |
|    3 | 0.1875 |
|    4 | 0.1875 |
|    5 | 0.2656 |
|    6 | 0.4375 |
|    7 | 0.8125 |
|    8 | 0.9219 |
|    9 | 1.0000 |

---

# Step 5: PDF of the Reference Image

| Gray | Frequency |    PDF |
| ---: | --------: | -----: |
|    0 |         4 | 0.0625 |
|    1 |         3 | 0.0469 |
|    2 |         6 | 0.0938 |
|    3 |         3 | 0.0469 |
|    4 |         4 | 0.0625 |
|    5 |         6 | 0.0938 |
|    6 |        11 | 0.1719 |
|    7 |        13 | 0.2031 |
|    8 |         8 | 0.1250 |
|    9 |         6 | 0.0938 |

---

# Step 6: CDF of the Reference Image

| Gray |    CDF |
| ---: | -----: |
|    0 | 0.0625 |
|    1 | 0.1094 |
|    2 | 0.2031 |
|    3 | 0.2500 |
|    4 | 0.3125 |
|    5 | 0.4063 |
|    6 | 0.5781 |
|    7 | 0.7813 |
|    8 | 0.9063 |
|    9 | 1.0000 |

---

# Step 7: Histogram Matching

Match each CDF value of the original image with the closest CDF value of the reference image.

| Original Gray | Original CDF | Closest Reference CDF | New Gray |
| ------------: | -----------: | --------------------: | -------: |
|             0 |       0.0469 |                0.0625 |        0 |
|             1 |       0.0781 |                0.0625 |        0 |
|             2 |       0.1719 |                0.2031 |        2 |
|             3 |       0.1875 |                0.2031 |        2 |
|             4 |       0.1875 |                0.2031 |        2 |
|             5 |       0.2656 |                0.2500 |        3 |
|             6 |       0.4375 |                0.4063 |        5 |
|             7 |       0.8125 |                0.7813 |        7 |
|             8 |       0.9219 |                0.9063 |        8 |
|             9 |       1.0000 |                1.0000 |        9 |

Therefore, the mapping is

| Original | Matched |
| -------- | ------- |
| 0 → 0    |         |
| 1 → 0    |         |
| 2 → 2    |         |
| 3 → 2    |         |
| 4 → 2    |         |
| 5 → 3    |         |
| 6 → 5    |         |
| 7 → 7    |         |
| 8 → 8    |         |
| 9 → 9    |         |

---

# Step 8: Matched Image

Replace every pixel according to the mapping.

$$
\begin{array}{cccccccc}
0&3&7&7&3&8&7&8\\
7&2&5&2&5&3&5&8\\
5&9&7&7&0&7&2&7\\
5&5&0&7&5&7&7&3\\
9&5&0&7&8&2&5&7\\
2&8&8&2&7&5&7&8\\
7&2&2&5&0&7&3&8\\
9&9&3&5&7&7&7&7
\end{array}
$$

---

# Step 9: Histogram of the Matched Image

| Gray Level | Frequency |
| ---------- | --------: |
| 0          |         5 |
| 1          |         0 |
| 2          |         7 |
| 3          |         5 |
| 4          |         0 |
| 5          |        11 |
| 6          |         0 |
| 7          |        24 |
| 8          |         7 |
| 9          |         5 |

---

# Histogram of the Reference Image

```text
Gray Level : Frequency

0 : ████
1 : ███
2 : ██████
3 : ███
4 : ████
5 : ██████
6 : ███████████
7 : █████████████
8 : ████████
9 : ██████
```

---

# Histogram of the Matched Image

```text
Gray Level : Frequency

0 : █████
1 :
2 : ███████
3 : █████
4 :
5 : ███████████
6 :
7 : ████████████████████████
8 : ███████
9 : █████
```

---

## Final Answer (Exam)

* Compute the histogram, PDF, and CDF of both the original and reference images.
* Match the original gray levels to the reference gray levels using the closest CDF values.
* The obtained mapping is:

$$
0\rightarrow0,;
1\rightarrow0,;
2\rightarrow2,;
3\rightarrow2,;
4\rightarrow2,;
5\rightarrow3,;
6\rightarrow5,;
7\rightarrow7,;
8\rightarrow8,;
9\rightarrow9
$$

* Replace all pixels using this mapping to obtain the histogram-matched image.
* Draw the reference histogram and the histogram of the matched image as shown above.
