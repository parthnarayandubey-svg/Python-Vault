import os
import shutil


def start():
    print("========== FILE ORGANIZER ==========")

    folder_path = input("Enter folder path: ")

    if not os.path.exists(folder_path):
        print("Folder not found!")
        return

    files = os.listdir(folder_path)

    file_types = {
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",

        ".mp3": "Music",
        ".wav": "Music",

        ".mp4": "Videos",
        ".mkv": "Videos",

        ".pdf": "PDFs",

        ".doc": "Documents",
        ".docx": "Documents",
        ".txt": "Documents",

        ".py": "Python Files"
    }

    for file in files:

        source = os.path.join(folder_path, file)

        if not os.path.isfile(source):
            continue

        extension = os.path.splitext(file)[1].lower()

        if extension in file_types:

            destination_folder = os.path.join(folder_path, file_types[extension])

            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)

            destination = os.path.join(destination_folder, file)

            shutil.move(source, destination)

            print(f"{file} moved to {file_types[extension]}")

        else:
            print(f"{file} skipped")