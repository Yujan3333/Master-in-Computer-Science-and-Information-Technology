#fuzzy-system #third-semester 
Good question. In your example, the centroid step is actually **skipped** by saying:

> "After calculation, assume FanSpeed = 625 RPM."

Let's actually perform the centroid calculation.

---

# Step 7: Final Aggregated Output

After MAX aggregation, suppose the final fuzzy output (after clipping) is sampled at these fan speeds:

| Fan Speed (RPM) | Membership |
| --------------: | ---------: |
|             250 |          0 |
|             375 |        0.5 |
|             500 |        0.5 |
|             625 |        0.5 |
|             750 |       0.25 |
|             875 |       0.25 |
|            1000 |       0.25 |

These values come from the aggregated graph:

* Medium set clipped at **0.5**
* Fast set clipped at **0.25**
* Combined using **MAX**

---

# Step 8: Apply the centroid formula

Since we have discrete sample points, use

$$
z=\frac{\sum x_i\mu(x_i)}{\sum\mu(x_i)}
$$

---

## Numerator

Multiply each fan speed by its membership.

|  RPM | Membership | Product |
| ---: | ---------: | ------: |
|  250 |          0 |       0 |
|  375 |        0.5 |   187.5 |
|  500 |        0.5 |     250 |
|  625 |        0.5 |   312.5 |
|  750 |       0.25 |   187.5 |
|  875 |       0.25 |  218.75 |
| 1000 |       0.25 |     250 |

Total:

$$
0+187.5+250+312.5+187.5+218.75+250
=1406.25
$$

---

## Denominator

$$
0+0.5+0.5+0.5+0.25+0.25+0.25
=2.25
$$

---

## Final centroid

$$
z=\frac{1406.25}{2.25}
$$

$$
z=625\ \text{RPM}
$$

Therefore,

$$
\boxed{\text{Fan Speed}=625\ \text{RPM}}
$$

---

# Why did we choose those RPM values?

Those points are **sampled from the final aggregated membership graph**. In a real continuous Mamdani system, the centroid is

$$
z=\frac{\int x,\mu(x),dx}{\int\mu(x),dx}
$$

using the **entire aggregated curve**.

However, in many university numerical problems, the graph is replaced by a table of sampled values, and you use

$$
z=\frac{\sum x_i\mu(x_i)}{\sum\mu(x_i)}.
$$

---

## In an actual exam

There are two common cases:

1. **A table of output memberships is given** → Use the discrete centroid formula:
   $$
   z=\frac{\sum x_i\mu(x_i)}{\sum\mu(x_i)}.
   $$

2. **Only the output membership graph is given** (triangles/trapezoids after clipping) → Compute the centroid of the **area under the aggregated graph**, usually using geometry (areas and centroids of simple shapes) or integration if required.

In your example, the author jumped directly to **625 RPM** without showing the intermediate centroid calculation. The calculation above is one valid way to show that step using discrete sampling. If your exam expects the **graphical centroid calculation** from the clipped triangles and trapezoids (without converting to a table), I can also show that method step by step.
