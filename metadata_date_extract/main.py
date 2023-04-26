import os
import sys
from pathlib import Path
import time
import datetime as dt
import shutil


def main():
    directory = Path.cwd() / "processed_files"
    directory.mkdir(exist_ok=True)

    def to_destination_dir(file, path=None):
        date = dt.datetime.strptime(time.ctime(os.path.getctime(file)), "%a %b %d %H:%M:%S %Y")
        output_file = f"{file.stem}_{date.month}_{date.day}_{date.year}{file.suffix}"
        file_location = directory / output_file
        shutil.copyfile(file, file_location)
    
    images = Path.cwd() / "images"
    for i in images.glob('*.*'):
        to_destination_dir(i)

if __name__ == "__main__":
    main()
