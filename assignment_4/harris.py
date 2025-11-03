import numpy as np
import cv2


def main():
    img = cv2.imread("reference_img.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Ignore the noise in corners by binarizing the image
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    gray_float = np.float32(binary)
    dst = cv2.cornerHarris(gray_float, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)

    threshold = 0.1 * dst.max()

    img_result = img.copy()
    img_result[dst > threshold] = [0, 0, 255]

    cv2.imwrite("harris.png", img_result)


if __name__ == "__main__":
    main()
