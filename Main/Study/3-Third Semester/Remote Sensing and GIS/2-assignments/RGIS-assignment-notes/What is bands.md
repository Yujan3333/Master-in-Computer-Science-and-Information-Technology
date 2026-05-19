#RGIS #third-semester 

![Image](https://images.openai.com/static-rsc-4/eid4buXeqFF2Wc6_fj47A4jAHsRZYU-4i2iAZhAnrRw-RgTAFBBuQelQWoAX7dM25BhnIdsjfjrUHbkv3DQUs3qmE0-DdyPezGp4PLTYSsbXWVO5BkOBsimZAH4bIDsLTQ0lIBkchXitZe-iPp-OUnzSF0wDFzJhOBVt9qZiMl61Mmcd6Z65B1GR4f3d9TRg?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/8QIqyOhHBddq8NMKnYg4-5t6Q-qnGzpXUxFR_Ywni2V_BSUd_qeyySGF-2Q7oY6_lVDJssppf8VXo47SQIYhEYPZuIDO_Ru3PeQqqq85Ypm4dqwS26ZNKQ6fKl3nfQpBAYhc1Z61R1xtIPv2vTJrX2zWH4jgyTwFZt40dFf1zlaglZvOtODEa3UQfElrIAyQ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/TRgyn_af--vYCOtQ7OLSr17ZPzp0iNxED2AelSpMQI7oJlXwiHTyW-TL9Kcp5iJinPGthJm0hN8G_CmTf0rLo_RMMpkcatx7ysQRtXTUBajwXb9iaBd3_w6xXpaMBpXHpLX_sEp9Seppp2GFWK9zdt998d_1qP3mzSQZ5JtP9aQH6wTiBNhskGscaJyY6rgt?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/OBTNbN-O-5sbYPzSKZ7-iHUGMWqVhI-ENBL5_JaucUjn8Eb2gzIiWYL9uLc4ZfX3T5wUd2ezX0o9GUypKzXpcVzTwjNvtgINZl0_59gbGvGProWMiXUArzW2uJl7z0vNzUySDa4xzEgZ-WHdAcB9Ceyyx8FsVCGD85QQIq7fROBLZiZknrelj8wZZYJ1i3v-?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/1-0NWxczqyhwsXFNmCnBxuhWW92iK61vffb8FrEYP0ui9pGl4a5vr-k_ghTuqQUUdgFlYbxxTphHbzUN1Z-UDbAg-BArPdJ3oU8bOVq0g_dKlRnVRV5gxeLdSSwFx0bqBINtRzT4J-n9N58CrYr06Pc4eXMSbZ9ON3AM-aEy70OE8SHeKXJMekWUpo7bJf5U?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/EUdkmLD53X-2TmqPBr_yceivmcPm78nz-S1_lyNue_wXFNqJeRGIJkYx4qJqXaUZ9sN3LXIU-EDJPTVNqrzio1QXrayWa7E1PSl1aYVc57qjMmUSQa__dCHkgQg6weGMHmkY8frC8V9b5Ctcyr6jjHH6M6ZjuFReTB6huZBXVg9EDnU5j6EKt81o4ASmnbul?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/1vCsNibxarTow0tTA8BDWUBaDTzZjZ-GP2NI--pDZB-OmCc99WK7YlMkxNZUadAE3_L5f3Gs7bPgPrOoYDg2-xmpg_ag-3_2NUzMcAnmPKnUEpPHmn47vbPpOdDu9VrnV2KmrOb-AMGyxEahPruUptJ4XcgUkgnGnxY4cmCjtC0jZpsCqLjacFLUx-1jtS4B?purpose=fullsize)

In Landsat satellite imagery, **bands** mean:

> separate layers/images captured in different types of light (wavelengths).

A normal camera captures mainly:

* Red
* Green
* Blue (RGB)

But Landsat 8 and Landsat 9 capture many additional wavelengths such as:

* Infrared
* Thermal
* Shortwave infrared

Each wavelength is stored as a separate image called a **band**.

---

# Simple Example

Imagine the satellite takes multiple photos of the same place:

| Band    | What It Captures |
| ------- | ---------------- |
| Band 2  | Blue light       |
| Band 3  | Green light      |
| Band 4  | Red light        |
| Band 5  | Near Infrared    |
| Band 10 | Thermal heat     |

So instead of one image, Landsat gives many image layers.

---

# Why Are Bands Important?

Different objects reflect light differently.

Example:

| Object             | Infrared Reflection |
| ------------------ | ------------------- |
| Healthy vegetation | Very high           |
| Water              | Very low            |
| Urban buildings    | Medium              |

That’s why infrared bands help identify vegetation very clearly.

---

# Why Vegetation Appears Red in FCC

For False Color Composite (FCC), you assign:

| Display Color | Landsat Band      |
| ------------- | ----------------- |
| Red           | Band 5 (Infrared) |
| Green         | Band 4            |
| Blue          | Band 3            |

Since plants strongly reflect infrared,
they appear bright red.

---

# What the Actual Files Look Like

After download you’ll see:

```text id="n5htht"
LC09_B1.TIF
LC09_B2.TIF
LC09_B3.TIF
LC09_B4.TIF
LC09_B5.TIF
```

Each `.TIF` file = one band.

---

# Think of Bands Like Filters

A very easy way to understand:

Imagine wearing different glasses:

* one sees normal colors,
* one sees heat,
* one sees vegetation better.

Each “view” = one spectral band.

The satellite stores each view separately.

---

# In QGIS

You combine multiple bands together to create:

* True color images
* False color images
* Classification maps

Example:

* B5 + B4 + B3 = FCC image

---

# Important Bands for Your Assignment

| Band | Use           |
| ---- | ------------- |
| B3   | Green         |
| B4   | Red           |
| B5   | Near Infrared |
| B10  | Thermal       |

Most likely you’ll mainly use:

* B3
* B4
* B5
