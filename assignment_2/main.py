import cv2
import numpy as np


def save_img(file, img):
    cv2.imwrite(f"solutions/{file}", img)


def padding(image, border_width):
    return cv2.copyMakeBorder(
        image,
        border_width,
        border_width,
        border_width,
        border_width,
        cv2.BORDER_REFLECT,
    )


def crop(image, x_0, x_1, y_0, y_1):
    height, width, _ = image.shape

    left = x_0
    right = width - x_1
    top = y_0
    bot = height - y_1

    return image[top:bot, left:right]


def resize(image, width, height):
    return cv2.resize(image, (width, height))


def copy(image, empty_picture_array):
    height, width, channels = image.shape

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                empty_picture_array[i, j, k] = image[i, j, k]
    return empty_picture_array


def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def hsv(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


def hue_shifted(image, empty_picture_array, hue):
    height, width, channels = image.shape

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                val = int(image[i, j, k]) + hue

                # This is done to keep it inside 0-255
                #
                # The image would have some weird shifts
                # down to the lower end because of each
                # pixel is a uint8.

                if val > 255:
                    val = 255
                elif val < 0:
                    val = 0

                empty_picture_array[i, j, k] = val
    return empty_picture_array


def smoothing(image):
    return cv2.GaussianBlur(image, (15, 15), cv2.BORDER_DEFAULT)


def rotation(image):
    return cv2.rotate(image, cv2.ROTATE_180)


def main():

    img = cv2.imread("lena.png")

    height, width, channels = img.shape
    data_type = img.dtype

    empty_picture_array = np.zeros((height, width, channels), dtype=data_type)

    save_img("padding.png", padding(img, 100))
    save_img("crop.png", crop(img, 80, 130, 80, 130))
    save_img("resize.png", resize(img, 200, 200))
    save_img("copy.png", copy(img, empty_picture_array))
    save_img("grayscale.png", grayscale(img))
    save_img("hsv.png", hsv(img))
    save_img("hue_shifted.png", hue_shifted(img, empty_picture_array, 50))
    save_img("smoothing.png", smoothing(img))
    save_img("rotation.png", rotation(img))


if __name__ == "__main__":
    main()
