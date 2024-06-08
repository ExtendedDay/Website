import os
from PIL import Image

#This script converts all images in the current directory to processed versions with the same aspect ratio, in webp and jpg formats

def process_images():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder = script_dir
    output_folder = os.path.join(script_dir, 'processed')

    # Create the processed folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Function to resize the image maintaining aspect ratio
    def resize_image(img, target_size=1024):
        width, height = img.size
        if width > height:
            if width > target_size:
                new_width = target_size
                new_height = int((target_size / width) * height)
            else:
                new_width, new_height = width, height
        else:
            if height > target_size:
                new_height = target_size
                new_width = int((target_size / height) * width)
            else:
                new_width, new_height = width, height
        return img.resize((new_width, new_height), Image.LANCZOS)

    # Loop through all files in the current directory
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            # Open an image file
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Resize the image
                resized_img = resize_image(img)

                # Define the new filename and path
                base_name, ext = os.path.splitext(filename)
                new_jpg_path = os.path.join(output_folder, f"{base_name}.jpg")
                new_webp_path = os.path.join(output_folder, f"{base_name}.webp")

                # Save the image with reduced quality
                resized_img.save(new_jpg_path, 'JPEG', quality=85)  # Adjust quality as needed

                # Save a WebP version
                resized_img.save(new_webp_path, 'WEBP', quality=85)  # Adjust quality as needed

                print(f"Processed {filename} to {new_jpg_path} and {new_webp_path}")

if __name__ == "__main__":
    process_images()
    input("Processing complete. Press Enter to exit.")
