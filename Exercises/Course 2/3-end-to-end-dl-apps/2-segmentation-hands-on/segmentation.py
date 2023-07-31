import numpy as np
import numpy.ma as ma

import nibabel as nib

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import matplotlib.pyplot as plt

from collections import OrderedDict

class UNet(nn.Module):
    def __init__(self, in_channels=1, out_channels=1, init_features=32):
        super(UNet, self).__init__()

        features = init_features


        self.encoder1 = self.unet_block(in_channels, features, name="enc1")
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.encoder2 = self.unet_block(features, features * 2, name="enc2")
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.encoder3 = self.unet_block(features * 2, features * 4, name="enc3")
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.encoder4 = self.unet_block(features * 4, features * 8, name="enc4")
        self.pool4 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.bottleneck = self.unet_block(features * 8, features * 16, name="bottleneck")
        
    
        self.upconv4 = nn.ConvTranspose2d(
            features * 16, features * 8, kernel_size=2, stride=2
        )

        self.decoder4 = self.unet_block((features * 8) * 2, features * 8, name="dec4")

        self.upconv3 = nn.ConvTranspose2d(
            features * 8, features * 4, kernel_size=2, stride=2
        )
        self.decoder3 = self.unet_block((features * 4) * 2, features * 4, name="dec3")

        
        self.upconv2 = nn.ConvTranspose2d(
            features * 4, features * 2, kernel_size=2, stride=2
        )
        self.decoder2 = self.unet_block((features * 2) * 2, features * 2, name="dec2")
        

        self.upconv1 = nn.ConvTranspose2d(
            features * 2, features, kernel_size=2, stride=2
        )
        self.decoder1 = self.unet_block(features * 2, features, name="dec1")

        self.conv = nn.Conv2d(
            in_channels=features, out_channels=out_channels, kernel_size=1
        )

        self.softmax = nn.Softmax(dim=1)


    def forward(self, x):
        enc1 = self.encoder1(x)
        enc2 = self.encoder2(self.pool1(enc1))
        enc3 = self.encoder3(self.pool2(enc2))
        enc4 = self.encoder4(self.pool3(enc3))

        bottleneck = self.bottleneck(self.pool4(enc4))

        dec4 = self.upconv4(bottleneck)
        dec4 = torch.cat((dec4, enc4), dim=1)
        dec4 = self.decoder4(dec4)

        dec3 = self.upconv3(dec4)
        dec3 = torch.cat((dec3, enc3), dim=1)
        dec3 = self.decoder3(dec3)
        
        dec2 = self.upconv2(dec3)
        dec2 = torch.cat((dec2, enc2), dim=1)
        dec2 = self.decoder2(dec2)
        
        dec1 = self.upconv1(dec2)
        dec1 = torch.cat((dec1, enc1), dim=1)
        dec1 = self.decoder1(dec1)

        out_conv = self.conv(dec1)

        return self.softmax(out_conv)

    def unet_block(self, in_channels, features, name):
        return nn.Sequential(
            OrderedDict(
               [
                 (name + "_conv1",
                  nn.Conv2d(
                    in_channels=in_channels,
                    out_channels=features,
                    kernel_size=3,
                    padding=1,
                    bias=False
                  )
                 ),
                 (name + "_norm1", nn.BatchNorm2d(num_features=features)),
                 (name + "_relu1", nn.ReLU(inplace=True)),


                 (name + "_conv2",
                  nn.Conv2d(
                    in_channels=features,
                    out_channels=features,
                    kernel_size=3,
                    padding=1,
                    bias=False
                  )
                 ),
                 (name + "_norm2", nn.BatchNorm2d(num_features=features)),
                 (name + "_relu2", nn.ReLU(inplace=True)),
               ] 
            )
        )

#print(UNet())

## Loading data
training_volume = nib.load("data/spleen1_img.nii.gz").get_fdata()
training_label  = nib.load("data/spleen1_label.nii.gz").get_fdata()

print(f"training volume shape: {training_volume.shape}")
print(f"training label  shape: {training_label.shape}")

print(f"label unique: {np.unique(training_label)}")
print(f"slice min: {training_volume.min()} max: {training_volume.max()}")

# viz
# plt.imshow(np.rot90(training_volume[:, :, 5] + training_label[:, :, 5]*training_volume.max()), cmap="gray")
# plt.show()

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print(f"device: {device}")

unet = UNet(1, 2)

# move all trainable params to the device
unet.to(device)

loss = torch.nn.CrossEntropyLoss()

optimizer = optim.Adam(unet.parameters(), lr=0.001)
optimizer.zero_grad()

# number of parameters
n_params = sum(p.numel() for p in unet.parameters() if p.requires_grad)
print(f"number of trainable params: {n_params}")


# set up the model for training
unet.train()


for epoch in range(0, 5):
    for slice_ix in range(0, 10):
        slc = training_volume[:, :, slice_ix].astype(np.single) / np.max(training_volume[:, :, slice_ix])
        slc_tensor = torch.from_numpy(slc).unsqueeze(0).unsqueeze(0).to(device)
        
        label = training_label[:, :, slice_ix].astype(np.uint8)
        label_tensor = torch.from_numpy(label).unsqueeze(0).long().to(device)

        #print(slc_tensor.shape)
        #print(label_tensor.shape)      
        #print(np.unique(label_tensor))
      
        optimizer.zero_grad()
        pred = unet(slc_tensor)

        l = loss(pred, label_tensor)
        l.backward()
        optimizer.step()
    
    print(f"Epoch: {epoch}, training loss: {l}")

#plt.imshow(pred.cpu().detach()[0,1])
#plt.show()

unet.eval()

def inference(img):
  test_tensor = torch.from_numpy(img.astype(np.single)/np.max(img)).unsqueeze(0).unsqueeze(0)
  pred = unet(test_tensor.to(device))
  return np.squeeze(pred.cpu().detach())

level = 11

test_img = training_volume[:, :, level]
pred = inference(test_img)

print(f"predicted mask shape: {pred.shape}")
#plt.imshow(pred[0])
#plt.show()

print(f"pred[0]: {np.unique(pred[0])}")
print(f"pred[1]: {np.unique(pred[1])}")

#mask = torch.argmax(pred, dim=0)
#plt.imshow(mask)
#plt.show()

# creating NIFTI volume from predicted masks
mask3d = np.zeros(training_volume.shape)

for slice_ix in range(training_volume.shape[2]):
    pred = inference(training_volume[:, :, slice_ix])
    mask3d[:, :, slice_ix] = torch.argmax(pred, dim=0)

org_volume = nib.load("data/spleen1_img.nii.gz")
print(f"Affine: {org_volume.affine}")

img_out = nib.Nifti1Image(mask3d, org_volume.affine)
nib.save(img_out, "data/out1.nii.gz")



