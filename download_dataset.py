import os
import urllib.request

# Define dataset URLs
flickr8k_images_url = "https://example.com/flickr8k_images.zip"
flickr8k_text_url = "https://example.com/flickr8k_text.zip"

# Define download directory
download_dir = "data"
os.makedirs(download_dir, exist_ok=True)

# Function to download a file
def download_file(url, output_path):
    print(f"Downloading {url}...")
    urllib.request.urlretrieve(url, output_path)
    print(f"Downloaded {output_path}.")

# Download datasets
image_zip_path = os.path.join(download_dir, "Flickr8k_Dataset.zip")
text_zip_path = os.path.join(download_dir, "Flickr8k_Text.zip")

if not os.path.exists(image_zip_path):
    download_file(flickr8k_images_url, image_zip_path)
else:
    print(f"{image_zip_path} already exists. Skipping download.")

if not os.path.exists(text_zip_path):
    download_file(flickr8k_text_url, text_zip_path)
else:
    print(f"{text_zip_path} already exists. Skipping download.")

print("Dataset download complete. Please unzip the files manually.")
