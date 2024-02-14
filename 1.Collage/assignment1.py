import cv2
import numpy as np
from tkinter import Tk, filedialog

print("Select images for collage.")
Tk().withdraw()  
images_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

collage_width=610
collage_height=2000
target_height=300
collage = np.zeros((collage_height, collage_width, 3), dtype=np.uint8)
x, y = 0, 0
row_height=0
border_size=10
for image_path in images_paths:
    img = cv2.imread(image_path)
    # scale_factor = 0.25
    scale_factor=target_height/img.shape[1]
    img = cv2.resize(img, (0, 0), fx=scale_factor, fy=scale_factor)
    height, width, _ = img.shape
    if x + width > collage_width:
        x = 0
        y += row_height + border_size  
        row_height=0

    collage[y:y+height, x:x+width] = img

    x += width + border_size  
    row_height=max(row_height,height)
cv2.imshow("Collage", collage)
cv2.waitKey(0)
cv2.destroyAllWindows()