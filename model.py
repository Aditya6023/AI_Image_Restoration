import cv2


def restore_image(input_path: str, output_path: str):
    """
    Simple AI restoration placeholder.
    Enhances image using sharpening + denoise.
    """

    # read image
    image = cv2.imread(input_path)

    if image is None:
        raise Exception("Image not found")

    # --- DENOISE ---
    denoised = cv2.fastNlMeansDenoisingColored(
        image, None, 10, 10, 7, 21
    )

    # --- SHARPEN ---
    kernel = [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]

    kernel = cv2.UMat(cv2.getGaussianKernel(3, 0))
    sharpened = cv2.filter2D(denoised, -1, kernel)

    # save result
    cv2.imwrite(output_path, sharpened)