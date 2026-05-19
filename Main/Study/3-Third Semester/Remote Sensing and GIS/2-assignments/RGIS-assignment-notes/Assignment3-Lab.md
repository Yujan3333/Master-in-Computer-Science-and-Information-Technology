#lab #assignment #RGIS #third-semester 

- [Understanding the flow of the lab](Understanding%20the%20flow%20of%20the%20lab.md)
# Remote Sensing & Image Classification Using QGIS (Landsat 8/9)

## Study Area

For this assignment, you can use **Kathmandu Valley, Nepal** as the study area because it contains urban areas, vegetation, water bodies, and barren land, making classification easier.

---

# i. Download a 30 m Resolution Landsat Image

Use Landsat 8 or Landsat 9 imagery from:

* [USGS EarthExplorer](https://earthexplorer.usgs.gov?utm_source=chatgpt.com)
* [USGS Landsat Collection](https://www.usgs.gov/landsat-missions?utm_source=chatgpt.com)

### Steps

1. Open EarthExplorer.
2. Create/login to your USGS account.
3. Search for **Kathmandu, Nepal**.
4. Under **Data Sets**:

   * Select:

     * Landsat Collection 2
     * Landsat 8-9 OLI/TIRS
     * Level-1
5. Choose a cloud-free image (<10% cloud cover preferred).
6. Download the **GeoTIFF** product.

### Recommended Bands

For False Color Composite:

* Band 5 → Near Infrared (NIR)
* Band 4 → Red
* Band 3 → Green

---

# ii. Load Bands in QGIS and Create FCC

## Steps in QGIS

1. Open QGIS.
2. Go to:

   * **Layer → Add Layer → Add Raster Layer**



1. Load Bands:

   * B5
   * B4
   * B3

## Create FCC

1. Right-click raster → **Properties**
2. Select **Symbology**
3. Choose:

   * Render type = *Multiband color*

![](../../../../../../Images/Third_Sem_Images/Assignment3-Lab-3.png)



1. Assign:

   * Red = Band 5
   * Green = Band 4
   * Blue = Band 3

### Interpretation

* Vegetation → Bright Red
* Urban Areas → Cyan/Gray
* Water → Dark Blue/Black

![Image](https://images.openai.com/static-rsc-4/DCOmaNuIFtXK_yt3Ciy1Oc3EBo8ESTB2IGEMNqCf2S0ZbK3VWOmTN7UmG2Ad0l-Op_rDMVHjVhJSXnv8FE26-Xp_rPA3bhF4FLX7P5Wny94GL9ErZV6Rr0qBpZ5pqs7wBxwymMY0D6iLHxiXWOofEdSoug1n025idyU16K9zDRhMMlvDyLjYLvtsSkKg9FMF?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/U8pvrmlf4GsksDbhPLdVI0hIwh-Jeteb2sLGmIeF0hfxHxg2r8QKpcDzjvh5-3SVxF4fNjUMFLJJUjN8mdi7WXkupuyQJtdpBukfiLavue3k96t4X1Fk4A3kU2Cu_8qELqOp8oV5r9IUbsW7V0had_G88NjAxvN1ZZFzkIsk7LSio90v3QDXKXZNoElTNueJ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/OxyCAuHXFrOLF97L1o9aCXLqvRx7QkKQdLITXu1s0BY55BnVMVGvHWLbaR6g6XzbvA8elEQFMi4PXR1XCJQD3DNGyWqvYquk-hYCaoWpKQAMNzy5mmrVOh7qqpIF7RUQqw_vmRfnHoLU_sla7tpxflw5tt98d3mZNjltbPatzLYJI2XNMK88kTv52u2ugIva?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/6nUUmE70l__UJ3Tr80ytmUcjwcguvU7lcTXzfcQPVlNwTE2EAOfcQQvNbYDKMCFyEhFjd5yl6JYqUFDj4nNGZS3kkxpvjvfeKrit5EA5lKYbLesAZq1AlZxVmUS03qqmRgFYlKqWDeTJ9HHHuMIeAF1pxuoLZzslWFIVRrWGUWckZFfAP2BGI3kMpUCIoUYe?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/8oMF8TJDaqSPzTZrci4PTWWlXzASkLMnceKU-aNPAR4nneRTaLPRq2K3WjxOGPZJ9PaqAAInznea503jmhByqEo4A5LTfP7HjwvQIpUPbPbt7I7k8zuoE-jeBjFrBvY_Ta2PflckRxQJFtSkdKPMnKW5w2rgcVNzHb8E5YCmiEh-k2KyYxMw8EehZXlisTIf?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/H2LXGkcv8JTKbVycrJ_fnmzquwXuxfIZywLAM_27gdfi5yO7ixT5VlwEDzYmvpSsI1xDAEWWk7ghKDZDfGL6s2R0ceL1aUUaDE1tS5bCxKvEJldafnbmc7gG2JH08Oa5vcCRDt-fG7DLoaodbs-bymolis4VjNwMHYHvaC60-b7yfnPFhV5RpZTbTNpZMMkD?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/YsidAgsW3HZudkzI9T4dDnpOuEMzio_9Kna0zy3dACvi1ZU1LjScmPVNVhBcuwoy7uhCwdMpsRjTt62Rdj0CTfh3nCmNo0HHPOq9Tr3u3Ga_DsD7a1PSM7gwA9k8ydFNAslTlHlo7EI7RSqy-tTsWs1yoD4p8mpUQaN-UtlH2ghd8FK2hFRlCBPl-CaOthAY?purpose=fullsize)

---

# iii. Apply Image Enhancement Techniques

## 1. Contrast Stretching

### Steps

1. Raster Properties → Symbology
2. Min/Max Value Settings
3. Select:

   * Stretch to MinMax
   * Cumulative Count Cut (2%)

### Result

* Improves brightness and contrast
* Makes land cover features more visible

---

## 2. Histogram Equalization

### Steps

1. Open:

   * Raster → Miscellaneous → Build Virtual Raster
   * Or use Raster Calculator plugins/tools
2. Use histogram equalization from processing toolbox.

### Result

* Enhances tonal variation
* Improves visibility of subtle details

### Comparison

| Technique              | Effect                   |
| ---------------------- | ------------------------ |
| Contrast Stretching    | Improves global contrast |
| Histogram Equalization | Enhances local detail    |

![Image](https://images.openai.com/static-rsc-4/Cn-0yeofN83ptHq90pY-Vh3S3SnX0PksXfWTflHOSEZvkiRryDRHIEw85WtmozwdLFacIrTDP1kOv8jC27jQ9z6nX10gQw-Xj2CtSltuFvSTdxQexGrJoDFKHmn5ylLOhXSBzXNtwaGvLS8BB6Md5MMymi1A87X6B6LIe3Vm1V1WPQKkhQRj7hPAdxKmVg8I?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/KjVJ6iXCDHlQZubFPsoNnjwjKLVEZsVPjjkjRJStSYyTcdemLHOgG6Obp6N9vXUYGionZllZ260C4N6RZZnLtyYCRy47XzadcnFMbfe_DQ1xYgRWjOZdfRe_8Dv-f5JjoqafCeOZs1ZYm30D1fuBkI-JIEZWQdTDBLJnghnMxOnFkQUovrMsxDLwno9JTa83?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/BfWbymWFBu-FxpL0X1G5s7VTmz5GN2YmkEiV3FNhRm0ZK7FcAJufcSbUYydOHuqdVz74MxsR-AQt2sTUbgamdrISHj1JsRz-lcTWQFhfsPR31JrldvSK_Q_JHGPCMObQJVoQMMNNWu9vXSlzWSt9RY3YeBH2nKwCNkfVjzwC80r1KKLG6FNMLxIKANI3Oeed?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/rDQUNQd5GH5JBTryzUUe7nyu8rMYO_WCoe18KonhCtJVzTASlln7ylC1XOzlPIr9vIHwsZW1Q6izGagTDwZQooeiNX0ewclBVZKepKw8ku5-9ppwxH95tMxsHJ3QMcEQ7rreyZ1_XunKEIhYSSwIgxbENyC2i_EONULCKJ0fNNeF1dKlILkzvH4RPqe9Gt7d?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/mHNPQn_FT_TClVBK1YS3HmlOJaK4T9XAHI4n7H9rgavEllLOSq-J1uS-VWEznN0H74QV6CGDU7UYwDxSkTfJFwFKj2sle0lsdKuNF-KDrjNm_jphC5hW-LCtyxj7NDCbv6cqW1jNB1OQiCT9tHZeoOh7BRnlx_zGGryFz67adAcX6IpG9C7VmSiJKSNRdYee?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/FklvbkklcxZArYqpA2UZMmuwwdC8XRyJoRBSxQD25dM1SeXMwayvuDVvDUX9akKyp4rBl0-Jj0xnw2gT9fA9ZPoFPOdMlSP99fuHwBTx86KXR6-H2-dYlr31C2vPUIdkEYT1bOSdtMdOEVL9jnTBYT-IGzXDKOvSp5xiKPyNoCjEkNGaSUeX-_DskSZN3tex?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/QcFOW1EjDwgDVPKO1x8siErR1da2YsDhdClUbFkr0-LyzBgkAKOxShtegyxbUG3f_YiBCdxwyULVlHzll9F8l2eW5mT6z99jwfluNAI5KI_9PoVC4xRIvRw8YIaEZU_VRyiCLk8QicIU_iA3ASrktyo04gzIXjDDMx_O4zZ8r2QrdM5X1ivOlzwZvE7qoVDY?purpose=fullsize)

---

# iv. Apply Spatial Filters

## A. Low-Pass Filter (Smoothing)

### Purpose

* Removes noise
* Smoothens image

### Steps

Use:

* Processing Toolbox → SAGA/GRASS → Convolution Filter

Kernel Example:
$$[
\frac{1}{9}
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
]$$

### Result

* Blurred image
* Reduced high-frequency information

---

## B. High-Pass Filter (Edge Detection)

### Purpose

* Enhances edges and boundaries

Kernel Example:
$$[
\begin{bmatrix}
-1&-1&-1\\
-1&8&-1\\
-1&-1&-1
\end{bmatrix}
]$$

### Result

* Roads/buildings become sharper
* Boundaries highlighted

![Image](https://images.openai.com/static-rsc-4/c5dVIBY5ECcRSEXTjtjGa7pIgece5MNeL9URSYaLfhVazh7KKrVLzwV6Avo0ubAhtaD5RIDdUGm6R-qRiS3rqRei-nyhkwhpX8GGty7YbQCD5OqVO0vH4gbY5IZiMMTjdDP7MJTFTgrKiKgp7dhfmOb9x4HiVmwVNTRQ2UF80MeT5RNcwAXqfnLvhCej6J41?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/CmdiMyuPQBq2lv046Fzml9A1FRCP79h5eStRExB-7WgkwIhnFHY6-i-JvFzMJ3qQjUOrusv3EbOdBtbqq6yeHZXgC4aEBv2mX7Q02_yWJ5BnvWXgkQDk7R6-9vWHbbFbjM-3-JlVH-Ds1izufjH85XgPrBcm3SL0iKzXZ32TSyuYADZCWgvSHFHp051S-QPF?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/xyrhJl3baLlgUl53iSNx1S_WhBds1Nl3J-yxnVPVQIyOG-8RoNfXQe5bZcvxgr73j-9Xux_MlP__LixmvDrDuJuJUDpewqDxyN-_dEP1yvoxeBb_hQFWyU8yIbXl3_1zX7rVrnvpuSeHDuR550rOjJUeLsdTl3eZUxfPeJteKeskvAZaycsvu79LTJbDkUwG?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/WjkY6qryVsibTyV5wT3XjR1PXL3xJ0J2h8EfFbjgdZZ83ugRnOWyk02YK6JJIFGj_m0dVmBKFbSFWWRwNMoMoI7jaSfKbcUaNxNfny_7WRNFz91hMQUSYLp72WPbsAKuykwSF7Y0XDpiD-0r9d6gPFmR78vgH4mfKSOCJXX0fJfDN0qJL_x0GnDkE7CNtCLQ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/hKeg-dQUqZ3UlJk8YqJ2cjaxgIPPj837TykGlC-jhvj1-P6TYdSiqNZcOrpJaYPNeomwPNozSq7jrWT2aJnSrID19-jliknvoECJtv84emEFOwrak_Lykif5P89EiTU90CKM0RJglyaqK-dYTlFB8LZXdpLK4FztnofbWqeVXW2YUeU3Yji8j30QjSQv1GU7?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/kihq4VAJ6qt0Ocvk0WY57UYJoGtGN_WrFhNhjYVpP0YYto1zWOvlgOHzbQBAC3RrGkUBZS_HJQ3nayUab1rPaKHZeq1jLrdMNWQ3E6SUpySqOoDtjWREahmY2VREp3NM7l-JmsMUDmWi_Lv3PUQirm6s6lvEffbcSjn2AWcStyFleQ6pffIYjrHlx-xGGkuS?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/798yTWdyVU2YvWo-2CSsttuWKrMYI7bwu_5WvmL_CDyZrwox2YdwH2F4TxcmKIzZ-MhFIXQHsSQNFLyJ4yUHvVqehMaFyfdyGp_y_0wS1JnQuR4CJHFMw3fOsC-t_c-qNUq9Jc1V1dLiD9KgwOO2gxNMVD27OFkbdF18MpTgTIXM6FRybNfW08h2ZghmcSVq?purpose=fullsize)

---

# v. Perform Land Use/Land Cover Classification

## Recommended Method

Use **Unsupervised Classification (K-Means)** if you are beginner-friendly.

### Steps

1. Install:

   * Semi-Automatic Classification Plugin (SCP)
2. Open SCP Dock.
3. Select:

   * K-Means Classification
4. Choose:

   * Number of classes = 4 or 5

## Suggested Classes

* Urban/Built-up
* Vegetation
* Water
* Bare Soil

---

## Alternative: Supervised Classification

If required:

1. Create training samples (ROI).
2. Use:

   * Maximum Likelihood Classification

---

# vi. Create Final Map Layout

In QGIS:

1. Go to:

   * **Project → New Print Layout**
2. Add:

   * Original FCC image
   * Enhanced image
   * Filtered image
   * Classified map

## Include:

* Title
* North Arrow
* Scale Bar
* Legend
* Coordinate Grid

### Suggested Layout

| Map            | Description          |
| -------------- | -------------------- |
| Original Image | FCC Landsat          |
| Enhanced Image | Contrast/Histogram   |
| Filtered Image | Low-pass & High-pass |
| Classified Map | Land Cover Classes   |

![Image](https://images.openai.com/static-rsc-4/FkOYKd2Xe3GKJpZkQ81hOpc87cFoFwwyhdGaCbWxNKKmIQXbNjvvYPJ4hZjn32ysVkGrMX3mipsdDKX2TJPj4avjOKm_f3XHF8ZbisRRY3Viug9fv7gIUmMOxqFxtMrAyY3V04CFWtlnP5WhAzzQVyfCMb2vuHY7k70CUkC24N8WqHD53_VPD_DT4EeKGSO8?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Tucx5Ydrzn3w2eQEwgVpe8bJwCaz8nm1FWYd_55DEpai_pqwh1sd2bu43SvbwLDA23_NgE0Om4oft3Ch0O-FInHGGeqN16rlkK302MJjbH1Vx1jDvaL0L6u686DTzYoFo5-EBALje189cDiOJ3eCSQ_6_WJcBA_exV9g-pJ0yqT0tzY2Dabd9YOIixlQOg-M?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/XUsDkf6_2xLRa4PfpHoOOkcueSr2SZPOPmFpBHNLZ3xpM1Au83xRwMQ22UPMUnC1cd1BBoktNM5nc_kn6bbQA3EgPrFM4PFGeeIjXuQYTfmKxrnjR1dej7Ow1GYkvdpJnSBYuVsIO6NjGA8bdg8vy5pLT9fbmyxNAgXIh8DMkaGPo1Mlg2X2x4yu4wveCQa1?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/SnGfNHePKCb7oNK1vLs68Ig_ZQ_plR1otxfNmtpQkNRkDldaHQKMvJeZDNGYW9D5DvMIsWsUpBlFHJKmhue5i1ZXwxPdB5KolJDUq6ifq7WQWKixJAFlE0Njn-QPFv4WeLxjZ0xtGioe9Q3f8dzEvGKTkb0-mQqOTrkoBuayf4xuDdnZtQeGIYmRVIphJG1-?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/2rSw4FtUlULboOItK-FPmiBcjF3_jnjZI_trtqHYt2waX9Ohd9sq6ZkIyySGnWaY70mrCPIHfO7plWO7kW4s4_giPrx_W7d6Kc2mCbS4vtyrcmgffUKn1DUU3_d4KejB0ZsfjjLRHCqwWMCMZ-zubz2RGXYrqBBkCY8GiG19KQlr2Bu_Sd8TYWlqzaLFm7OG?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/k0accJo1Nlsd-01W7WFkJqhRR4ySxP6dF9nl2NgMeOvsqit7uT1b2ucl2YMKeBXKA4HsdGskN3wXGkRvJ-Q8tyOW_hybvGXVeWK1HGXhn_MxAwI9fWuNufRvxoAWD1Yxq-WI09WM8CBcl6T58oTOsTHFR0EL9qUiq91XefMj04zYRnyTKQEQKhce3IF6wavS?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/LJxYLQO6vFoSO98fmOSRhLj4UvvV2FbGWka62-NWwUeZZcJtrDt42vuuYxk_7OJGqLvn1EANKfkKzaq0fSt-R8tf_z5oopHfvQejQztbJWx44wJ9uCCvehPK9nlaTwroY2sJ--z_kxIPLrGmt_uRCvMJOqNoe8zHwWIFcg-Sa-HJtaS5_EuwQ8hUcjqccZan?purpose=fullsize)

---

# vii. Interpretation and Discussion

## Interpretation of Results

### FCC Image

* Vegetation appeared bright red due to high NIR reflectance.
* Urban areas appeared cyan/gray.
* Water bodies appeared dark.

### Enhancement Effects

* Contrast stretching improved overall visibility.
* Histogram equalization enhanced subtle terrain and land cover variations.

### Filtering Effects

| Filter           | Impact                               |
| ---------------- | ------------------------------------ |
| Low-pass filter  | Reduced noise but blurred boundaries |
| High-pass filter | Enhanced edges and object boundaries |

### Classification Accuracy

* High-pass filtering improved edge definition and helped distinguish urban boundaries.
* Excessive smoothing reduced classification precision because neighboring pixels became spectrally similar.

---

# Conclusion

This exercise demonstrated the use of QGIS for satellite image processing using Landsat 8/9 data. Image enhancement improved visual interpretation, spatial filtering highlighted different spatial frequencies, and classification successfully identified major land cover classes in Kathmandu Valley. The study shows how preprocessing techniques significantly influence classification quality and spatial detail extraction.
