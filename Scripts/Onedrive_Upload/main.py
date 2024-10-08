# main.py
from etl import etl_upload

if __name__ == "__main__":
    download_folder_path = r"C:\path\to\your\download_folder"  # Replace with the path where extracted profiles are stored
    etl_upload(download_folder_path)
