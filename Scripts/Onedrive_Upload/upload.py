# upload.py
import os
import requests
from auth import get_access_token

ONE_DRIVE_API_ENDPOINT = "https://graph.microsoft.com/v1.0"
USER_ID = "your_user_id_here"  # Replace with the user ID or user email

# Function to upload files to OneDrive
def upload_file_to_onedrive(local_file_path, onedrive_folder_name):
    access_token = get_access_token()

    # Extracting the filename from the local filepath
    file_name = os.path.basename(local_file_path)

    # Make sure the folder exists -> If not, create one
    create_folder_url = f"{ONE_DRIVE_API_ENDPOINT}/users/{USER_ID}/drive/root:/{onedrive_folder_name}"
    create_folder_headers = {
        "Authorization": f"Bearer {access_token}",  # Bearer token authentication
        "Content-Type": "application/json"  # Create folder using JSON format
    }

    # Check if the folder already exists
    folder_response = requests.get(create_folder_url, headers=create_folder_headers)

    # If folder does not exist, create it
    if folder_response.status_code == 404:
        create_folder_data = {
            "name": onedrive_folder_name,
            "folder": {},
            "@microsoft.graph.conflictBehavior": "replace"
        }
        create_folder_response = requests.post(f"{ONE_DRIVE_API_ENDPOINT}/users/{USER_ID}/drive/root/children", headers=create_folder_headers, json=create_folder_data)

        if create_folder_response.status_code not in (200, 201):
            raise Exception(f"Failed to create folder '{onedrive_folder_name}'. Status code: {create_folder_response.status_code}, Error: {create_folder_response.text}")

    # Upload the actual file to OneDrive
    upload_url = f"{ONE_DRIVE_API_ENDPOINT}/users/{USER_ID}/drive/root:/{onedrive_folder_name}/{file_name}:/content"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/octet-stream"  # This will upload the file by binary stream
    }

    # Open the file and upload it
    with open(local_file_path, 'rb') as file_data:
        response = requests.put(upload_url, headers=headers, data=file_data)

    # Next, check if the file was uploaded successfully
    if response.status_code in (200, 201):
        print(f"File '{file_name}' uploaded successfully to folder '{onedrive_folder_name}'.")
    else:
        print(f"Failed to upload file. Status code: {response.status_code}, Error: {response.text}")
