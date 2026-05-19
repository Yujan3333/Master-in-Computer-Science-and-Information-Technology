#assignment #RGIS #lab 

# Complete Workflow: Landsat Data → QGIS → Processing → Classification

## STEP 1 — Download Landsat Data

Go to:

[USGS EarthExplorer](https://earthexplorer.usgs.gov?utm_source=chatgpt.com)

Search your area (example: Kathmandu).

Select:

* Landsat Collection 2
* Landsat 8-9 OLI/TIRS
* Level-1

Download the product.

---

# STEP 2 — What Format Will You Get?

You usually download a compressed file:

```text
LC09_L1TP_141041_20250510_20250512_02_T1.tar
```

or sometimes `.zip`

---

# STEP 3 — Extract the File

After extraction, you’ll see many files like:

```text
LC09_B1.TIF
LC09_B2.TIF
LC09_B3.TIF
LC09_B4.TIF
LC09_B5.TIF
...
LC09_MTL.txt
```

Important:

* `.TIF` = image bands
* each file = one spectral band

---

# STEP 4 — Which Bands Do You Need?

For FCC (False Color Composite):

| Band | Meaning       |
| ---- | ------------- |
| B5   | Near Infrared |
| B4   | Red           |
| B3   | Green         |

These three are most important.

---

# STEP 5 — Open QGIS

Open:
QGIS

---

# STEP 6 — Load Landsat Bands into QGIS

Go to:

```text
Layer → Add Layer → Add Raster Layer
```

Select:

* B5.tif
* B4.tif
* B3.tif

Click Open.

Now you’ll see grayscale images.

---

# STEP 7 — Create False Color Composite (FCC)

This is the most important visualization step.

## Right Click One Raster

```text
Properties → Symbology
```

Change:

```text
Render Type → Multiband Color
```

Assign:

| Color | Band |
| ----- | ---- |
| Red   | B5   |
| Green | B4   |
| Blue  | B3   |

Click Apply.

---

# Result

Vegetation becomes:

* bright red

Urban areas:

* cyan/gray

Water:

* dark blue/black

![Image](https://images.openai.com/static-rsc-4/0g36ZT5r2VqerwgOxAVQJ7PNpv1X2V8-IyBQkwVRTx-UO7cZ5UXtYV3i1W-q7Mnmlu2yvqBi9M6emoMPf2hLw8CMZgYVrTJUQkKzv5srauAefu0wf8SuFyfsjdnemW2LO8yoDMrBi7FbiYEcMpkT6CEaoxVOqzd9mNrX39AQ1pjWZUXgj9sfAr21l5Y-OG-s?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Xb_OvF87w1UBNgqcIbSvXPAOYPFuYaDaYW7MzIpCf5ULskRnz73zsYbJ48eL0ATnQ7BupYxox5c7Ga3CkGrDI_Wjc-otq7LM8PEs5EMZ7vCjwqernxFeSHcJIQOtPkMIXGEtyXvZ_kglv6VT5lMRwqEcARMhmphF1i8tt7l93j0k1u_dGDjgJS40eHWzE7g-?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/oE2QE1yxE6nt7I-I3NRF_bqX9G1OPzGvdWD0Loktk7sweHxNyxj7LPhu6M9yx9L4yKK8GzxtOJ4s4rzjPlwbP7GyyeREunzstqYmBahtUfTX8yBgwqvzUvcV_69FcKKFaMkXCREMZkE6eoBeJ5e4NpDWt07sC15GRVxnZcER1MgUkbtIVsET6-34hhkVZk0e?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ie-EGAHveH8HjpQmuDXAaJLksyEIUEKuyVu8E3ZpwTNfX35LuRin9UDdyfpC3Cbs_Dmf54xbE5lyFDdzssBP9kE8c4-8EftE8NjtkOjBehtF8xTa4Wu7xR-xrS2Q9Taa8gwtjTfLSVDe9FceDUyv6DX5TfPJvIUeRXwKyHLgzXyUYL-9s6zxXxn15DemQj1E?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/i0C76cN_ZVlrIiFpTXqLSyB7eh9yD4Q4NWmAk60Oh8HrYYXQrSBuiL76vsKsXqvFzHgRA_a8v2QsdLx5COiPNvWvzTuRQcsw-NUqajL2TM3sId6tKlC9e-gQpN7by3Uhbcr-1PAAxU-jhfa8Y395mUnLHWbquoBPFp_Q2TWfSM3zNwtUVn9aRmYM4Um6XtNt?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/TEp_SBGtBOTc7-QdRKqSWE_i0Y7FyI8BOm4ONXZFs-ETINH61UfUo2KSLhg3tlklZURlooCNixGn0FvfUpdL7S_deUQVvsAESoV6eI1nMRg-ktqbxjW3R8rM92-3CAbW6fpxDWoU7X3z9Jm62BU2HXnq0Eto07C-JAUBv8cJS0cpPCq3Enc6iZEWUW6d6X5T?purpose=fullsize)

---

# STEP 8 — Image Enhancement

## Method 1: Contrast Stretching

Go to:

```text
Raster Properties → Symbology
```

Select:

```text
Min/Max Value Settings
→ Stretch to MinMax
```

Apply.

### Effect

Image becomes clearer and brighter.

---

## Method 2: Histogram Equalization

Go to:

```text
Raster → Miscellaneous
```

Use enhancement tools/plugins.

### Effect

Improves visibility of darker/lighter regions.

---

# STEP 9 — Spatial Filtering

## A. Smoothing (Low Pass Filter)

Purpose:

* remove noise
* blur image slightly

Go to:

```text
Processing Toolbox
→ Filter
→ Smoothing
```

---

## B. Edge Detection (High Pass Filter)

Purpose:

* sharpen boundaries
* highlight roads/buildings

Go to:

```text
Processing Toolbox
→ Edge Detection
```

![Image](https://images.openai.com/static-rsc-4/s9NEV_ug0JA1l23m4fjHrR4wVWeXqhtPmspe9u_UewvWuGScxmRKya4nBq1RTHF4cmvOPMuKxOl6wCbUA8Nm8T4HhhO_5PQoD573EfElP57gar2JkszaTDVUmQxumHPiMtMfB2nrXz0joYFuw3j8Fr6Utpbbp3wQXmGlAYrr7LHykjuXp3OZs1jD1TLIpy9x?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ky1z_rhIOyHUt-DOHDwuzt-XXyMoyCfo3h60qs6OlNuQu8vo-55brXPQpkwJ0AiUBnw36vJ7I5Inw8NJ6HvIAGkFufhsP4HqJT9eF0oODOjBMBd8bXTr9WHWzKA-uDXfzEpLtz6F4GB-Mi5sulHgjTfmivNDIdHXI8A8ByeIAvrODeRX0f3byMsgbwj_BT6a?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/c5dVIBY5ECcRSEXTjtjGa7pIgece5MNeL9URSYaLfhVazh7KKrVLzwV6Avo0ubAhtaD5RIDdUGm6R-qRiS3rqRei-nyhkwhpX8GGty7YbQCD5OqVO0vH4gbY5IZiMMTjdDP7MJTFTgrKiKgp7dhfmOb9x4HiVmwVNTRQ2UF80MeT5RNcwAXqfnLvhCej6J41?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/hKeg-dQUqZ3UlJk8YqJ2cjaxgIPPj837TykGlC-jhvj1-P6TYdSiqNZcOrpJaYPNeomwPNozSq7jrWT2aJnSrID19-jliknvoECJtv84emEFOwrak_Lykif5P89EiTU90CKM0RJglyaqK-dYTlFB8LZXdpLK4FztnofbWqeVXW2YUeU3Yji8j30QjSQv1GU7?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/CmdiMyuPQBq2lv046Fzml9A1FRCP79h5eStRExB-7WgkwIhnFHY6-i-JvFzMJ3qQjUOrusv3EbOdBtbqq6yeHZXgC4aEBv2mX7Q02_yWJ5BnvWXgkQDk7R6-9vWHbbFbjM-3-JlVH-Ds1izufjH85XgPrBcm3SL0iKzXZ32TSyuYADZCWgvSHFHp051S-QPF?purpose=fullsize)

---

# STEP 10 — Classification

## Easiest Method: Unsupervised Classification

Install:

* Semi-Automatic Classification Plugin (SCP)

Go to:

```text
Plugins → Manage and Install Plugins
```

Search:

```text
Semi-Automatic Classification Plugin
```

Install it.

---

## Run Classification

Open SCP Dock.

Choose:

```text
K-Means Classification
```

Select:

* input image
* number of classes = 4 or 5

Run.

---

# Result

You’ll get classes like:

| Color | Land Type  |
| ----- | ---------- |
| Green | Vegetation |
| Gray  | Urban      |
| Blue  | Water      |
| Brown | Bare soil  |

![Image](https://images.openai.com/static-rsc-4/Ard0uMtMbBvbsPCWFaDBLvDSMCsl5aIPhTgXumlWnOJEc1ScyE8I4V3LiH0R-M0_35DBXqv24S8aaqZ0vinjByqQue0WsVs8OLzBTtDR4HHXgOhAAkKRq4KXxTwaOp2U8nqISX09mNMGzkSfnbQaxkqO6TK9fAc3SBcoa7EAnw-vkNJXTBV76ZzdUlQyrXiy?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/8RwDQOUBcJXWxTqHcWG7WsaH1xoISZtyeCDf0UfE9cd7FwjntlDoqU5e7xT4yP8iSNQVX6L5899dq454wqYVTW3XJgcHKjN183KtfIQ0Zr8hs6Mr0KFd0qXGNbGAnmtXX_YRquJvK0vPR2ztDKx3_U7_utdCbc8II0I0BvMGIwe0cIRigyZ9GgDXsq_pffG5?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/X25ovWJY03FgvgzLZgXM3z0lH4mr7KEUflt0M_2P5QLEIsk9Rl2ZnUfuCpTqu5k-mPBA0mg1IQDILvDNqwaTNb-REl9RVolujZIj88vr0X5esQ-RDrtqoRedQV4lVLwrB_Ghit7TBA_K36HAJw3QU7zk_Rp-H6rt3doUtXWqC5DZTAhgPCEyr4d1mruxXN8J?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/XwBhTyGPFGNx3ZnPmZHicNf82wEIuyZwq1pJZbrc3DnS4w3V8ffHNPBbbT4Yh8xQxaoTHbwlf4kcvWbZuEzScjy2CWsguS-98-jJE3u2nfT2ToyCW8BV-phzwwjTLZ7HFrqsc67fiqafoAp2q_eMldbWUK1cko867I6EjRHJSr-Ak79ninjRIOtjBpuC6X7V?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Tr0mhAhy2w4wSIko3nWzzXeQBKeYKll5EJhEhqOwQm0QKcjlpmI39atvQb6fvL_aQZaMXEKtwDw5YyC-y3ZxGwejaq29aQAbebjDQLEuQwrMR9OLZ9FaczGM38IXBEMcjQHjCygXlu7X9tIHbUjjDpncqVY8V_u7W8YT2IL4ba0UEEvMOpqkDTu-EPicMNv0?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ncCetSP0Duvdxta8zxTxLiJXz-86ar-IEVMZU8fWvMdWYccjlH_gojtDZAtfoNnVECvvsK9WIXNJpAKNLLdokcMezvgtZ4MDeeSfTyAoQrzo_Zq9f8XAunNNZMPbRX-jR99Ij-ahxQ7MsPVWC8XLEYDXCR0JJm8mBCTXJJaX_W6A-LVkuD21iShT1w-1-7wO?purpose=fullsize)

---

# STEP 11 — Create Final Layout

Go to:

```text
Project → New Print Layout
```

Add:

* Original FCC
* Enhanced image
* Filtered image
* Classified map

Also add:

* legend
* north arrow
* scale bar
* title

---

# SIMPLE FLOW DIAGRAM

```text
Download Landsat Data
        ↓
Extract .tar/.zip
        ↓
Load .TIF Bands into QGIS
        ↓
Create FCC (B5,B4,B3)
        ↓
Enhancement
(Contrast / Histogram)
        ↓
Spatial Filtering
(Low-pass / High-pass)
        ↓
Classification
(K-Means or Supervised)
        ↓
Final Map Layout
        ↓
Interpret Results
```

---

# Most Important Files

| File Type  | Use                 |
| ---------- | ------------------- |
| .TIF       | Actual raster bands |
| .txt (MTL) | Metadata            |
| .tar/.zip  | Download package    |

---

# What You Actually Submit

Usually:

1. Screenshots from QGIS
2. Final map layout
3. Brief interpretation report
4. Classified output image/map
