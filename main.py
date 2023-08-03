from PIL import Image
import os

def resize_image(image_path, output_filename, size=(32, 32)): #change this value to get desired resolutions
    try:
        # Open the image
        image = Image.open(image_path)

        # Resize the image
        resized_image = image.resize(size)

        # Get the current working directory
        current_directory = os.getcwd()

        # Save the resized image to the current directory with the specified filename
        output_path = os.path.join(current_directory, output_filename)
        resized_image.save(output_path)

        print(f"Image resized to {size[0]}x{size[1]} and saved at {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
input_image_path = "IMAGE NAME" #change the value to use different images
output_image_filename = "resized_image.png" #change this to get the desired output image name
resize_image(input_image_path, output_image_filename)
