import cv2

class Image_Processor:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)  # Load the image from the specified path

    def show_image(self):
        cv2.imshow('Original Image', self.image)  # Display the original image
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def remove_noise(self):
        denoised_image = cv2.fastNlMeansDenoisingColored(self.image, None, 10, 10, 7, 21)  # Remove noise from the image
        cv2.imshow('Denoised Image', denoised_image)  # Display the denoised image
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def remove_background(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale
        _, thresh = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)  # Apply thresholding to get a binary image
        inverted_thresh = cv2.bitwise_not(thresh)  # Invert the binary image
        background_removed_image = cv2.bitwise_and(self.image, self.image, mask=inverted_thresh)  # Remove the background
        cv2.imshow('Background Removed Image', background_removed_image)  # Display the background removed image
        cv2.waitKey(0)
        cv2.destroyAllWindows()