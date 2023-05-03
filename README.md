# metadata_date_extract_from_images

How it works
================

> main.py path_to_files [-e, --extension FILEEXTENSIONS [FILEEXTENSIONS ...]] [-d, --dir PROCESSED_FILES_DESTINATION]

For example: __python main.py /home/%username%/Desktop/images -e jpg, png__

By default - file destination is current folder, but it can be specified by -d or --dir flag.

For example: __python main.py /home/%username%/Desktop/images -e jpg, png -d /home/%username%/Desktop/formatted_images__


THIS IS A WIP
================

This is a quick script on the task I saw for upwork that I didn't manage to get, sadly.
However, I have found it very interesting and decided to make it a side project for portfolio.

TASK DESCRIPTION:
================
"I need a simple app that changes file name to have the creation date at the beginning files in a designated folder. For example, DJI_1.mp4 would be 202304011005_DJI_1.mp4. I should be able to designate the folder to perform the action on as well as the file type/extension."
As far as I understand - it is needed to be in format of year-month-day-hour-minute.

TODO:
================
~~* Add an ability to specify folder location.~~

~~* Add a check for files based on their extension according to the task description.~~
~~* re-do the script, cause it is not working as intended and very messy.~~
* Work on code clarity, it is a bit dirty, leave extra comments.
* Work on help section
* re-do readme




WHAT WAS DONE SO FAR:
================
* Basic program logic.
* Added the ability to specify folder location
* Added a check for file extension
