# Program to organise random files into folders based on the file extension
# Date: 12 Sept 2021

import os
from pathlib import Path

# Dictionary with folder names as key and file extensions as values
foldernames = {
    "Images" : [".png", ".jpeg", ".jpg", ".svg", ".gif"],
    "Videos" : [".mp4", ".mpeg", ".mpg", ".mkv", ".mov"],
    "Audio" : [".mp3", ".wav", ".wma"],
    "PDF" : [".pdf"],
    "Zip Files" : [".zip", ".rar", ".tar", ".iso", ".gz"],
    "Documents" : [".xls", ".xslx", ".doc", ".docx", ".ppt", ".pptx", ".md", ".csv", ".json"],
}

# Map file formats to respective folders
file_formatlist = {
    file_format : folder 
    for folder, file_formats in foldernames.items()
    for file_format in file_formats
}

def organise():
    for entry in os.scandir():
        if entry.is_dir():
            continue

        file_path =  Path(entry)
        file_format = file_path.suffix.lower()

        if file_format in file_formatlist:
            folder_path = Path(file_formatlist[file_format])
        # When there is a file format that is not specified in the dictionary
        else:
            folder_path = Path('Others')

        folder_path.mkdir(exist_ok=True)
        file_path.rename(folder_path.joinpath(file_path))

if __name__ == '__main__':
    organise()
