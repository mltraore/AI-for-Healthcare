import os 
import numpy as np
import pydicom
import warnings

import matplotlib.pyplot as plt

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 


rpath = r"data"

dirs = np.asarray([[(os.path.join(dp, f), pydicom.dcmread(os.path.join(dp, f), stop_before_pixels=True)) for f in files] 
                 for dp, _, files in os.walk(rpath) if len(files) != 0])

# How many dirs
print(f'Dir number: {len(dirs)}')

# number of instances
instances = dirs[0]
print(f'Instance number: {len(instances)}')

# number of series
series_uids = np.unique([inst[1].SeriesInstanceUID for inst in instances])
print(f'Series number: {len(series_uids)}')

# number of studies
studies_uids = [inst[1].StudyInstanceUID for inst in instances]
print(f'Studies number: {len(np.unique(studies_uids))}')

# patients
patient_ids = np.unique([inst[1].PatientID for inst in instances])
print(f'Number of patients: {len(patient_ids)}, patient IDs: {patient_ids}')


# sample dicom metadata
print(instances[0][1])


# imaging modalities
modalities = np.unique([inst[1].Modality for inst in instances])
print(f'Number of modalities: {len(modalities)}, Modalities: {(modalities)}')

# imaging modalities per series
series_uids_modalities = [(suid, np.unique([inst[1].Modality for inst in instances if inst[1].SeriesInstanceUID == suid])) for suid in series_uids]

#for item in series_uids_modalities:
#  print(f'{item[0]:65}: {item[1]}')

# sample from ct scans
ct_scans = [pydicom.dcmread(inst[0]) for inst in instances if inst[1].SeriesInstanceUID == '1.2.826.0.1.3680043.2.1125.1.45859137663006505718300393375464286']

print(f'CT sample number: {len(ct_scans)}')

ct_img = ct_scans[10].pixel_array 

# sample from mr scans
#1
mri_1 =  [pydicom.dcmread(inst[0]) for inst in instances if inst[1].SeriesInstanceUID == '1.3.6.1.4.1.14519.5.2.1.4429.7055.111299569371716382165219422799']

print(f'MRI 1 sample number: {len(mri_1)}')

mri_1_img = mri_1[10].pixel_array

#2 
mri_2 =  [pydicom.dcmread(inst[0]) for inst in instances if inst[1].SeriesInstanceUID == '1.3.6.1.4.1.14519.5.2.1.4429.7055.732954519300668202085572772042']

print(f'MRI 2 sample number: {len(mri_2)}')

mri_2_img = mri_2[10].pixel_array


# plotting sample from modalities
_, axes = plt.subplots(1, 3, figsize=[12, 8])
m_axes = axes.flatten()
titles = ['CT', 'MR1', 'MR2']
images = [ct_img, mri_1_img, mri_2_img]
for i, ax in enumerate(axes):
  ax.set_title(titles[i])
  ax.imshow(images[i], cmap='gray')
  ax.axis('off')

#plt.show()
# the most oldest and most recent studies
from collections import defaultdict
study_dates = defaultdict(set)

for inst in instances:
   s_uid = inst[1].StudyInstanceUID
   s_date = inst[1].StudyDate
   study_dates[s_uid].add(s_date)

study_dates = dict(sorted(study_dates.items(), key=lambda item: np.max(item[1])))

for k, v in study_dates.items():
  print(f'{k:65}: {v}')

# study date
study_date = sorted(np.unique([inst[1].StudyDate for inst in instances]))

print(study_date)


# outliers

slices_odd_mr = [pydicom.dcmread(inst[0]) for inst in instances if inst[1].StudyDate == "20150116"]

series_ = np.unique([inst.SeriesInstanceUID for inst in slices_odd_mr])

print(f'Slice number in this study: {len(slices_odd_mr)}')
print(f'List of series: {series_}') # only one series --> a whole volume (outlier)

plt.figure()
plt.imshow(slices_odd_mr[ len(slices_odd_mr) // 2].pixel_array, cmap='jet')
#plt.show()


volumes = dict()

for inst in instances:
  sid = inst[1].SeriesInstanceUID
  if sid not in volumes:
     volumes[sid] = dict()
     volumes[sid]["Study Date"] = inst[1].StudyDate
     volumes[sid]["Rows"] = inst[1].Rows
     volumes[sid]["Columns"] = inst[1].Columns
     volumes[sid]["Patient ID"] = inst[1].PatientID
  else:
     pass

  if "Count_instance" not in volumes[sid]:
     volumes[sid]["Count_instance"] = 0
  else:
     volumes[sid]["Count_instance"] += 1


for k, v in volumes.items():
  print(f'{k:65}: {v}')





print("Spatial Resolutions: (rows×columns×number_of_slice)")

for sid in series_uids:
  volume_info = volumes[sid]
  
  print(f"{volume_info['Rows']}x{volume_info['Columns']}x{volume_info['Count_instance']}")
