# Create zip file at location given by user
import os
import zipfile
def create_zip_folder(folder_path, zip_filename):
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return
    if os.path.exists(zip_filename):
        print(f"Warning: File '{zip_filename}' already exists. Overwriting...")
        try:
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for foldername, subfolders, filenames in os.walk(folder_path):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        zipf.write(file_path, os.path.relpath(file_path, folder_path))
            print(f"ZIP file '{zip_filename}' created successfully.")
        except Exception as e:
            print(f"Error: Failed to create ZIP file '{zip_filename}'.")
            print(f"Reason: {e}")

folder_path = r"C:\Users\CSD 8\4th_sem_python"
zip_filename = r"C:\Users\CSD 8\4th_sem_python\zipped.zip"
create_zip_folder(folder_path, zip_filename)
