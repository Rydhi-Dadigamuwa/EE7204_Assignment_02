import numpy as np
import cv2

def generate_custom_image(width, height):
    """
    Generates a grayscale image with:
    - Background (gray): 60
    - Rectangle (medium gray): 140
    - Triangle (white): 220
    """
    img = np.ones((height, width), dtype=np.uint8) * 60  # Background

    # Dynamically size the rectangle (left side)
    rect_width = width // 4
    rect_height = height // 3
    rect_x = width // 10
    rect_y = height // 3
    cv2.rectangle(img, 
                  (rect_x, rect_y), 
                  (rect_x + rect_width, rect_y + rect_height), 
                  140, -1)

    # Dynamically size the triangle (right side)
    base_center_x = width * 3 // 4
    base_y = height * 2 // 3
    triangle_height = height // 3

    pts = np.array([
        [base_center_x, base_y - triangle_height],          # Top vertex
        [base_center_x - rect_width // 2, base_y],          # Bottom left
        [base_center_x + rect_width // 2, base_y]           # Bottom right
    ], np.int32)

    cv2.fillPoly(img, [pts], 220)  # Triangle

    return img

def add_gaussian_noise(img, mean=0, stddev=40):
    """Adds Gaussian noise to an image."""
    noise = np.random.normal(mean, stddev, img.shape).astype(np.float32)
    noisy_img = img.astype(np.float32) + noise
    return np.clip(noisy_img, 0, 255).astype(np.uint8)

#Create 2 objects with 3 intensity levels
generated_image = generate_custom_image(640, 480)

#Add Gaussian noise
noisy_img = add_gaussian_noise(generated_image)

#Apply Otsu’s thresholding
_, otsu_result = cv2.threshold(noisy_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#Display results
cv2.imshow("Synthetic Image with 3 intensity Levels", generated_image)
cv2.imshow("Gaussian Noisy Image", noisy_img)
cv2.imshow("Thresholded Image using Otsu", otsu_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
