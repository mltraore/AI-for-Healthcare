import numpy as np
import torch 
import torch.nn as nn
import torch.nn.functional as F

from PIL import Image
import matplotlib.pyplot as plt

# kernel
conv_kernel = np.ones((4, 4))
conv_kernel[2:, :] = -1
print(f"kernel\n{conv_kernel}")


# conv2D layer
conv2d = nn.Conv2d(
   1, # input
   1, # output
   kernel_size = (4, 4),
   bias = False
)

print(f"conv2d info:\n{conv2d}")

# setting a custom weight for the conv2D layer
params = torch.from_numpy(conv_kernel).type(torch.FloatTensor).unsqueeze(0).unsqueeze(0)

conv2d.weight = nn.Parameter(params)

print(f"custom weights:\n{params}")


rgb_img = Image.open("walrus.jpg")
gray_img = rgb_img.convert('L')

uint = np.array(gray_img) / 0xff
print(f"uint: type:{uint.dtype} max:{uint.max()}  min:{uint.min()}")

single = np.array(gray_img).astype(np.single) / 0xff
print(f"single: type:{single.dtype} max:{single.max()}  min:{single.min()}")

img_arr = np.array(gray_img).astype(np.single) / 0xff

print(img_arr.dtype)

#plt.imshow(img_arr, cmap = "gray")
#plt.show()


# (batch, c,w,h)
img_tensor = torch.from_numpy(img_arr).type(torch.FloatTensor).unsqueeze(0).unsqueeze(1)

print(f"image_tensor: {img_tensor.shape}")


convolved = conv2d(img_tensor)
relu = F.relu(convolved)

print(f"relu output shape: {relu.shape}")

"""
fig, axes = plt.subplots(1, 3, figsize=(12,12))

axes = axes.flatten()

axes[0].imshow(img_arr, cmap='gray')
axes[1].imshow(np.squeeze(convolved.detach().numpy()), cmap='gray')
axes[2].imshow(np.squeeze(relu.detach().numpy()), cmap='gray')

plt.show()
"""

# loading nifti data
import nibabel as nib

nib_data = nib.load("spleen.nii.gz")

nib_img = nib_data.get_fdata()


print("nib image shape: {nib_img.shape}")

"""
plt.imshow(np.rot90(nib_img[:,:, 0]), cmap='gray') # axial
plt.title('axial')
plt.show()
"""

# sagittal axe

pix_dim = nib_data.header['pixdim']

print(f"pixel dim: {pix_dim}")

ar = pix_dim[3] / pix_dim[1]

print(f"aspect ration: {ar}")


"""
plt.imshow(np.rot90(nib_img[250,:, :]), aspect=ar, cmap='gray') # sagittal
plt.title('Sagittal')
plt.show()
"""


def plot_slices(volume, plot_dim, trans=True, fig_name="convolved.png"):
 
  if trans:
    volume = np.transpose(volume, (2, 0, 1))
  
  fig, axes = plt.subplots(*plot_dim, figsize=[50, 50])
  list_axes = axes.flatten()
  
  for i, img in enumerate(volume):
    list_axes[i].imshow(np.rot90(img), cmap="gray")
    list_axes[i].set_title(f"slice {i+1}",  fontsize=12, pad=2)
    list_axes[i].axis("off")

  if len(list_axes) > len(volume):
     for i in range(len(volume), len(list_axes)):
       list_axes[i].axis("off")
       list_axes[i].set_visible(False)
  
  #plt.tight_layout(w_pad=0.2)  
  #plt.subplots_adjust(wspace=0.0)
  #print(volume.shape)
  #print(n_slices)



  #plt.show()
  plt.savefig(fig_name)

# plot_slices(nib_img, (6, 7))


## convolution 2D
from time import perf_counter

def conv2d_slices(volume):
  conv_slices = []
  relu_slices = []
  volume = np.transpose(volume, (2, 0, 1))
  for i, _slice in enumerate(volume):
    slice_tensor = torch.from_numpy(_slice).type(torch.FloatTensor).unsqueeze(0).unsqueeze(1)
    #print(slice_tensor.shape)
    
    convolved = conv2d(slice_tensor)
    relu = F.relu(convolved)

    conv2d_slice = np.squeeze(convolved.detach().numpy())
    relu_slice = np.squeeze(relu.detach().numpy())
    
    conv_slices.append(conv2d_slice)
    relu_slices.append(relu_slice)
    
  return conv_slices, relu_slices


s_time = perf_counter()

conv2d_slices, relu_slices = conv2d_slices(nib_img)

e_time = perf_counter()

print(f"Time elapsed (2D): {e_time - s_time}s")

#---------- save plots
#plot_slices(np.array(conv2d_slices), (7, 7), trans=False)
#plot_slices(np.array(relu_slices), (7, 7), trans=False, fig_name="relu.png")

print(f"conv2d params' shape: {conv2d.weight.shape}")
print(f"trainable params: {np.prod(conv2d.weight.shape)}")

## 3D Convolutions

conv3d = nn.Conv3d(
    1, 
    1,
    kernel_size = (4, 4, 4),
    bias = False
)

conv3d_kernel = np.array([conv_kernel, conv_kernel, conv_kernel, conv_kernel])
conv3d_kernel = torch.from_numpy(conv3d_kernel).type(torch.FloatTensor).unsqueeze(0).unsqueeze(0)

conv3d.weight = nn.Parameter(conv3d_kernel)

print(f"conv3d details: {conv3d}")
print(f"conv3d kernel shape: {conv3d_kernel.shape}")
print(f"conv3d weights:\n{conv3d.weight}")

conv_tensor = torch.from_numpy(nib_img.astype(np.single)/0xff).unsqueeze(0).unsqueeze(1)

print(f"conv tensor shape: {conv_tensor.shape}")

convolved3d = conv3d(conv_tensor)
relu3d = F.relu(convolved3d)

print(f"3d convolved shape: {convolved3d.shape}")
print(f"3d relu3d shape: {relu3d.shape}")


#---------- save plots
plot_slices(np.squeeze(convolved3d.detach().numpy()), (5, 8), trans=True, fig_name="conv3d.png")
plot_slices(np.squeeze(relu3d.detach().numpy()), (5, 8), trans=True, fig_name="relu3d.png")

