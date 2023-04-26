import os
import sys
from pathlib import Path
import time
import datetime as dt
import shutil


def main():
    directory = Path.cwd() / "processed_files"
    directory.mkdir(exist_ok=True)


    def file_to_destination_dir(file):
        date = dt.datetime.strptime(time.ctime(os.path.getctime(file)), "%a %b %d %H:%M:%S %Y")
        output_file_name = f"{date.year}{date.month}{date.day}{date.hour}{date.minute}_{file.stem}{file.suffix}"
        file_location = directory / output_file_name
        shutil.copyfile(file, file_location)

    
    
    # test case for images...
    try:
        # path specification
        images = Path(sys.argv[1])
        for i in images.glob(f'*.*'):
            file_to_destination_dir(i)
    except IndexError:
        print("Please, specify the file name and/or extension.")
        sys.exit()
    except FileNotFoundError:
        print("File doesn't exist...")

if __name__ == "__main__":
    main()
