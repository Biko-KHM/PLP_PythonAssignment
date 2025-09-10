Ubuntu Image Fetcher
A Python script that fetches images from URLs, inspired by Ubuntu's "I am because we are" philosophy.
Features

Downloads images from single or comma-separated URLs
Saves images to Fetched_Images directory
Prevents duplicates using SHA-256 hashing
Validates content type and size for safety
Handles errors gracefully

Requirements

Python 3.6+
requests library (pip install requests)

Usage

Clone the repo:git clone https://github.com/Biko-KHM/Ubuntu_Requests.git
cd Ubuntu_Requests


Install dependencies:pip install requests


Run the script:python ubuntu_image_fetcher.py


Enter image URL(s):Enter image URL(s): https://example.com/image.jpg
✓ Successfully fetched: image.jpg
✓ Image saved to Fetched_Images/image.jpg



Ubuntu Principles

Community: Connects to web resources
Respect: Safe downloads with error handling
Sharing: Organizes images for easy access
Practicality: Useful image collection tool

License
MIT License