import cv2
from cv2.gapi import BGR2Gray
import numpy as np


def save_img(file, img):
    cv2.imwrite(f"solutions/{file}", img)


def sobel_edge_detection(image):
    blur = cv2.GaussianBlur(image, (3, 3), 0)
    sobel = cv2.Sobel(blur, cv2.CV_64F, dx=1, dy=1, ksize=1)
    save_img("sobel.png", sobel)


def canny_edge_detection(image, threshold_1, threshold_2):
    blur = cv2.GaussianBlur(image, (3, 3), 0)
    canny = cv2.Canny(blur, threshold_1, threshold_2)
    save_img("canny.png", canny)


def template_match(image, template):

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    w, h = template_gray.shape[::-1]
    res = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    save_img("template.png", image)


def resize(image, scale_factor, up_or_down):
    if up_or_down.lower() == "up":
        for _ in range(scale_factor):
            image = cv2.pyrUp(image)

    elif up_or_down.lower() == "down":
        for _ in range(scale_factor):
            image = cv2.pyrDown(image)

    save_img("resize.png", image)


def main():
    lambo = cv2.imread("lambo.png")
    shapes = cv2.imread("shapes.png")
    shapes_template = cv2.imread("shapes_template.jpg")
    canny_edge_detection(lambo, 50, 50)
    sobel_edge_detection(lambo)
    template_match(shapes, shapes_template)
    resize(lambo, 2, "down")


if __name__ == "__main__":
    main()
