# etl.py
import os
from upload import upload_file_to_onedrive

# Main function for ETL upload Operation
def etl_upload(download_folder_path):
    for root, _, files in os.walk(download_folder_path):
        for file in files:
            # Derive OneDrive folder name from the downloaded folder name
            onedrive_folder_name = os.path.basename(root)
            local_file_path = os.path.join(root, file)
            # Upload to OneDrive
            upload_file_to_onedrive(local_file_path, onedrive_folder_name)
