import os
from PIL import Image

#This script converts all images in the current directory to processed versions with the same aspect ratio, in webp and jpg formats

def process_images():
    # Get the directory where the script is located, to create/get the processed folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder = script_dir
    # Get the processed folder
    output_folder = os.path.join(script_dir, 'processed')

    # Create the processed folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Function to resize the image while maintaining aspect ratio
    def resize_image_small(img, target_size=512):
        # Get the width and height of the image
        width, height = img.size
        # If the width is greater than the height, resize the width to the target size
        if width > height:
            if width > target_size:
                new_width = target_size
                new_height = int((target_size / width) * height)
            else:
                new_width, new_height = width, height
        # If the height is greater than the width, resize the height to the target size
        else:
            if height > target_size:
                new_height = target_size
                new_width = int((target_size / height) * width)
            else:
                new_width, new_height = width, height

        # Resize the image to the new width and height using the Lanczos filter and return the resized image
        return img.resize((new_width, new_height), Image.LANCZOS)
    # Function to resize the image while maintaining aspect ratio
    def resize_image_large(img, target_size=1280):
        # Get the width and height of the image
        width, height = img.size
        # If the width is greater than the height, resize the width to the target size
        if width > height:
            if width > target_size:
                new_width = target_size
                new_height = int((target_size / width) * height)
            else:
                new_width, new_height = width, height
        # If the height is greater than the width, resize the height to the target size
        else:
            if height > target_size:
                new_height = target_size
                new_width = int((target_size / height) * width)
            else:
                new_width, new_height = width, height

        # Resize the image to the new width and height using the Lanczos filter and return the resized image
        return img.resize((new_width, new_height), Image.LANCZOS)

    # Loop through all files in the current directory 
    for filename in os.listdir(input_folder):
        # Check if the file is an image, if so process it
        if filename.lower().endswith(('.jpg', '.jpeg', '.webp', '.png')):
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Resize the image using the resize_image function above
                resized_img_small = resize_image_small(img)
                resized_img_large = resize_image_large(img)

                # Define the new filenames and paths
                base_name, ext = os.path.splitext(filename)
                # new_jpg_path = os.path.join(output_folder, f"{base_name}.jpg")
                new_webp_path_small = os.path.join(output_folder, f"{base_name}.webp")
                new_webp_path_large = os.path.join(output_folder, f"{base_name}_large.webp")

                # Save a JPG version
                # resized_img.save(new_jpg_path, 'JPEG', quality=85)

                # Save a thumbnail and large size webp version
                resized_img_small.save(new_webp_path_small, 'WEBP', quality=90)
                resized_img_large.save(new_webp_path_large, 'WEBP', quality=90)

                print(f"Processed {filename} to {new_webp_path_small} and {new_webp_path_large}")

if __name__ == "__main__":
    process_images()
    input("Processing complete. Press Enter to exit.")
