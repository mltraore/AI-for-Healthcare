import numpy as np
import nibabel as nib


def dice_score(gt, cus):
    # 2*|gt int pred| / |gt|+|pred|
    intersection = np.sum(gt * cus)
    sum_ = np.sum(gt) + np.sum(cus)
    
    if sum_ == 0:
        return -1

    return 2 * intersection / sum_



if __name__ == "__main__":
  
  gt_labels = nib.load("data/spleen1_label.nii.gz").get_fdata()
  cus_labels = nib.load("data/created_label.nii.gz").get_fdata()
  
  assert len(gt_labels) == len(cus_labels)

  dcs = dice_score(gt_labels, cus_labels)
  
  print(f"Dice score = {dcs:.2f}%")

