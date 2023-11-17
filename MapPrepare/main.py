import numpy as np
import matplotlib.pyplot as plt

# from skimage.filters import sobel, threshold_otsu, threshold_local
# from skimage.measure import label, regionprops
# from skimage.morphology import *
# from collections import defaultdict
# from skimage import color

img = plt.imread("karta-01.bmp")

plt.figure()

plt.subplot(121)
plt.imshow(img)

mask = img.mean(2)

startPointCoords = np.where(mask==156.7)
print(startPointCoords)
endPointCoords = np.where(mask==100.3)

mask[mask < 10] = 0
mask[mask > 0 ] = 255

res = np.zeros(shape=(mask.shape[0], mask.shape[1], 3))

for y in range(0, mask.shape[0]):
    for x in range(0, mask.shape[1]):
        if mask[y][x] != 0:
            res[y][x] = [255, 255, 255]

plt.subplot(122)
plt.imshow(res)

plt.show()

plt.imsave("kartaFormatted.bmp", res)