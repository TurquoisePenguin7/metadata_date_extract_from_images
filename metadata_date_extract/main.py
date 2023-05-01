import os
import sys
from pathlib import Path
import time
import datetime as dt
import shutil
import argparse


def main():
    """A CLI parser to extract metadata."""

    parser = argparse.ArgumentParser(
        description="A quick script to add date from the metadata of the file."
    )
    parser.add_argument('path_to_files', help="File path to the files")
    parser.add_argument('-fe', '--fileextensions',
                    action="extend", nargs="+", dest='fileextensions',
                    help="Supplies file extension to the script, supports multiple.")
    parser.add_argument('-d', '--dir', dest="processed_files", help="processed files destination", default=Path.cwd() / "processed_files")

    args = parser.parse_args()

    def file_to_destination_dir(file: Path, processed_dir=None) -> None:
        """This function retreives the metadata creation time from the file.
           It then makes a check on the directory and moves the files accordingly."""
        date = dt.datetime.strptime(time.ctime(os.path.getctime(file)), "%a %b %d %H:%M:%S %Y")
        output_file_name = f"{date.year}{date.month}{date.day}{date.hour}{date.minute}_{file.stem}{file.suffix}"
        
        # A check on directories
        if processed_dir is None:
            default_directory = Path.cwd() / "processed_files"
            default_directory.mkdir(exist_ok=True)
            file_location = default_directory / output_file_name
            shutil.copyfile(file, file_location)
        else:
            file_location = processed_dir / output_file_name
            shutil.copyfile(file, file_location)
    

    try:
        # Setting up the path for the file location that was specified, as well as extensions and a new folder for processed files.
        files = Path(args.path_to_files)
        extensions = args.fileextensions
        processed_files = Path(args.processed_files)

        for file in files.glob(f'*.*'):
            # checks if extension is in the extensions, otherwise do nothing.
            # We strip the code in order to get the proper value from the suffix from the Path object
            # Since it returns ".jpg", for example, we just remove the dot and get the exact name instead.
            if file.suffix.strip('.') in extensions:
                file_to_destination_dir(file, processed_files)
                print(f"Working on {file.name}, sending it to {processed_files}")
    # Error handling, when file or extention is not specified
    except IndexError:
        print("Please, specify the file name and/or extension.")
        sys.exit(1)
    # If file doesn't exist
    except FileNotFoundError:
        print("File doesn't exist...")
        sys.exit(1)

if __name__ == "__main__":
    main()
