import os
import shutil

def organize_files():
    # Specify the path to your desktop
    desktop_path = os.path.expanduser("~/Desktop")
    print('desktop path:', desktop_path)

    # Create folders if they don't exist
    folders = ['Images', 'Documents', 'Archives']
    for folder in folders:
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Get a list of all files on the desktop
    files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]

    for file in files:
        file_path = os.path.join(desktop_path, file)

        # Get the file extension
        _, file_extension = os.path.splitext(file)

        # Define categories based on file extensions
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        document_extensions = ['.doc', '.docx', '.pdf', '.txt', '.ppt', '.xls']
        archive_extensions = ['.zip', '.rar', '.tar', '.gz']

        # Move the file to the appropriate folder
        if file_extension.lower() in image_extensions:
            move_to_folder(file_path, 'Images')
        elif file_extension.lower() in document_extensions:
            move_to_folder(file_path, 'Documents')
        elif file_extension.lower() in archive_extensions:
            move_to_folder(file_path, 'Archives')

def move_to_folder(file_path, folder_name):
    desktop_path = os.path.expanduser("~/Desktop")
    destination_folder = os.path.join(desktop_path, folder_name)
    shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))

if __name__ == "__main__":
    organize_files()
    print("Files organized successfully!")
