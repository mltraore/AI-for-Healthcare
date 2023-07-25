import os
import pydicom
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# Load the volume into array of slices
vpath = "volume"
slices = [pydicom.dcmread(os.path.join(vpath, sfile))
          for sfile in os.listdir(vpath)]

slices = sorted(slices, key = lambda dcm: dcm.ImagePositionPatient[0])

# What are the dimensions?
print(f'{len(slices)} of size {slices[0].Rows}x{slices[0].Columns}')

# What is the modality?
print(f'Modaliy: {slices[0].Modality}')

# What is the slice spacing?
print(f'Pixel spacing: {slices[0].PixelSpacing},\nSlice thickness: {slices[0].SliceThickness}')

# Load image data into numpy array
image_data = np.stack([s.pixel_array for s in slices])
print(image_data.shape)

# %%
print("Saving axial: ")

# Extract slice  / the middle slice for better understanding
axial = image_data[image_data.shape[0] // 2]
plt.imshow(axial, cmap='gray')
#plt.show()

#saving using full-range window
im = Image.fromarray((axial/np.max(axial)*0xff).astype(np.uint8), mode="L")
im.save("axial.png")

# %%
# print("Saving sagittal: ")
# Extract slice
sagittal = image_data[:, :, image_data.shape[2] // 2]
print(sagittal.shape) # (24, 320)

# Compute aspect ratio
ar = slices[0].SliceThickness / slices[0].PixelSpacing[0]

plt.imshow(sagittal, cmap='gray', aspect=ar)
#plt.show()

im = Image.fromarray((sagittal/np.max(sagittal)*0xff).astype(np.uint8), mode="L")

#rIm = im.resize((sagittal.shape[1], int(sagittal.shape[0]*ar)))
rIm = im.resize((int(sagittal.shape[0]*ar), sagittal.shape[1]))
rIm.save('sagittal.png')

# %%
print("Saving Coronal: ")
# Extract slice
coronal = image_data[:, image_data.shape[1]//2, :]
print(coronal.shape) # (24, 260)

# save the full-range window
im = Image.fromarray((coronal/np.max(coronal)*0xff).astype("uint8"), mode="L")
rIm = im.resize((coronal.shape[1], int(coronal.shape[0]*ar)))
rIm.save("coronal.png")



