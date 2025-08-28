# File Read & Write Challenge ✍️

def modify_content(text):
    """Simple modification: convert text to uppercase"""
    return text.upper()

try:
    # Read from input file
    with open("input.txt", "r") as file:
        content = file.read()

    # Modify content
    new_content = modify_content(content)

    # Write to new file
    with open("output.txt", "w") as file:
        file.write(new_content)

    print("File has been read, modified, and saved to output.txt ✅")

except FileNotFoundError:
    print("Error: input.txt not found. Please make sure the file exists.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
