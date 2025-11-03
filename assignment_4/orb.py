import cv2
import numpy as np


def main():
    feat_based_img_alignment("align_this.jpg", "reference_img-1.png", 1500, 0.15)


def feat_based_img_alignment(
    image_to_align, reference_image, max_features, good_match_percent
):
    img_1 = cv2.imread(image_to_align, cv2.IMREAD_COLOR)
    img_2 = cv2.imread(reference_image, cv2.IMREAD_COLOR)

    img_1_gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
    img_2_gray = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(max_features)
    keypoints1, descriptors1 = orb.detectAndCompute(img_1_gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(img_2_gray, None)

    # I hate this example :)
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = matcher.match(descriptors1, descriptors2)

    matches = sorted(matches, key=lambda x: x.distance)

    num_good_matches = int(len(matches) * good_match_percent)
    good_matches = matches[:num_good_matches]

    img_matches = cv2.drawMatches(
        img_1, keypoints1, img_2, keypoints2, good_matches, None
    )
    cv2.imwrite("matches.jpg", img_matches)

    points1 = np.float32([keypoints1[m.queryIdx].pt for m in good_matches])
    points2 = np.float32([keypoints2[m.trainIdx].pt for m in good_matches])

    h, _ = cv2.findHomography(points1, points2, cv2.RANSAC)

    height, width, _ = img_2.shape
    img_1_reg = cv2.warpPerspective(img_1, h, (width, height))

    cv2.imwrite("aligned.jpg", img_1_reg)


if __name__ == "__main__":
    main()
