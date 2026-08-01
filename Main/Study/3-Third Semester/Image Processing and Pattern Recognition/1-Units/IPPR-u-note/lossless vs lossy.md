
# 2. What is Image Compression? Differentiate between Lossy and Lossless Compression with examples.

---

# Image Compression

## Definition

**Image Compression** is the process of reducing the amount of data (number of bits) required to represent an image by removing redundant or unnecessary information while maintaining acceptable image quality.

Its main objectives are:

* Reduce storage space.
* Reduce transmission bandwidth.
* Reduce transmission time.
* Improve processing efficiency.

---

# Need for Image Compression

Digital images require a large amount of storage. For example, a high-resolution image may occupy several megabytes of memory. Image compression reduces this storage requirement and enables faster transmission over communication networks.

---

# Types of Image Compression

Image compression is classified into two types:

1. **Lossless Compression**
2. **Lossy Compression**

---

# 1. Lossless Compression

## Definition

**Lossless compression** compresses an image **without losing any information**. After decompression, the reconstructed image is **identical** to the original image.

No pixel information is discarded.

---

## Working Principle

It removes only **statistical redundancy** and stores repeated data more efficiently.

---

## Characteristics

* No loss of image quality.
* Exact reconstruction.
* Lower compression ratio.
* Suitable for images requiring high accuracy.

---

## Advantages

* Original image is perfectly recovered.
* No degradation in quality.
* Suitable for repeated editing.

---

## Disadvantages

* Lower compression ratio.
* Requires more storage than lossy compression.

---

## Applications

* Medical imaging
* Satellite images
* Legal documents
* Scientific images
* Text documents

---

## Examples

* Huffman Coding
* Run Length Encoding (RLE)
* LZW Compression
* PNG
* GIF

---

# 2. Lossy Compression

## Definition

**Lossy compression** removes less important image information to achieve a much higher compression ratio.

The reconstructed image is **not identical** to the original image.

---

## Working Principle

It removes visually insignificant information that is less noticeable to the human eye.

---

## Characteristics

* Some information is permanently lost.
* Higher compression ratio.
* Smaller file size.
* Slight reduction in image quality.

---

## Advantages

* Very high compression ratio.
* Saves significant storage space.
* Faster transmission.

---

## Disadvantages

* Original image cannot be recovered exactly.
* Image quality decreases after compression.

---

## Applications

* Digital photography
* Multimedia
* Video streaming
* Social media
* Web images

---

## Examples

* JPEG
* JPEG2000 (lossy mode)
* MPEG
* WebP (Lossy)

---

# Difference Between Lossy and Lossless Compression

| Lossless Compression                               | Lossy Compression                                    |
| -------------------------------------------------- | ---------------------------------------------------- |
| No information is lost.                            | Some information is permanently lost.                |
| Original image is recovered exactly.               | Reconstructed image is only an approximation.        |
| Lower compression ratio.                           | Higher compression ratio.                            |
| Better image quality.                              | Slight reduction in image quality.                   |
| Suitable for medical, legal and scientific images. | Suitable for photographs, multimedia and web images. |
| Can be edited repeatedly without quality loss.     | Repeated compression causes quality degradation.     |
| Examples: Huffman Coding, RLE, PNG, GIF.           | Examples: JPEG, MPEG, WebP.                          |

---

# Advantages of Image Compression

* Reduces storage requirements.
* Saves transmission bandwidth.
* Enables faster image transfer.
* Reduces communication cost.
* Improves processing efficiency.

---

# Disadvantages

* Lossy compression reduces image quality.
* Compression and decompression require additional computation.
* High compression may introduce visible artifacts.

---

# Exam Answer (5 Marks)

**Image Compression:**
Image compression is the process of reducing the number of bits required to store or transmit an image by removing redundant information while maintaining acceptable image quality. It reduces storage space, transmission time, and bandwidth requirements.

Image compression is of two types:

### Lossless Compression

* No information is lost.
* Original image is reconstructed exactly.
* Lower compression ratio.
* Used for medical and scientific images.
* **Examples:** Huffman Coding, RLE, PNG, GIF.

### Lossy Compression

* Some information is permanently lost.
* Original image cannot be reconstructed exactly.
* Higher compression ratio.
* Used for photographs and multimedia.
* **Examples:** JPEG, MPEG, WebP.


| **Lossless Compression**                                               | **Lossy Compression**                                           |
| ---------------------------------------------------------------------- | --------------------------------------------------------------- |
| No information is lost during compression.                             | Some information is permanently lost during compression.        |
| Original image is recovered exactly after decompression.               | Reconstructed image is only an approximation of the original.   |
| Compression is reversible.                                             | Compression is irreversible.                                    |
| Lower compression ratio.                                               | Higher compression ratio.                                       |
| Produces larger compressed files.                                      | Produces much smaller compressed files.                         |
| Image quality remains unchanged.                                       | Image quality decreases due to information loss.                |
| Suitable for images requiring high accuracy.                           | Suitable for images where slight quality loss is acceptable.    |
| Used in medical imaging, scientific images, legal documents, and text. | Used in digital photography, multimedia, web images, and video. |
| Repeated compression/decompression does not degrade quality.           | Repeated compression causes cumulative quality degradation.     |
| Examples: Huffman Coding, Run-Length Encoding (RLE), LZW, PNG, GIF.    | Examples: JPEG, JPEG2000 (lossy mode), MPEG, WebP (lossy).      |



> **Exam Tip:** If asked to "differentiate," write the definition first, then draw the comparison table. This usually earns full marks.
