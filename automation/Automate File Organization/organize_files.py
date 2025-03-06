

import os
import shutil

# Define the folder to organize
folder_path = "C:/Users/User/Desktop/Pyhton_series/automation/Automate File Organization/FilesToOrganize"

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Loop through each file
for file in files:
    # Get the file extension
    file_extension = os.path.splitext(file)[1].lower()

    # Create a folder for the extension if it doesn't exist
    if file_extension:
        destination_folder = os.path.join(folder_path, file_extension[1:])  # Remove the dot from the extension
        os.makedirs(destination_folder, exist_ok=True)

        # Move the file to the corresponding folder
        shutil.move(os.path.join(folder_path, file), os.path.join(destination_folder, file))

print("Files organized successfully!")
