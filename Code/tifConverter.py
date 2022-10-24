from PIL import Image, ImageSequence
import cv2
import numpy as np
import os

path = "DataSets/TIFs"
writePath = "DataSets/OCTBs"
folders = os.listdir(path)
mode = 0o666
print(os.listdir(path))

# for file in folders:
#     name = file.split(".")[0]
#     print(name)

#     im = Image.open(path + "/" + file)

#     for i, page in enumerate(ImageSequence.Iterator(im)):
#         page.save(writePath + "/" + name + "/" + name + "%d.png" % i)

for file in folders:
    name = file.split(".")[0]
    print(name)

    for image in os.listdir(writePath + "/" + name):
        img = cv2.imread(writePath + "/" + name + "/" + image , 1)
        kernel = np.ones((3,3), np.float32)/9

        filt_2D = cv2.filter2D(img, -1, kernel)

        cv2.imshow("try1", filt_2D)

cv2.waitKey(0)
cv2.destroyAllWindows()


    