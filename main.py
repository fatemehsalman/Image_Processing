from src.Image_Processor import Image_Processor

def main_menu():
    print("1. Show Original Image")
    print("2. Remove Noise")
    print("3. Remove Background")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    image_path = '/home/fatemeh/Documents/image/images.jpg'  # Specify the path to your image
    image_processor = Image_Processor(image_path)  # Create an instance of ImageProcessor with the image path
    while True:
        choice = main_menu()  # Display the main menu and get the user's choice
        if choice == '1':
            image_processor.show_image()  # Display the original image
        elif choice == '2':
            image_processor.remove_noise()  # Remove noise from the image and display it
        elif choice == '3':
            image_processor.remove_background()  # Remove the background from the image and display it
        elif choice == '4':
            break  # Exit the program
        else:
            print("Invalid choice. Please try again.")  # Display an error message for invalid choices

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly