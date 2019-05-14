import cv2
import numpy as np
from collections import Counter
import sys

def pp(img, name='img'): # print profile for image 
  print('{}: val=[{:.2f} - {:.2f}], shape={}, std={:.2f}, mean={:.2f}, sum={}, top={}'.format(
          name, img.min(), img.max(), img.shape, img.std(), img.mean(), img.sum(),
          Counter(img.ravel()).most_common()[:10]))

H=150
W=200
def pad(img, h, w):
  img = img[:h, :w]
  px = (h - img.shape[0], 0)
  py = (w - img.shape[1], 0)
  return np.pad(img, (px,py), 'constant') # pad with 0
def pad3(img3, h, w):
  ret = np.zeros((h,w,3))
  for i in range(3):
    img = img3[:h, :w, i]
    px = (h - img.shape[0], 0)
    py = (w - img.shape[1], 0)
    ret[:,:,i] = np.pad(img, (px,py), 'constant') # pad with 0
  return ret
def normalize_01(img):
  img = img.astype(np.float64)
  img = img - img.min()
  if img.max():
      img = img / img.max()
  return img.astype(np.float64)

edges = cv2.imread(sys.argv[1])
saliency = cv2.imread(sys.argv[2])
saliency = pad3(saliency, H, W)
saliency = 1-normalize_01(saliency)
saliency[saliency < 0.25] = 0
#saliency[saliency > 0.85] = 1
pp(edges)
pp(saliency)
prod = edges*0 + (edges * saliency)
prod = normalize_01(prod)
prod[prod>0.75] = 1
prod *=255
cv2.imwrite(sys.argv[3], prod)

