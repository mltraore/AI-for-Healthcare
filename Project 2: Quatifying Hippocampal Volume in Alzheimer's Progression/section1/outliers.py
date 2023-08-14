import os
import numpy as np
import pandas as pd
import nibabel as nib
import matplotlib.pyplot as plt


images_dir = r"../data/TrainingSet/images"

images_path = [f for f in os.listdir(images_dir)]

images_list = []

for img in images_path:
    image = nib.load(os.path.join(images_dir, img)).get_fdata()
    
    images_list.append({
    'path': os.path.join(images_dir, img),
    'slice_no': image.shape[0],
    'height': image.shape[1],
    'width': image.shape[2]
    })

 
images_df = pd.DataFrame(images_list)


def find_outliers(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = (column < lower_bound) | (column > upper_bound)
    return outliers

# Find outlier files based on columns 'slice_no', 'height', and 'width'
outliers_slice = find_outliers(images_df['slice_no'])
outliers_height = find_outliers(images_df['height'])
outliers_width = find_outliers(images_df['width'])

# Combine outlier flags for all columns
outliers = outliers_slice & outliers_height & outliers_width

# Identify outlier files based on the 'path' column
outlier_files = images_df.loc[outliers, 'path']

print("Outlier Files:")
print(outlier_files)

