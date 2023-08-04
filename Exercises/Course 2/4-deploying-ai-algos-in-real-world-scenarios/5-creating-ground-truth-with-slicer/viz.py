import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt

nib_imgs = nib.load("spleen1_img.nii.gz").get_fdata()
#nib_lbls = nib.load("spleen1_label.nii.gz").get_fdata()
nib_lbls = nib.load("created_labels.nii.gz").get_fdata()


print(f"Imgs shape: {nib_imgs.shape}")
print(f"GT labels shape: {nib_lbls.shape}")


# viz

fig, axes = plt.subplots(1, 3, figsize=[12, 12])
axes = axes.flatten()

axes[0].imshow(np.rot90(nib_imgs[:, :, 1]), cmap='gray')
axes[0].set_title("Slice")
axes[0].axis("off")

axes[1].imshow(np.rot90(nib_lbls[:, :, 1]), cmap='gray')
axes[1].set_title("GT label")
axes[1].axis("off")


axes[2].imshow(np.rot90(nib_imgs[:, :, 1] + nib_lbls[:, :, 1]*500), cmap='gray')
axes[2].set_title("Overlapped")
axes[2].axis("off")

plt.show()
