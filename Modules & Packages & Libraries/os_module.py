import os

cwd = os.getcwd()  # get address and directory this file

print(cwd)

my_image = "D:\Business\Education\course notes\computer vision Aije Egwaikhide coursera\week 2\1. what is a digital image\16"

image_path = os.path.join(cwd, my_image)  # get address and directory of an image

print(image_path)
