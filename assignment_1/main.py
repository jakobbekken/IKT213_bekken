import cv2


def print_image_information(image):
    height, width, channels = image.shape
    size = image.size
    data_type = image.dtype

    print(f"""
        Width: {width}
        Height: {height}
        Channels: {channels}
        Size: {size}
        Data type: {data_type}
    """)


def save_web_cam_info(camera, output_file):
    fps = int(camera.get(cv2.CAP_PROP_FPS))
    width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))


    with open(output_file, "w") as f:
        f.write(f"fps: {fps}\n")
        f.write(f"width: {width}\n")
        f.write(f"height: {height}\n")


def main():
    
    # Part 4
    img = cv2.imread("lena.png")
    print_image_information(img)

    # Part 5
    output_file = "solutions/camera_outputs.txt"
    cam = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Forces v4l2 since I am too lazy to install gstreamer for now :)
    save_web_cam_info(cam, output_file)
    cam.release()


if __name__ == "__main__":
    main()
