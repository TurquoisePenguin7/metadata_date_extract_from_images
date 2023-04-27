import os
import sys
from pathlib import Path
import time
import datetime as dt
import shutil
import argparse


def main():

    parser = argparse.ArgumentParser(
        description="A quick script to add date from the metadata of the file."
    )
    parser.add_argument('path_to_files', help="File path to the files")
    parser.add_argument('-fe', '--fileextensions',
                    action="extend", nargs="+", dest='fileextensions',
                    help="Supplies file extension to the script, supports multiple.")
    parser.add_argument('-d', '--dir', dest="processed_files", help="processed files destination", default=Path.cwd() / "processed_files")

    args = parser.parse_args()

    def file_to_destination_dir(file, processed_dir=None):
        date = dt.datetime.strptime(time.ctime(os.path.getctime(file)), "%a %b %d %H:%M:%S %Y")
        output_file_name = f"{date.year}{date.month}{date.day}{date.hour}{date.minute}_{file.stem}{file.suffix}"
        if processed_dir is None:
            default_directory = Path.cwd() / "processed_files"
            default_directory.mkdir(exist_ok=True)
            file_location = default_directory / output_file_name
            shutil.copyfile(file, file_location)
        else:
            file_location = processed_dir / output_file_name
            shutil.copyfile(file, file_location)
    

    try:
        # path specification
        files = Path(args.path_to_files)
        extensions = args.fileextensions
        processed_files = Path(args.processed_files)
        for file in files.glob(f'*.*'):
            # checks if value is in pathlib object, otherwise do nothing. 
            if file.suffix.strip('.') in extensions:
                file_to_destination_dir(file, processed_files)
                print(f"Working on {file.name}, sending it to {processed_files}")
    except IndexError:
        print("Please, specify the file name and/or extension.")
        sys.exit(1)
    except FileNotFoundError:
        print("File doesn't exist...")
        sys.exit(1)

if __name__ == "__main__":
    main()
