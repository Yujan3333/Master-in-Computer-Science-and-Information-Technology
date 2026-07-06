#exam-paper-answer #mid-term #fuzzy-system 

Yes. I’ll solve all 3 questions clearly.

---

# 1(a) Mild Temperature using triangular membership

Given:

```text
X = {5,10,15,20,25,...,80,85,90}
a = 20, b = 45, c = 75
```

Triangular membership:

```text
μM(x) = 0,                x ≤ 20
μM(x) = (x - 20)/(45-20), 20 < x ≤ 45
μM(x) = (75 - x)/(75-45), 45 < x < 75
μM(x) = 0,                x ≥ 75
```

So:

```text
μM(x) = (x-20)/25  for 20 < x ≤ 45
μM(x) = (75-x)/30  for 45 < x < 75
```

## Mild Temperature fuzzy set

```text
Mild =
{
0/5, 0/10, 0/15, 0/20,
0.2/25, 0.4/30, 0.6/35, 0.8/40, 1/45,
0.83/50, 0.67/55, 0.5/60, 0.33/65, 0.17/70,
0/75, 0/80, 0/85, 0/90
}
```

## Is Mild Temperature convex?

A triangular fuzzy set is always **convex** because membership increases up to the peak and then decreases.

```text
0 → 0.2 → 0.4 → 0.6 → 0.8 → 1 → 0.83 → 0.67 → 0.5 → 0.33 → 0.17 → 0
```

So, **Mild Temperature is convex**.

---

# 1(b) Low Temperature = Complement of Mild

Formula:

```text
μLow(x) = 1 - μMild(x)
```

## Low Temperature fuzzy set

```text
Low =
{
1/5, 1/10, 1/15, 1/20,
0.8/25, 0.6/30, 0.4/35, 0.2/40, 0/45,
0.17/50, 0.33/55, 0.5/60, 0.67/65, 0.83/70,
1/75, 1/80, 1/85, 1/90
}
```

## Is Low Temperature normal?

A fuzzy set is **normal** if at least one element has membership value **1**.

Here Low has membership 1 at:

```text
5, 10, 15, 20, 75, 80, 85, 90
```

So, **Low Temperature is normal**.

---

# 1(c) Support and Boundary of Mild Temperature

## Support

Support means:

```text
Support(Mild) = {x | μMild(x) > 0}
```

So:

```text
Support(Mild) = {25, 30, 35, 40, 45, 50, 55, 60, 65, 70}
```

## Boundary

Boundary means:

```text
Boundary(Mild) = {x | 0 < μMild(x) < 1}
```

So remove membership 0 and membership 1.

```text
Boundary(Mild) = {25, 30, 35, 40, 50, 55, 60, 65, 70}
```

45 is not boundary because:

```text
μMild(45) = 1
```

---

# 1(d) Strict alpha cut of Low Temperature for α = 0.3

Strict alpha cut means:

```text
Lowα = {x | μLow(x) > α}
```

Here:

```text
α = 0.3
```

So choose all values where:

```text
μLow(x) > 0.3
```

From Low set:

```text
Low =
{
1/5, 1/10, 1/15, 1/20,
0.8/25, 0.6/30, 0.4/35, 0.2/40, 0/45,
0.17/50, 0.33/55, 0.5/60, 0.67/65, 0.83/70,
1/75, 1/80, 1/85, 1/90
}
```

Strict alpha cut:

```text
Low0.3 = {5,10,15,20,25,30,35,55,60,65,70,75,80,85,90}
```

Note:

```text
40 is not included because 0.2 < 0.3
45 is not included because 0 < 0.3
50 is not included because 0.17 < 0.3
```

---

# 1(e) Prototype of Mild Temperature

Prototype means the element having maximum membership value.

For Mild:

```text
μMild(45) = 1
```

Therefore:

```text
Prototype of Mild Temperature = 45
```

---

# 2. Relation R over Mild and Low Temperature

A fuzzy relation between Mild and Low can be created using Cartesian product:

```text
μR(x,y) = min( μMild(x), μLow(y) )
```

So:

```text
R = Mild × Low
```

## X-projection of R

Formula:

```text
πX(R)(x) = max over y [ μR(x,y) ]
```

Since Low is normal and has maximum value 1:

```text
πX(R)(x) = μMild(x)
```

Therefore:

```text
X-projection = Mild Temperature
```

```text
πX(R) =
{
0/5, 0/10, 0/15, 0/20,
0.2/25, 0.4/30, 0.6/35, 0.8/40, 1/45,
0.83/50, 0.67/55, 0.5/60, 0.33/65, 0.17/70,
0/75, 0/80, 0/85, 0/90
}
```

## Y-projection of R

Formula:

```text
πY(R)(y) = max over x [ μR(x,y) ]
```

Since Mild is also normal and has maximum value 1:

```text
πY(R)(y) = μLow(y)
```

Therefore:

```text
Y-projection = Low Temperature
```

```text
πY(R) =
{
1/5, 1/10, 1/15, 1/20,
0.8/25, 0.6/30, 0.4/35, 0.2/40, 0/45,
0.17/50, 0.33/55, 0.5/60, 0.67/65, 0.83/70,
1/75, 1/80, 1/85, 1/90
}
```

---

# 3. Fuzzy arithmetic operation A = A1 + A2 using Max-Min Extension Principle

Given:

```text
A1 = {0.1/20, 0.53/30, 0.8/40, 1/50, 0.7/60}
```

```text
A2 = {0.3/40, 0.4/50, 0.5/60, 1/70, 0.8/80, 0.33/90}
```

For addition:

```text
z = x + y
```

Membership formula:

```text
μA(z) = max min( μA1(x), μA2(y) )
```

where:

```text
z = x + y
```

Final result:

```text
A =
{
0.1/60,
0.3/70,
0.4/80,
0.5/90,
0.53/100,
0.8/110,
1/120,
0.8/130,
0.7/140,
0.33/150
}
```

---

# Final Short Answers

```text
1(a) Mild =
{
0/5, 0/10, 0/15, 0/20,
0.2/25, 0.4/30, 0.6/35, 0.8/40, 1/45,
0.83/50, 0.67/55, 0.5/60, 0.33/65, 0.17/70,
0/75, 0/80, 0/85, 0/90
}

Mild is convex.
```

```text
1(b) Low =
{
1/5, 1/10, 1/15, 1/20,
0.8/25, 0.6/30, 0.4/35, 0.2/40, 0/45,
0.17/50, 0.33/55, 0.5/60, 0.67/65, 0.83/70,
1/75, 1/80, 1/85, 1/90
}

Low is normal.
```

```text
1(c) Support(Mild) =
{25,30,35,40,45,50,55,60,65,70}

Boundary(Mild) =
{25,30,35,40,50,55,60,65,70}
```

```text
1(d) Strict alpha cut of Low for α = 0.3 =
{5,10,15,20,25,30,35,55,60,65,70,75,80,85,90}
```

```text
1(e) Prototype of Mild = 45
```

```text
2. R = Mild × Low

μR(x,y) = min(μMild(x), μLow(y))

X-projection = Mild
Y-projection = Low
```

```text
3. A = A1 + A2 =
{
0.1/60,
0.3/70,
0.4/80,
0.5/90,
0.53/100,
0.8/110,
1/120,
0.8/130,
0.7/140,
0.33/150
}
```
