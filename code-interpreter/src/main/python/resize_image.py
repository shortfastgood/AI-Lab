import cv2
import numpy as np

# Load the new image using cv2
img_museo_01 = cv2.imread('/mnt/data/20230726_140851.jpg')

# Define new width
new_width = 640

# Calculate the new height to keep the aspect ratio
height_size_new = int(new_width * img_museo_01.shape[0] / img_museo_01.shape[1])

# Resize the image using NumPy array interpolation
img_museo_01_resized = cv2.resize(img_museo_01, (new_width, height_size_new), interpolation=cv2.INTER_AREA)

# Save the image using cv2
cv2.imwrite('/mnt/data/museo_01_small.jpg', img_museo_01_resized)

# Return the path of the resized image
'/mnt/data/museo_01_small.jpg'
