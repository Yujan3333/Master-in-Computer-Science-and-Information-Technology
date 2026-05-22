#assignment #fuzzy-system

- [Scaling and Clipping Part Explained](FS-assignments/Scaling%20and%20Clipping%20Part%20Explained.md)

# Given Fuzzy Sets

## Input Fuzzy Sets

### Low Mixture

$$\mu_{LM}=\left\{\frac{0}{2}+\frac{0.3}{5}+\frac{0.5}{8}+\frac{1}{11}+\frac{0.6}{14}+\frac{0.3}{17}+\frac{0}{20}\right\}$$

### High Mixture

$$\mu_{HM}=\left\{\frac{0}{1}+\frac{0.2}{2}+\frac{0.4}{6}+\frac{0.8}{8}+\frac{0.5}{10}+\frac{0.1}{11}+\frac{0}{12}\right\}$$

### Very Pure

$$\mu_{VP}=\left\{\frac{0}{5}+\frac{0.3}{10}+\frac{0.7}{15}+\frac{1}{20}+\frac{0.8}{25}+\frac{0.3}{40}+\frac{0}{45}\right\}$$

### Slightly Pure

$$\mu_{SP}=\left\{\frac{0}{3}+\frac{0.25}{5}+\frac{0.4}{10}+\frac{0.7}{20}+\frac{0.5}{25}+\frac{0.1}{30}+\frac{0}{35}\right\}$$

---

# Output Fuzzy Sets

### Excellent Quality

$$\mu_{EQ}=\left\{\frac{0}{34}+\frac{0.3}{40}+\frac{0.5}{45}+\frac{1}{50}+\frac{0.6}{55}+\frac{0.3}{60}+\frac{0}{65}\right\}$$

### Good Quality

$$\mu_{GQ}=\left\{\frac{0}{6}+\frac{0.4}{10}+\frac{0.6}{15}+\frac{0.8}{20}+\frac{0.5}{25}+\frac{0.3}{30}+\frac{0}{39}\right\}$$

---

# Fuzzy Rules

## Rule 1

If mixture is low OR purity is very pure, then quality is excellent.

## Rule 2

If mixture is high AND purity is slightly pure, then quality is good.

---

# Given Inputs

$$x_1=8 \quad (\text{mixture})$$

$$x_2=20 \quad (\text{purity})$$

---

# Step 1: Find Membership Values

## For mixture = 8

From low mixture set:

$$\mu_{LM}(8)=0.5$$

From high mixture set:

$$\mu_{HM}(8)=0.8$$

---

## For purity = 20

From very pure set:

$$\mu_{VP}(20)=1$$

From slightly pure set:

$$\mu_{SP}(20)=0.7$$

---

# Step 2: Rule Firing Strength

## Rule 1 (OR Operation)

Using Mamdani OR:

$$\alpha_1=\max(0.5,1)=1$$

Therefore, Rule 1 fires with strength:

$$\alpha_1=1$$

Output: Excellent Quality clipped/scaled at 1.

Since clipping at 1 does not change the set:

$$\mu_{EQ}'=\mu_{EQ}$$

---

## Rule 2 (AND Operation)

Using Mamdani AND:

$$\alpha_2=\min(0.8,0.7)=0.7$$

Output: Good Quality clipped/scaled at 0.7.

---

# Step 3: Clipping Method

Clip Good Quality at 0.7.

Original Good Quality:

$$\mu_{GQ}=\left\{\frac{0}{6}+\frac{0.4}{10}+\frac{0.6}{15}+\frac{0.8}{20}+\frac{0.5}{25}+\frac{0.3}{30}+\frac{0}{39}\right\}$$

After clipping at 0.7:

$$\mu_{GQ}^{clip}=\left\{\frac{0}{6}+\frac{0.4}{10}+\frac{0.6}{15}+\frac{0.7}{20}+\frac{0.5}{25}+\frac{0.3}{30}+\frac{0}{39}\right\}$$

---

# Step 4: Aggregation (Max Operation)

Combine Excellent Quality and Clipped Good Quality.

$$\mu_Y=\mu_{EQ}\cup\mu_{GQ}^{clip}$$

Aggregated output:

$$\mu_Y=\left\{\frac{0}{6},\frac{0.4}{10},\frac{0.6}{15},\frac{0.7}{20},\frac{0.5}{25},\frac{0.3}{30},\frac{0}{34},\frac{0.3}{40},\frac{0.5}{45},\frac{1}{50},\frac{0.6}{55},\frac{0.3}{60},\frac{0}{65}\right\}$$

---

# Step 5: Defuzzification (Centroid Method)

Formula:

$$y^*=\frac{\sum \mu(y_i)y_i}{\sum \mu(y_i)}$$

## Numerator

$$=(0.4\times10)+(0.6\times15)+(0.7\times20)+(0.5\times25)+(0.3\times30)+(0.3\times40)+(0.5\times45)+(1\times50)+(0.6\times55)+(0.3\times60)$$

$$=4+9+14+12.5+9+12+22.5+50+33+18$$

$$=184$$

## Denominator

$$=0.4+0.6+0.7+0.5+0.3+0.3+0.5+1+0.6+0.3$$

$$=5.2$$

Therefore,

$$y^*=\frac{184}{5.2}$$

$$y^*=35.38$$

---

# Final Answer (Clipping Method)

$$\boxed{y^*\approx35.38}$$

Hence, the defuzzified quality of the product is:

$$\boxed{35.38}$$

---

# Scaling Method

For scaling, multiply all membership values of Good Quality by 0.7.

$$\mu_{GQ}^{scale}=\left\{\frac{0}{6}+\frac{0.28}{10}+\frac{0.42}{15}+\frac{0.56}{20}+\frac{0.35}{25}+\frac{0.21}{30}+\frac{0}{39}\right\}$$

Aggregate with Excellent Quality using max operator:

$$\mu_Y=\left\{\frac{0}{6},\frac{0.28}{10},\frac{0.42}{15},\frac{0.56}{20},\frac{0.35}{25},\frac{0.21}{30},\frac{0}{34},\frac{0.3}{40},\frac{0.5}{45},\frac{1}{50},\frac{0.6}{55},\frac{0.3}{60},\frac{0}{65}\right\}$$

---

# Defuzzification for Scaling Method

## Numerator

$$=(0.28\times10)+(0.42\times15)+(0.56\times20)+(0.35\times25)+(0.21\times30)+(0.3\times40)+(0.5\times45)+(1\times50)+(0.6\times55)+(0.3\times60)$$

$$=2.8+6.3+11.2+8.75+6.3+12+22.5+50+33+18$$

$$=170.85$$

## Denominator

$$=0.28+0.42+0.56+0.35+0.21+0.3+0.5+1+0.6+0.3$$

$$=4.52$$

Therefore,

$$y^*=\frac{170.85}{4.52}$$

$$y^*\approx37.8$$

---

# Final Answer (Scaling Method)

$$\boxed{y^*\approx37.8}$$