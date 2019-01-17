import cv2
import math

img = cv2.imread("../../samples/world.png") # 512x512

img_shape = img.shape
tile_size = (16, 16)
offset = (16, 16)

for i in range(int(math.ceil(img_shape[0]/(offset[1] * 1.0)))):
    for j in range(int(math.ceil(img_shape[1]/(offset[0] * 1.0)))):
        cropped_img = img[offset[1]*i:min(offset[1]*i+tile_size[1], img_shape[0]), offset[0]*j:min(offset[0]*j+tile_size[0], img_shape[1])]
        # Debugging the tiles
        cv2.imwrite("debug_" + str(i) + "_" + str(j) + ".png", cropped_img)
