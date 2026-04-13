- [Point in polygon and line in polygon in figure](RGIS-assignment-notes/Point%20in%20polygon%20and%20line%20in%20polygon%20in%20figure.md)
## 1. Point-in-Polygon Overlay

![Image](https://images.openai.com/static-rsc-4/PETVxEEegvgHfcbKnu1-hpJLuTgpEsT7AcaUadojtafrMgfBMf6gsub0xVeUN-JP7Jc_zsWIEveB5TWJzf2lMnJXESR_9ao3CTqaKqHJCcaTD_QN_pDaQ_d6shM_h8DYgcdgTavE_nsxuK2hmoE8CSZfhVE_3V96sx58YtUU1tFfkLvSVFPWCbz7ccY0LWHF?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/JDBWr2SdVlO5t9W994SykT7VciQQi4xdybUGTFxI1XiN32WKMlYv2ChKS7HS_bpV7GkWBaq9mG6Xt35Z5GWT7-0Xuw3JOJAf4jpjuIB4jrTyfBEHKK-SmVJ94Rfob8oZ9InKliWJtsaPw33NJ_fE2FEzkjG3zofQDYx8erfJwwC6NCvu8wPbwM60sQIumozZ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/O8sAda1WYFHpQREpuRdAna7ZJLCj2eesuJLBqfM_zcBKgaYgd3zsXfOsARB9knxvxi2LwDlr0rHvRty6_hkYRs9U0RyHvYTKuVqRn3UMCH2ATKZp5TVGKJlG4FewFla9oDulxpafUG-uAiqzO9Sn2ge7L6ENjRGrWo2wF3479-BeQrbzRfR95c1s-81bQ2vS?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/_UGMTn3if0tZ_UDUrcLgQ9otDDUoQyeJEmphGT57RS-_PlsWUpIQ1y5wxMlWxcOQ4q5qfiKTgoyvxd5RbJO4fkka0sE-EZtx5CtCmZR2LBrNudRmsOlvQedcPnAeWXPomtWxkuV2mR8n9gX2KhQX_ao1yZgJN0ksSiOHV5TaZV2q_rOJc5h_MlEAXQ1nRG3u?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/6cMoXQ4JLO8brAiP7gAxYsW9wiTpqKdT7DxokQQF0QBwiyneNa1JjcvxN1M9CyJHOfhjuU2JlTze_OIj6Pm13dIRMiOwca8_fbgGwjVCDfeD3kXeX2vBmkViCMP5a44pd-on2V8qiw4z6KDjNglV1zxVPIGF0ZJeD6VNquA3pH_epBsUsVwoPMSI9pxmho8e?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ZBmPQrWrHpQiFBZkz-TWRdDMZ6G70F9BA1xqKdsrWH8hiYXIabwdI_SX9e3M6P9crZGHUHax2uyYLo0dbc6b-Yr3TXeypP_yQwl5JzBD_byJYcBsBIxxbmhjkT0a5bAtvrcg46h-ChCyWPlLgoBhCvS4xbVQQvnt0uPtTQn76V76W7FZVoZYqneSPj6gB35l?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/4B_pyZ70BSMHRFH_gMG1sSiGhvwWy0GdkB1tL4qqfbwJ5b0dkTuTk6k0lfip3N_a7J3jRTfeRD_r5_VboJjsiZ8ZNzbOO9QcyOejzsu0zhFV5uFYyhMLPFpuv-XUGd5DqIhpAzghUMG3J-3IeTcTobv7anj85zgf7jaCKJHIieOdqXn74Oc65nXVKOhM6huI?purpose=fullsize)

### Concept

**Point-in-polygon (PIP)** determines which polygon each point falls inside. It is one of the most common GIS overlay operations and is often implemented as a **spatial join**.

### How it works

* Input layers:

  * Points (e.g., schools, wells, accidents)
  * Polygons (e.g., districts, land-use zones)
* For each point → check if it lies **inside a polygon boundary**
* Assign polygon attributes to that point

### Example Attribute Tables

**Input Point Layer**

| Point_ID | Name     |
| -------- | -------- |
| P1       | School A |
| P2       | School B |

**Input Polygon Layer**

| Poly_ID | District | Population |
| ------- | -------- | ---------- |
| D1      | North    | 50,000     |
| D2      | South    | 70,000     |

**Output (After Overlay)**

| Point_ID | Name     | District | Population |
| -------- | -------- | -------- | ---------- |
| P1       | School A | North    | 50,000     |
| P2       | School B | South    | 70,000     |

### Key Use Cases

* Assigning **administrative areas** to locations
* Finding **which zone a facility belongs to**
* Environmental monitoring (e.g., which watershed a sensor lies in)

---

## 2. Line-in-Polygon Overlay

![Image](https://images.openai.com/static-rsc-4/JDBWr2SdVlO5t9W994SykT7VciQQi4xdybUGTFxI1XiN32WKMlYv2ChKS7HS_bpV7GkWBaq9mG6Xt35Z5GWT7-0Xuw3JOJAf4jpjuIB4jrTyfBEHKK-SmVJ94Rfob8oZ9InKliWJtsaPw33NJ_fE2FEzkjG3zofQDYx8erfJwwC6NCvu8wPbwM60sQIumozZ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/PETVxEEegvgHfcbKnu1-hpJLuTgpEsT7AcaUadojtafrMgfBMf6gsub0xVeUN-JP7Jc_zsWIEveB5TWJzf2lMnJXESR_9ao3CTqaKqHJCcaTD_QN_pDaQ_d6shM_h8DYgcdgTavE_nsxuK2hmoE8CSZfhVE_3V96sx58YtUU1tFfkLvSVFPWCbz7ccY0LWHF?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/IkxT5OqnUcsDiyLlEiSDrTsTqD0KxKUDdAIHy4PMTi0LJqcVA3bV5eb4AYuWEjNwReCmTVLQySo2emcqrM9Zm97dd_pCa5X9RXf17Jd0zA9KAtaqmkYwf8LxlqKFNZ5pj8ToawQJ29NWaCvfdWXI-j33udmsEwwFBYG50W0xZiadOU9EtXGl-t0afMq_oYwQ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/rgZge8TEYX76XlNOSXZbwrQbPr8Yqaccjfy2m09TLFTcHYEXoZcORrrnokpOHBDGlCrTUp35112WWIyOARtSWcDgkEejzhrAbmY0Sez1DBuDV3mj8NSKec0yTdiCtWe6w2JP0oF79ewktuCJRKpk7gvVN4bI-rl-JTMK3QZMoyeYY8rt87YX4AcaayGqjSl-?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/FLsvYLxMFKR7UHhf-TMjih0Ir1QUN2tEg2Zp0vL7I9jeBmKx441Opgw4PDvXEXxkR24NY4ecUfrKEO8TyiNQzlC42KSFtsL3Xeo-S0sD-huCqTFGlgGQC_vxVFWOZtu4whVmPUIRuqUI_7ifNDkaKhVAV4P_U2zrxwQGk05emufT2CCB9V9xkUwJz2WfUVYC?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/AEjiVf3g7rsx1gU1OWBY0p1OHrxtNSQve3wZyMnfMq0jcR0gxujNBy7Rjqn9I7Gm6XPXkFbaHSxyKhrMtziy8h_I6f4jLTLTvBR-9YeZEiRrfrpDVsi2AZQ9UNGBAk4dJ9fUsAEYht7hiMKUO5-lgAIskPQtyafJHUVm_gDVuHZ0mtGJIPqP2ldIW9kPhGfl?purpose=fullsize)

### Concept

**Line-in-polygon overlay** splits lines wherever they cross polygon boundaries and assigns polygon attributes to each resulting segment.

### How it works

* Input layers:

  * Lines (e.g., roads, rivers, pipelines)
  * Polygons (e.g., counties, land-use zones)
* Each line is **cut at polygon boundaries**
* Each segment inherits attributes from the polygon it lies within

### Example Attribute Tables

**Input Line Layer**

| Line_ID | Road_Name |
| ------- | --------- |
| L1      | Highway 1 |

**Input Polygon Layer**

| Poly_ID | District |
| ------- | -------- |
| D1      | North    |
| D2      | South    |

**Output (After Overlay)**

| Segment_ID | Line_ID | Road_Name | District |
| ---------- | ------- | --------- | -------- |
| S1         | L1      | Highway 1 | North    |
| S2         | L1      | Highway 1 | South    |

---

## 3. Why Line-in-Polygon Produces More Features

👉 This is a key concept:

* A **single line** may pass through **multiple polygons**
* Each crossing → creates a **new segment**
* So:
  **1 input line → many output segments**

### Example

* One road crosses 5 districts → becomes **5 separate features**
* Each segment has **different polygon attributes**

### Reason Summary

* Overlay performs **geometric splitting**
* Each split = new feature
* Therefore:

> Output feature count ≥ Input line count (usually much higher)

---

## 4. Real-World GIS Applications

### Point-in-Polygon Applications

* **Urban Planning**: Assigning buildings to zoning districts
* **Public Health**: Mapping disease cases to administrative regions
* **Retail Analysis**: Identifying which store falls in which market area

### Line-in-Polygon Applications

* **Transportation Planning**:

  * Roads segmented by districts or traffic zones
* **Utility Management**:

  * Pipelines divided by land ownership or regulatory zones
* **Environmental Studies**:

  * Rivers segmented by ecological regions
* **Taxation & Maintenance**:

  * Road segments assigned to different jurisdictions for funding

---

## Quick Comparison

| Feature Type     | Operation Result              |
| ---------------- | ----------------------------- |
| Point-in-Polygon | Points get polygon attributes |
| Line-in-Polygon  | Lines are split into segments |
| Output Size      | Same (points)                 |
| Output Size      | Larger (lines → segments)     |

---

