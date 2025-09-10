import requests
import os
from urllib.parse import urlparse
import hashlib
from datetime import datetime

def get_file_hash(filepath):
    """Calculate SHA-256 hash of a file to check for duplicates."""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def is_valid_image_content_type(content_type):
    """Check if the content type is a valid image type."""
    valid_types = ['image/jpeg', 'image/png', 'image/gif', 'image/bmp']
    return content_type in valid_types

def generate_unique_filename(filename, directory):
    """Generate a unique filename by appending timestamp if needed."""
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"{base}_{timestamp}_{counter}{ext}"
        counter += 1
    return new_filename

def fetch_and_save_image(url, directory="Fetched_Images"):
    """Fetch and save an image from a URL, with safety checks."""
    try:
        # Send HEAD request to check headers first
        head_response = requests.head(url, timeout=5, allow_redirects=True)
        head_response.raise_for_status()

        # Check Content-Type
        content_type = head_response.headers.get('content-type', '').lower()
        if not is_valid_image_content_type(content_type):
            print(f"✗ Invalid content type for {url}: {content_type}")
            return False

        # Check Content-Length (avoid very large files, e.g., >10MB)
        content_length = int(head_response.headers.get('content-length', 0))
        if content_length > 10 * 1024 * 1024:
            print(f"✗ File too large for {url}: {content_length} bytes")
            return False

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename or not os.path.splitext(filename)[1]:
            filename = f"downloaded_image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

        # Generate unique filename to avoid overwriting
        filename = generate_unique_filename(filename, directory)

        filepath = os.path.join(directory, filename)

        # Calculate hash of the downloaded content
        content_hash = hashlib.sha256(response.content).hexdigest()

        # Check for duplicates by comparing hashes of existing files
        for existing_file in os.listdir(directory):
            existing_path = os.path.join(directory, existing_file)
            if os.path.isfile(existing_path):
                if get_file_hash(existing_path) == content_hash:
                    print(f"✗ Duplicate image detected for {url}, skipping save.")
                    return False

        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
        return False
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")
        return False

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)
    
    # Get URLs from user (comma-separated or single URL)
    urls_input = input("Please enter image URL(s) (comma-separated for multiple): ")
    urls = [url.strip() for url in urls_input.split(',')]
    
    success_count = 0
    for url in urls:
        if url:
            if fetch_and_save_image(url):
                success_count += 1
    
    print(f"\nConnection strengthened. Community enriched. ({success_count}/{len(urls)} images fetched)")

if __name__ == "__main__":
    main()