
import os
import shutil
from pathlib import Path

def download_folder():
    home_name = Path.home()
    downloads = home_name / "Downloads"
    
    return str(downloads)

target_folder = download_folder()

subfolders = ["Images", "Documents", "Videos", "Audio", "Archives", "Misc"]

for folder in subfolders:
    folder_path = os.path.join(target_folder, folder)
    os.makedirs(folder_path, exist_ok=True)

extension_to_folder = {
    
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
 
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
 
    ".mp4": "Videos",
    ".mov": "Videos",
    
    ".mp3": "Audio",
    ".wav": "Audio",

    ".zip": "Archives",
    ".rar": "Archives",
}

for filename in os.listdir(target_folder):
    file_path = os.path.join(target_folder, filename)
    
    if os.path.isdir(file_path):
        continue
    
    _, extension = os.path.splitext(filename)
    extension = extension.lower() 

    
    target_subfolder = extension_to_folder.get(extension, "Misc")
    target_path = os.path.join(target_folder, target_subfolder, filename)

    
    try:
        shutil.move(file_path, target_path)
        print(f"Moved: {filename} → {target_subfolder}/")
    except Exception as e:
        print(f"Error moving {filename}: {e}")