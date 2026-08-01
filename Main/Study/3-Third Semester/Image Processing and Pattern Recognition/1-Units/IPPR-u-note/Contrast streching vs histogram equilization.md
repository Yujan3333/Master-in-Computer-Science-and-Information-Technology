#ippr #third-semester 
## Contrast Stretching vs Histogram Equalization

| Contrast Stretching                                                                        | Histogram Equalization                                                            |
| ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| **1. Increases the intensity range** of an image.                                          | **Redistributes the intensity values** using the histogram.                       |
| **2. Uses a linear transformation** to stretch gray levels.                                | **Uses a nonlinear transformation** based on the CDF of the histogram.            |
| **3. Does not aim for a uniform histogram.**                                               | **Attempts to produce a nearly uniform histogram.**                               |
| **4. Requires only the minimum and maximum intensity values** ($r_{\min}$ and $r_{\max}$). | **Requires the image histogram, PDF, and CDF** for computation.                   |
| **5. Mainly improves overall contrast.**                                                   | **Enhances both contrast and hidden details**, especially in low-contrast images. |

### Memory Trick

* **Contrast Stretching = Stretch the gray levels.**
* **Histogram Equalization = Spread the histogram (pixel frequencies).**
