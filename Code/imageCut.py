from PIL import Image
import os
# import cv2

directory = 'DataSets'
folders = os.listdir(directory)
print(os.listdir(directory))

for folder in folders:
    f = os.path.join(directory, folder)
    images = os.listdir(f)
    for image in images:
        print(image)
        path = os.path.join(f, image)
        img = Image.open(path)
        w, h = img.size
        box = (0, 719, 834, 1553)
        im1 = img.crop(box)
        im1.show()