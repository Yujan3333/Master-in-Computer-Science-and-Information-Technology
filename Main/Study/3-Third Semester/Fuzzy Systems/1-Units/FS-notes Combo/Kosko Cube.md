#fuzzy-system #third-semester 

For a cube with side length $a$, one common coordinate assignment is:

| Vertex | Coordinates |
| ------ | ----------- |
| $A$    | $(0,0,0)$   |
| $B$    | $(a,0,0)$   |
| $C$    | $(a,a,0)$   |
| $D$    | $(0,a,0)$   |
| $E$    | $(0,0,a)$   |
| $F$    | $(a,0,a)$   |
| $G$    | $(a,a,a)$   |
| $H$    | $(0,a,a)$   |

Here:

* The **x-axis** represents width.
* The **y-axis** represents depth.
* The **z-axis** represents height.

So each coordinate is either **0** or **$a$**, giving the $2^3 = 8$ vertices of the cube.

### Visual arrangement

```
        H(0,a,a) -------- G(a,a,a)
        /|                 /|
       / |                / |
 E(0,0,a) -------- F(a,0,a) |
      |  |              |   |
      | D(0,a,0) ------ | C(a,a,0)
      | /               | /
      |/                |/
 A(0,0,0) -------- B(a,0,0)
```

### Cube centered at the origin

Sometimes it is more convenient to center the cube at $(0,0,0)$. Then the coordinates become:

| Vertex             | Coordinates |
| ------------------ | ----------- |
| $(-a/2,-a/2,-a/2)$ |             |
| $(a/2,-a/2,-a/2)$  |             |
| $(a/2,a/2,-a/2)$   |             |
| $(-a/2,a/2,-a/2)$  |             |
| $(-a/2,-a/2,a/2)$  |             |
| $(a/2,-a/2,a/2)$   |             |
| $(a/2,a/2,a/2)$    |             |
| $(-a/2,a/2,a/2)$   |             |

In this case, each coordinate is either $-\frac{a}{2}$ or $\frac{a}{2}$.

If you meant **Kosko's cube** (e.g., in fuzzy logic or another specific context), let me know—that is different from the ordinary geometric cube.
