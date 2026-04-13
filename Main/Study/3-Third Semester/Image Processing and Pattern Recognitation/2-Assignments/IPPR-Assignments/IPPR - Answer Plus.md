I did it as a beginner-friendly Python lab solution based on your PDF instructions. The PDF covers 5 labs: image fundamentals, histograms, spatial filtering, FFT filtering, and kernel/frequency analysis. 

Files:
[Python lab solution script]()
[Generated output images zip]()

How to approach this lab

1. First understand the pattern.
   Every lab follows the same idea:

* load an image
* apply one image-processing method
* display the result
* compare before vs after
* write 1–2 lines explaining what changed

2. Do not try to memorize the math first.
   Start by understanding:

* what image goes in
* what operation is applied
* what output comes out
* why the output looks different

3. For your report, always answer these four things:

* What did I apply?
* Which parameters did I use?
* What changed visually?
* Why did it happen?

What is happening in the code

The script is split by lab, so you can read it section by section.

Lab 1

* Loads a sample color image
* Prints image stats like shape, dtype, min, max, mean
* Downsamples the image by skipping pixels
* Quantizes grayscale into 4, 8, and 16 levels
* Splits RGB channels and computes correlation between them
* Applies rotate, scale, and translation transforms

What to understand:

* shape tells image size and channels
* downsampling reduces resolution
* quantization reduces the number of gray values
* RGB channels show how color is stored
* transforms change image geometry, not pixel meaning

Lab 2

* Makes a low-contrast image
* Applies contrast stretching
* Applies gamma correction
* Does global histogram equalization
* Does adaptive equalization (CLAHE)
* Matches one image histogram to another
* Enhances color image in two ways:

  * CLAHE on each RGB channel
  * CLAHE only on luminance/value channel

What to understand:

* histogram = how brightness values are distributed
* contrast stretching spreads intensities wider
* gamma correction brightens or darkens nonlinearly
* histogram equalization improves contrast
* CLAHE improves local contrast in smaller areas

Lab 3

* Applies average, Gaussian, and median filters
* Sharpens with Laplacian and unsharp masking
* Adds Gaussian noise and salt-and-pepper noise
* Filters noisy images
* Computes PSNR to compare quality

What to understand:

* average filter smooths but blurs edges
* Gaussian filter smooths more naturally
* median filter is strong for salt-and-pepper noise
* Laplacian emphasizes edges
* unsharp masking sharpens by adding edge detail back
* PSNR tells how close restored image is to original

Lab 4

* Computes FFT of grayscale image
* Shows magnitude and phase
* Applies ideal low-pass, Gaussian low-pass, Gaussian high-pass
* Reconstructs image using inverse FFT
* Compares frequency Gaussian blur with spatial Gaussian blur

What to understand:

* FFT changes image from spatial domain to frequency domain
* low frequencies = smooth areas
* high frequencies = edges/details
* low-pass keeps smooth structure
* high-pass keeps edge/detail structure

Lab 5

* Builds box, Laplacian, and Sobel kernels
* Pads them to image size
* Finds kernel frequency responses
* Creates a band-pass filter
* Applies high-frequency emphasis filtering

What to understand:

* kernels in spatial domain have frequency behavior too
* box blur passes low frequencies
* Sobel and Laplacian emphasize edges/high frequencies
* band-pass keeps middle-frequency information
* high-frequency emphasis sharpens while preserving some original image

How you should study it

Open the script and do this:

* Run only Lab 1 first
* Look at the saved output images
* Read the comments line by line
* Then move to Lab 2
* Do not jump to FFT first

Best learning order:

* Lab 1: understand images as arrays
* Lab 2: understand brightness and histograms
* Lab 3: understand filtering in spatial domain
* Lab 4: understand FFT and frequency domain
* Lab 5: connect kernels and frequency response

What to write in your report

For each task, use this format:

* Objective: what this step does
* Method: what function/filter you used
* Parameters: kernel size, sigma, gamma, cutoff, etc.
* Observation: what changed visually
* Conclusion: which method worked best and why

Example:
“Median filtering performed better on salt-and-pepper noise because it removes isolated extreme pixels without blurring edges as much as averaging.”

One important note:
Your PDF’s page 9 cuts off right after “High-Frequency Emphasis: Implement high-frequency emphasis filtering using the formula:”. The visible formula is missing in the uploaded file, so I used the standard image-processing form:
`H_hfe(u,v) = a + b * H_hp(u,v)`
That is the usual formula for high-frequency emphasis filtering.

How to run it

Install packages:

```bash
pip install numpy matplotlib scikit-image opencv-python scipy
```

Run:

```bash
python dip_lab_solution_guide.py
```

Then check the generated images in the `outputs` folders.

What I’d recommend you do next:
Run Lab 1 first, then paste me the first 30–40 lines of the script or a screenshot of the output, and I’ll explain it line by line in very simple words.
