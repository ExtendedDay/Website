import os
from bs4 import BeautifulSoup

# This script parses the names of all images in the processed directory and updates the html file accordingly

def update_and_beautify_gallery_html():
    # Define the directory and HTML file paths
    directory_path = 'Gallery/Images/processed'
    html_file_path = 'Gallery/Gallery.html'
    
    # Initialize BeautifulSoup object with the HTML file
    with open(html_file_path, 'r+') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        # Clear existing children of the masonry-gallery div
        masonry_div = soup.find('div', class_='masonry-gallery')
        if masonry_div:
            masonry_div.clear()
        
        # List all.webp files in the directory
        image_files = [f for f in os.listdir(directory_path) if f.endswith('.jpg')]
        
        # Append the grid-sizer div to the masonry-gallery div
        masonry_div.append(BeautifulSoup('<div class="grid-sizer"></div>', 'html.parser'))

        # Generate img tags for each image and append to the masonry-gallery div
        for image_file in image_files:
            img_tag = '<img alt="" src="Images/processed/' + image_file + '" class="gallery-item">'
            masonry_div.append(BeautifulSoup(img_tag, 'html.parser'))
        
        # Move the file pointer to the beginning of the file before writing
        file.seek(0)
        
        # Beautify the HTML content
        pretty_html = str(soup.prettify())
        
        # Write the updated and beautified HTML back to the file
        file.write(pretty_html)
        
        # Truncate the file to remove any remaining content after the write operation
        file.truncate()

if __name__ == '__main__':
    update_and_beautify_gallery_html()
    print("HTML updated and beautified successfully.")
