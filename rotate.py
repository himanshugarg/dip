import cv2
import numpy as np
import os
import sys

# read input
(path, angle, scale) = sys.argv[1:]
img = cv2.imread(path)

# rotate
(rows, cols) = img.shape[:2]
rm = cv2.getRotationMatrix2D((cols/2, rows/2), float(angle), float(scale))
rotated = cv2.warpAffine(img, rm, (cols, rows))

# write
path_prefix, path_ext = os.path.splitext(path)
new_path = path_prefix + '_rotated_' + angle + "_" + scale + '.' + path_ext
cv2.imwrite(new_path, rotated)
print "output written to " + new_path
