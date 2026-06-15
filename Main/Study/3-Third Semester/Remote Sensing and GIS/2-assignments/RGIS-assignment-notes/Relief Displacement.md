#RGIS #assignment 

# **1. Relief Displacement (with illustration + numerical solution)**

## **Concept (based on Bhatta’s Remote Sensing & Photogrammetry)**

Relief displacement is the **apparent outward shift of elevated objects** (like towers, buildings, trees) on an aerial photograph caused by their height above the ground.

### **Key points**

* Occurs only in **vertical aerial photographs**
* Objects appear to “lean away” from the principal point
* Displacement increases with:

  * object height ($h$)
  * distance from photo center ($r$)
* No displacement at the principal point (center of photo)

---

## **Illustration**

![Image](https://images.openai.com/static-rsc-4/7rWxIReiGrvqr--d8JkYbmNKEVo2UngYf1Jhn_UqTSSmRiA1raz7jY3Z1tcQIfjqnVi3GTrjYFq94d65NxIEDNxAUJyy-4Jm9t_CJ4a0PBq_rnLWqWhjvoSWHpExrzdACgn_OBL8e4Q61nv2cCT8SY11byrM7Mp7HN1ogrC6eeKOj5q7dZwrRc6VJHgwOd-E?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/CHD9Fr0dpiVy3JZPjK6Y87wXC6BHSASMv7oyRIYcIhQT2IdJbTK2rkeGmP_Q7cjhiHi5P5qG1QUM7LZgjk0mY-eHj6JY_GTImXUQszUxx4aDL7rPJBMeKF4iGfg-QbS_gJ0djLOVgib5jpelJICLOcV9SB4xGmSizZNdDX37ZdhEbaCJV_fNMdFWyxFGlinz?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/2wq2_K7RIFjiRrWY10lf6owu3y5IfzRgfnoKyX07wCrZi-9v8WQuPjHC8pKuDzIVj6kF2dtNvSndupYqNUwyEFOtqhqH13_qQAnU-aq95tBnKgWnzXZgKoOZUdCjZZmlrszfZYaqAenYsBfScNS8s3glhOlY-dnZis8f7gFtKv0ew0e1Npkh0q_Liulk7nLk?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/982giewQzeDaWD9O1tHJ6o_ii9kV9WYqMdg9uFDYp6PvlYSRV0qUCy91OOISsvqobXWlUnmUz7lgIyls4GwwdbuMJ7_ntfNUopw7P0OJVfoZhszhsX1nFLxtq3rIFKAtmNgv3tTAdnVTgJWIoZ9E7xeZ1MK7SFZO4ZgQZD6j-Vbisr7rWu833oHshd1lqANU?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/FAtGn3j8rh7g8nMhAhR63-jmxLQ8c3Alni83wJ4-xAugsw8QwVVqqnrgLPAx-9WoR0mSb1NuQq7zZSncEMI4T6dkfk6glzYEggXde2Vl59Qzykm9XaF_SmmuzcchqvWw9crMGd--URg7nNCKVEKqSL8fdLZxOg8fABQdjaZh9YC7kEq4jvONwc55yyFaat7y?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/dxO85KA2Sfk5HZ2BqqH4iP7bsNTsx7aken98aoxvPeWSR5YxyT9QGof6Q0KJ2JU3aNaLUx0oma73hwAdEuKCJxgy0LDLmjlKZl_0JQsJW8ILyCt_skF_WFC52Roi8AzWelivYxjjhFGSqg_nEJkkqgYpcU5seALvQZ4L88FFHlOl40RBntfGK7Wfkv5teyr5?purpose=fullsize)

---

## **Formula (from Bhatta photogrammetry theory)**

$$d=\frac{r \cdot h}{H}$$

Where:

* $d$ = relief displacement (mm)
* $r$ = radial distance from photo center (mm)
* $h$ = height of object (m)
* $H$ = flying height above ground (m)

Rearranging to find height:

$$h=\frac{d \cdot H}{r}$$

---

## **Given**

* $d = 2.5 , mm$
* $r = 55 , mm$
* $H = 1200 , m$

---

## **Step-by-step solution**

$$h=\frac{2.5 \times 1200}{55}$$

$$h=\frac{3000}{55}$$

$$h \approx 54.55 , m$$

---

## **Final Answer**

### **Height of the tower = 54.55 m**

---

## **Exam Tip (as per Bhatta style)**

* Always mention:

  > “Relief displacement is radial and increases with object height and distance from photo center.”

---
