# Python Resume Parser
Headstarter Summer Fellowship Week 1 Project

## Main Objective

## Functionality
This program performs 3 main tasks:

1) A user should be able to upload one or more resumes.
2) Resumes should be parsed for specific info.
3) User should be able to use a dashboard to search for keywords like "javascript" and receive resumes that prioritize javascript experience.

## Running the app
IDE: Go into `app.py` and press the play button to run the program.
Commandline: Type the command `python app.py` to run the program.
In either case, the site will be displated at this url: http://127.0.0.1:5000/

## Uploading Files
Note: This implementation only works with .txt files.

To upload one or more files, simply click the "choose files" button to choose file(s) to upload. From there, click "submit" to upload the file(s). The uploaded files will be in the `uploads` folder, which is hidden from public view via the `.gitignore`.

### Tutorial and Source Code for File Upload in Flask
https://blog.devgenius.io/a-simple-way-to-build-flask-file-upload-1ccb9462bc2c

https://github.com/ngbala6/Flask-Uploadfiles/tree/master/flaskmultiplefileupload

## Searching Files for Keywords
To search for keywords, go to http://127.0.0.1:5000/search and type keywords (seperated by commas) into the provided field. From there, click "submit". This will display a list of resumes that contain ALL of the keywords you provided. The following information will be displayed:
- Link to local copy of the file
- Link to download file
- Date file was modified
- File size
If the user enters no keywords, then all the resumes will be displayed.

### File Display and Download via AutoIndex Source Code
https://github.com/russellelliott/AutoIndex-File-Display-and-Download

### Flask AutoIndex
https://github.com/general03/flask-autoindex

https://flask-autoindex.readthedocs.io/en/latest/

### Display Files in Subdirectory
https://www.pythonfixing.com/2022/06/fixed-how-to-list-files-of-directory.html

### Checking if string contains all elements from list
https://www.geeksforgeeks.org/python-test-if-string-contains-element-from-list/