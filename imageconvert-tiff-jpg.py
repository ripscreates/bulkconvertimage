import os
import subprocess
from pathlib import Path

def convert_tiff_to_jpg(source_folder, target_folder):
    # Create the target folder if it doesn't exist
    Path(target_folder).mkdir(parents=True, exist_ok=True)

    # Iterate through each file in the source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.tiff') or filename.lower().endswith('.tif'):
            source_file = os.path.join(source_folder, filename)
            target_file = os.path.join(target_folder, f"{Path(filename).stem}.jpg")
            
            # Convert the file using ImageMagick's convert command
            subprocess.run(['convert', source_file, target_file], check=True)
            print(f"Converted {source_file} to {target_file}")

if __name__ == "__main__":
    source_folder = input("Please provide the path to the folder containing TIFF files: ")
    target_folder = input("Please provide the path to the folder where JPG files should be saved: ")

    if not os.path.isdir(source_folder):
        print(f"The provided source folder path '{source_folder}' is not valid.")
    elif not os.path.isdir(target_folder):
        print(f"The provided target folder path '{target_folder}' is not valid.")
    else:
        convert_tiff_to_jpg(source_folder, target_folder)
