import numpy as np
import nibabel as nib

def sensitivity(gt, pred):
  # tp / (tp + fn)
  tp = np.sum((gt == 1) & (pred == 1))
  fn = np.sum((gt == 1) & (pred == 0))
  
  if tp + fn == 0:
    return -1

  return tp / (tp + fn)

def dice_score(gt, pred):
  # 2*|gt int pred| / |gt|+|pred|
  intersection = np.sum(gt * pred)
  sum_ = np.sum(gt) + np.sum(pred)

  if sum_ == 0:
    return -1
    
  return 2 * intersection / sum_

if __name__ == "__main__":
    gt   = nib.load("data/spleen1_label_auto.nii.gz").get_fdata()
    pred = nib.load("data/spleen1_label_gt.nii.gz").get_fdata()

    print(f"ground truth -> shape: {gt.shape},  values: {np.unique(gt)}")
    print(f"preds        -> shape: {pred.shape},  values: {np.unique(pred)}")
   
    tpr = sensitivity(gt, pred)
    dsc = dice_score(gt, pred)

    print(f"sensitivity = {tpr*100:.2f}%")
    print(f"dice score  = {dsc*100:.2f}%")
