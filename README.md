# Image Segmentation Techniques – Assignment

This repository contains Python implementations of **two classic image segmentation techniques**:  
1. **Otsu’s Thresholding**  
2. **Region Growing Segmentation**

These solutions were developed as part of a university image processing assignment.

---

## Contents

- `task1_otsu_thresholding.py` – Generates a synthetic image with Gaussian noise and applies Otsu’s algorithm.
- `task2_region_growing.py` – Applies region growing technique using a manually provided grayscale image and seed points.

---

## Task 1: Otsu’s Thresholding with Synthetic Image

This task:
- Synthesizes a grayscale image with 3 intensity levels (background, rectangle, triangle).
- Adds Gaussian noise to simulate real-world conditions.
- Uses **Otsu’s algorithm** to automatically determine the best threshold and segment the image into foreground and background.

### Features:
- Rectangle: Intensity 140  
- Triangle: Intensity 220  
- Background: Intensity 60  
- Noise: Gaussian with `stddev=40`

### Example Output:
- Original image  
- Noisy image  
- Thresholded (binary) image using Otsu's method

---

## Task 2: Region Growing Algorithm

This task:
- Loads a real grayscale image (`Apple.png`)
- Starts from a given **seed point**
- Grows the region recursively if neighboring pixels fall within a certain intensity threshold.

### Features:
- 4-connected neighborhood
- Adjustable threshold (default = 80)
- Interactive region expansion

> Make sure to place `Apple.png` in the correct path or modify the file path in the script.

---

## How to Run

```bash
# Task 1
python task1_otsu_thresholding.py

# Task 2
python task2_region_growing.py
