import numpy as np
from PIL import Image
import os
import cv2
import sys

def main():
    param = sys.argv
    degraded_image = cv2.imread(param[1], 0)
    max_threshold_val, image = cv2.threshold(degraded_image, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    max_threshold_val2, image2 = cv2.threshold(degraded_image, 0, 255, cv2.THRESH_OTSU)
    min_threshold_val = int(0.5 * max_threshold_val)
    min_threshold_val2 = int(0.5 * max_threshold_val2)
    canny_image = cv2.Canny(degraded_image, min_threshold_val, max_threshold_val)
    canny_image2 = cv2.Canny(degraded_image, min_threshold_val2, max_threshold_val2)

    print(max_threshold_val)
    print(max_threshold_val2)
    cv2.imshow("binary_image", canny_image)
    cv2.imshow("binary_image2", canny_image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()