import os
import json

def generate_image_list(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter for image files (adjust the extensions as needed)
    image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    # Generate JSON data
    image_data = {"images": [{"filename": f, "path": os.path.join(directory, f)} for f in image_files]}
    
    return image_data

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
directory_path = 'Gallery/Images'
json_filename = directory_path + '/image_list.json'

# Generate the image list
image_list = generate_image_list(directory_path)

# Save the JSON data to a file
save_to_json(image_list, json_filename)

print(f"JSON saved to {json_filename}")
