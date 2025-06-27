## Question
Consider 4-bit grayscale image of resolution 5x5 image and 3x3 filter as below. Assume pixel values and filter of your own interest. Compute feature map and pooled feature map using 2x2 window. Use Max pooling.

#### ✅ In a 4-bit grayscale image:
Allowed pixel values: 0 to 15 (because 2⁴ = 16 possible values)

So each pixel must be represented using only one of those 16 values.

Example: a pixel can have values like 0, 1, 2, ..., 15.

#### ✅ In a 3-bit grayscale image:
Allowed pixel values: 0 to 7 (because 2³ = 8 possible values)

Each pixel is restricted to only these 8 levels.

Example: a pixel can be 0, 1, 2, ..., 7.

## Problem Setup

**5×5 4-bit Grayscale Image** (values: 0-15):
```
12   8   3  11  15
 6  14   9   2   7
10   5  13   8   4
 1  12   6  10  14
 9   3  11   5   8
```

**3×3 Filter** (Edge detection filter):
```
-1  -1  -1
-1   8  -1
-1  -1  -1
```

## Step 1: Convolution Operation

**Formula:** For each position (i,j):
`result[i][j] = Σ(input[i+m][j+n] × filter[m][n])`

### Convolution Calculations:

**Position (0,0):** Top-left 3×3 region
```
Input region:    Filter:       Calculation:
12   8   3      -1  -1  -1     12×(-1) + 8×(-1) + 3×(-1) +
 6  14   9   ×  -1   8  -1  =   6×(-1) + 14×8 + 9×(-1) +
10   5  13      -1  -1  -1     10×(-1) + 5×(-1) + 13×(-1)

= -12 - 8 - 3 - 6 + 112 - 9 - 10 - 5 - 13 = 46
```

**Position (0,1):**
```
Input region:    Filter:       Calculation:
 8   3  11      -1  -1  -1     8×(-1) + 3×(-1) + 11×(-1) +
14   9   2   ×  -1   8  -1  =  14×(-1) + 9×8 + 2×(-1) +
 5  13   8      -1  -1  -1     5×(-1) + 13×(-1) + 8×(-1)

= -8 - 3 - 11 - 14 + 72 - 2 - 5 - 13 - 8 = 8
```

**Position (0,2):**
```
Input region:    Filter:       Calculation:
 3  11  15      -1  -1  -1     3×(-1) + 11×(-1) + 15×(-1) +
 9   2   7   ×  -1   8  -1  =  9×(-1) + 2×8 + 7×(-1) +
13   8   4      -1  -1  -1     13×(-1) + 8×(-1) + 4×(-1)

= -3 - 11 - 15 - 9 + 16 - 7 - 13 - 8 - 4 = -54
```

**Position (1,0):**
```
Input region:    Filter:       Calculation:
 6  14   9      -1  -1  -1     6×(-1) + 14×(-1) + 9×(-1) +
10   5  13   ×  -1   8  -1  =  10×(-1) + 5×8 + 13×(-1) +
 1  12   6      -1  -1  -1     1×(-1) + 12×(-1) + 6×(-1)

= -6 - 14 - 9 - 10 + 40 - 13 - 1 - 12 - 6 = -31
```

**Position (1,1):**
```
Input region:    Filter:       Calculation:
14   9   2      -1  -1  -1     14×(-1) + 9×(-1) + 2×(-1) +
 5  13   8   ×  -1   8  -1  =  5×(-1) + 13×8 + 8×(-1) +
12   6  10      -1  -1  -1     12×(-1) + 6×(-1) + 10×(-1)

= -14 - 9 - 2 - 5 + 104 - 8 - 12 - 6 - 10 = 38
```

**Position (1,2):**
```
Input region:    Filter:       Calculation:
 9   2   7      -1  -1  -1     9×(-1) + 2×(-1) + 7×(-1) +
13   8   4   ×  -1   8  -1  =  13×(-1) + 8×8 + 4×(-1) +
 6  10  14      -1  -1  -1     6×(-1) + 10×(-1) + 14×(-1)

= -9 - 2 - 7 - 13 + 64 - 4 - 6 - 10 - 14 = -1
```

**Position (2,0):**
```
Input region:    Filter:       Calculation:
10   5  13      -1  -1  -1     10×(-1) + 5×(-1) + 13×(-1) +
 1  12   6   ×  -1   8  -1  =  1×(-1) + 12×8 + 6×(-1) +
 9   3  11      -1  -1  -1     9×(-1) + 3×(-1) + 11×(-1)

= -10 - 5 - 13 - 1 + 96 - 6 - 9 - 3 - 11 = 38
```

**Position (2,1):**
```
Input region:    Filter:       Calculation:
 5  13   8      -1  -1  -1     5×(-1) + 13×(-1) + 8×(-1) +
12   6  10   ×  -1   8  -1  =  12×(-1) + 6×8 + 10×(-1) +
 3  11   5      -1  -1  -1     3×(-1) + 11×(-1) + 5×(-1)

= -5 - 13 - 8 - 12 + 48 - 10 - 3 - 11 - 5 = -19
```

**Position (2,2):**
```
Input region:    Filter:       Calculation:
13   8   4      -1  -1  -1     13×(-1) + 8×(-1) + 4×(-1) +
 6  10  14   ×  -1   8  -1  =  6×(-1) + 10×8 + 14×(-1) +
11   5   8      -1  -1  -1     11×(-1) + 5×(-1) + 8×(-1)

= -13 - 8 - 4 - 6 + 80 - 14 - 11 - 5 - 8 = 11
```

## Feature Map (3×3):
```
 46    8  -54
-31   38   -1
 38  -19   11
```

## Step 2: Max Pooling (2×2 window)

Since we have a 3×3 feature map, we can apply 2×2 max pooling in overlapping or non-overlapping manner. 

**Method 1: Non-overlapping 2×2 windows**

**Top-left 2×2 block:**
```
 46    8
-31   38
Max = 46
```

**Remaining elements** (since 3×3 doesn't divide evenly into 2×2):
We can take additional windows or pad. Let's use overlapping windows:

**Top-right 2×2 block:**
```
  8  -54
 38   -1
Max = 38
```

**Bottom-left 2×2 block:**
```
-31   38
 38  -19
Max = 38
```

**Bottom-right 2×2 block:**
```
 38   -1
-19   11
Max = 38
```

## Final Pooled Feature Map (2×2):
```
46  38
38  38
```

## Alternative: Single Max Pool
If we use a single 2×2 max pooling on the entire 3×3 feature map:

**Taking top-left 2×2:**
```
 46    8
-31   38
Max = 46
```

**Final Result:** Single value = **46**

## Summary
- **Original Image:** 5×5 (25 pixels)
- **After Convolution:** 3×3 feature map (9 values)
- **After Max Pooling:** 2×2 or single value
- **Filter Effect:** The edge detection filter highlighted regions with high contrast
- **Dimensionality Reduction:** 25 → 9 → 4 (or 1) values

## Key Observations
1. The filter detected edges and high-contrast regions
2. Positive values indicate strong edge detection
3. Negative values indicate regions where the center pixel is lower than surrounding pixels
4. Max pooling preserved the strongest responses while reducing spatial dimensions