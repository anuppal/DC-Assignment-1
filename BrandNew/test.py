import os

def split_filename_from_path(filepath):
    # Use os.path.basename to get the filename from the path
    filename = os.path.basename(filepath)
    return filename

if __name__ == "__main__":
    path = "Data/abc.txt"  # Replace with the actual path
    filename = split_filename_from_path(path)
    print(f"Filename: {filename}")
