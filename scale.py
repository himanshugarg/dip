import cv2
import numpy as np
import os
import sys

# read input
(path, scale_x, scale_y) = sys.argv[1:]
img = cv2.imread(path)

# rotate
scaled = cv2.resize(img, None, fx=float(scale_x), fy=float(scale_y), interpolation = cv2.INTER_CUBIC)

# write
path_prefix, path_ext = os.path.splitext(path)
new_path = path_prefix + '_scaled_' + scale_x + "_" + scale_y + '.' + path_ext
cv2.imwrite(new_path, scaled)
print "output written to " + new_path
