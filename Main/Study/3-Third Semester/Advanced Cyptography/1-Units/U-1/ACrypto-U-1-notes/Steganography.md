#advanced-cryptography 

---

# Definition

**Steganography** is the technique of **hiding a secret message inside another ordinary file** (such as an image, audio, video, or text) so that **no one knows the message even exists**.

### Simple Definition (2 Marks)

> **Steganography is the art of hiding secret information inside another medium (image, audio, video, or text) so that the existence of the message is concealed.**

---

# Easy Example

Imagine you want to secretly send the message:

```text
Meet me at 5 PM
```

Instead of sending it directly, you hide it inside a photo.

Normal photo:

📷 Beach.jpg

Hidden inside:

```text
Meet me at 5 PM
```

To everyone else, it looks like an ordinary beach photo.

Only someone with the correct extraction method can retrieve the hidden message.

This is **Steganography**.

---

# Real-Life Analogy ⭐⭐⭐⭐⭐

Imagine writing a secret note inside a birthday card.

Outside:

```text
Happy Birthday!
```

Inside (hidden):

```text
The meeting is tomorrow at 9 AM.
```

Most people only notice the birthday message.

The hidden note represents **steganography**.

---

# How Steganography Works

```text
Secret Message
       +
Cover Object (Image, Audio, Video, Text)
               ↓
        Steganography Algorithm
               ↓
         Stego Object
               ↓
Receiver extracts the hidden message
```

---

# Basic Components ⭐⭐⭐⭐

## 1. Secret Message

The information you want to hide.

Example

```text
Password = ABC123
```

---

## 2. Cover Object

The file used to hide the message.

Examples

* Image
* Audio
* Video
* Text

---

## 3. Stego Object

The final file after hiding the message.

Example

```md
Original image

↓

Message hidden

↓

Stego image
```

---

## 4. Stego Key (Optional)

Some systems use a secret key.

Only someone with the key can recover the message.

---

# Types of Steganography ⭐⭐⭐⭐⭐

## 1. Image Steganography

Most common.

Message is hidden inside an image.

Example

```text
photo.png
```

Hidden data

```text
Secret Password
```

---

## 2. Audio Steganography

Secret message hidden inside sound.

Example

```text
song.mp3
```

contains hidden data.

---

## 3. Video Steganography

Message hidden inside video frames.

Example

```text
movie.mp4
```

---

## 4. Text Steganography

Message hidden inside text.

Example

Using extra spaces.

```text
HELLO␠WORLD
```

The spaces may represent hidden bits.

---

# Image Steganography (LSB Method) ⭐⭐⭐⭐⭐

The most popular method is **Least Significant Bit (LSB)**.

Each pixel has color values.

Example

Pixel value

```text
10110110
```

Suppose we want to hide bit

```text
1
```

Replace only the last bit.

Before

```text
10110110
```

After

```text
10110111
```

Only the last bit changes.

The image looks almost the same to the human eye.

---

# Why LSB Works

Changing only the last bit causes a very tiny color change.

Humans cannot usually notice the difference.

---

# Advantages of Steganography ⭐⭐⭐⭐

* Hides the existence of secret data.
* Provides confidential communication.
* Difficult to detect visually.
* Can hide large amounts of information (depending on the cover file).

---

# Disadvantages ⭐⭐⭐⭐

* If discovered, the hidden message may be extracted.
* Compression or editing may destroy hidden data.
* Provides little protection if no encryption is used.

---

# Applications ⭐⭐⭐⭐

* Military communication
* Digital watermarking
* Copyright protection
* Secure communication
* Intelligence agencies
* Medical record protection

---

# Steganography vs Cryptography ⭐⭐⭐⭐⭐

| Steganography                            | Cryptography                         |
| ---------------------------------------- | ------------------------------------ |
| Hides the existence of the message       | Hides the meaning of the message     |
| Message is concealed inside another file | Message is converted into ciphertext |
| Looks like a normal file                 | Encrypted data looks random          |
| Main goal: secrecy of existence          | Main goal: secrecy of content        |

---

## Easy Memory Trick

### Cryptography

Hide the **message**.

```
HELLO

↓

XJQPW
```

Everyone knows a secret message exists, but they cannot read it.

---

### Steganography

Hide the **entire message**.

```
HELLO

↓

Inside a Photo
```

Nobody even knows there is a secret message.

---

# Cryptography + Steganography ⭐⭐⭐⭐

They can be used together.

Example

Step 1

Encrypt

```text
HELLO
```

↓

```text
XJQPW
```

Step 2

Hide

```text
XJQPW
```

inside an image.

Now even if someone finds the image, they first have to discover that a message exists and then decrypt it.

---

# Exam Definitions ⭐⭐⭐⭐⭐

### Steganography

> Steganography is the technique of hiding secret information inside another medium so that the existence of the message is concealed.

### Cover Object

> The original file used to hide the secret message.

### Stego Object

> The output file containing the hidden secret message.

### LSB (Least Significant Bit)

> A method of hiding information by changing the least significant bit of image pixels.

---

# Frequently Asked Exam Questions ⭐⭐⭐⭐⭐

### 2 Marks

1. Define steganography.
2. What is a cover object?
3. What is a stego object?
4. What is the LSB method?

---

### 5 Marks

1. Explain steganography with a neat diagram.
2. Explain different types of steganography.
3. Differentiate steganography and cryptography.
4. Explain the LSB image steganography technique with an example.

---

# One-Minute Revision ⭐⭐⭐⭐⭐

```text
Steganography
= Hiding a secret message inside another file.

Components:
• Secret Message
• Cover Object
• Stego Object
• Stego Key (optional)

Types:
• Image
• Audio
• Video
• Text

Most Popular Method:
• LSB (Least Significant Bit)

Difference:
Cryptography → Hide the meaning.
Steganography → Hide the existence.
```

### Super Easy Memory

* **Cryptography** = Put your letter in a locked box 🔒 (everyone sees the box but can't read the letter).
* **Steganography** = Hide your letter inside a photo frame 🖼️ (people don't even know a letter is there).
