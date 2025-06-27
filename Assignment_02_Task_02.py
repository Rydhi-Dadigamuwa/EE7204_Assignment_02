import cv2
import numpy as np

def region_growing(img, seeds, threshold=15):
    height, width = img.shape
    segmented = np.zeros_like(img, dtype=np.uint8)
    visited = np.zeros_like(img, dtype=bool)

    seed_values = [img[y, x] for (y, x) in seeds]
    seed_mean = np.mean(seed_values)

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = list(seeds)

    while stack:
        y, x = stack.pop()
        if visited[y, x]:
            continue
        visited[y, x] = True

        pixel_value = img[y, x]
        if abs(int(pixel_value) - seed_mean) <= threshold:
            segmented[y, x] = 255

            for dy, dx in neighbors:
                ny, nx = y + dy, x + dx
                if 0 <= ny < height and 0 <= nx < width and not visited[ny, nx]:
                    stack.append((ny, nx))

    return segmented

# Load grayscale image
path = r'C:\Users\ASUS\Downloads\Apple.png'
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Check if image loaded
if image is None:
    print("Error: Image not found at specified path.")
    exit()

# Choose seed inside the object 
seed_points = [(150, 150)]

cv2.imshow("Original Image Gray Scaled", image)
result = region_growing(image, seed_points, threshold=80)
cv2.imshow("Region Growing Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
