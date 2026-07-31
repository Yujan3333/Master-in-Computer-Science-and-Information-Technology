#ippr #third-semester 

The main difference is **how many values each pixel stores**.

## 1. Binary Image

Each pixel stores **1 bit**.

Possible values:

* 0 = Black
* 1 = White

```text
⬛ ⬜ ⬛
⬜ ⬛ ⬜
```

Only two colors are possible.

---

## 2. Grayscale Image

Each pixel stores **one intensity value**.

Usually **8 bits**:


$$0 \text{ to } 255$$


```text
Pixel = 150
```

means the pixel is **medium gray**.

```text
0      64      128      192      255
Black → Dark → Gray → Light → White
```

One number per pixel.

---

## 3. Color Image (RGB)

A color image **does not have just one intensity value**.

Each pixel stores **three intensity values**:

* Red (R)
* Green (G)
* Blue (B)

Each ranges from **0 to 255**.

So one pixel is stored as


$$(R,;G,;B)$$


Example:

| Pixel         | Meaning    |
| ------------- | ---------- |
| (255,0,0)     | Pure Red   |
| (0,255,0)     | Pure Green |
| (0,0,255)     | Pure Blue  |
| (255,255,0)   | Yellow     |
| (255,255,255) | White      |
| (0,0,0)       | Black      |
| (128,128,128) | Gray       |

---

### Example of one pixel

Suppose a pixel has

```text
R = 200
G = 50
B = 30
```

The computer mixes

* lots of red,
* a little green,
* very little blue,

to produce a reddish color.

---

## Why 3 numbers?

Your monitor is made of tiny **red, green, and blue** light sources.

Each pixel on the screen actually looks like this:

```text
[R] [G] [B]
```

By changing the brightness (intensity) of each one, **millions of different colors** can be produced.

For example:

```text
(255,255,255) → White
(255,0,0)     → Red
(0,255,0)     → Green
(0,0,255)     → Blue
(255,255,0)   → Yellow
```

---

## Storage Comparison

| Image Type  | Values Stored Per Pixel      | Example       |
| ----------- | ---------------------------- | ------------- |
| Binary      | 1 value (0 or 1)             | 1             |
| Grayscale   | 1 intensity value            | 150           |
| Color (RGB) | 3 intensity values (R, G, B) | (200, 50, 30) |

---

### Easy way to remember

Think of a pixel as a small box:

* **Binary image:** One switch → ON or OFF (black or white).
* **Grayscale image:** One dimmer knob → controls **brightness** from black to white.
* **Color image:** Three dimmer knobs → one each for **Red**, **Green**, and **Blue**. By adjusting all three, almost any color can be created.

So, in image processing:

* **Grayscale image:** **1 intensity value per pixel**.
* **Color image:** **3 intensity values per pixel (R, G, B)**.
