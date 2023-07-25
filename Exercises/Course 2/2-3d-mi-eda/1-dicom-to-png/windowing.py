import pydicom
import numpy as np
import matplotlib.pyplot as plt

# Load the DICOM image file
dcm = pydicom.dcmread('instance.dcm')

# Extract the pixel array from DICOM image
image_array = dcm.pixel_array

# Apply WW/WC transform
window_center = 2472 #0#400#40#dcm.WindowCenter
window_width = 4144 #1#700#30#dcm.WindowWidth

# Calculate the range of pixel values for the display
min_pixel_value = window_center - (window_width / 2)
max_pixel_value = window_center + (window_width / 2)

# Clip the pixel values to the display range
clipped_array = np.clip(image_array, min_pixel_value, max_pixel_value)

# Rescale the clipped array to the full 8-bit range (0-255)
rescaled_array = ((clipped_array - min_pixel_value) / (max_pixel_value - min_pixel_value)) * 255

# Convert the rescaled array to uint8 data type
rescaled_array = rescaled_array.astype(np.uint8)

# Display the image using matplotlib
plt.imshow(rescaled_array, cmap='gray')
plt.axis('off')
plt.show()
