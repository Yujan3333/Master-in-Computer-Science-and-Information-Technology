#first-semester #advanced-operating-system

- **JPEG** stands for **Joint Photographic Experts Group**
    
- It is a **lossy compression standard** for **still images**
    
- Commonly used for photos, web images, and digital cameras


### 🧠 Main Idea:

JPEG **reduces image file size** by removing **visual data** the human eye is less sensitive to, especially color and fine detail.


## 🔧 Steps of JPEG (Very Simple)

### 1. Change Colors

- Convert **RGB** (red, green, blue) to **Y + color**:
    
	- Y = luminance (i.e., brightness) ~ black-white TV
    - I, Q = chrominance (similar to saturation and hue)
       

### 2. Shrink Color - Down Sample I, Q channels

- Reduce color detail:
    
    - Combine 2×2 pixels into 1 color pixel
        
- Brightness (Y) stays clear, color gets blurry — but we **don’t notice** it much

### 3. Cut into Blocks

- Break image into **8×8 squares** of pixels.


