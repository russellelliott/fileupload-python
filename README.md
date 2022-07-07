# Python Resume Parser
Headstarter Summer Fellowship Week 1 Project

## Functionality
This program performs 3 main tasks

1) A user should be able to upload one or more resumes.
2) Resumes should be parsed for specific info.
3) User should be able to use a dashboard to search for keywords like "javascript" and receive resumes that prioritize javascript experience.

## Tutorial and Source Code for File Upload in Flask
https://blog.devgenius.io/a-simple-way-to-build-flask-file-upload-1ccb9462bc2c
https://github.com/ngbala6/Flask-Uploadfiles/tree/master/flaskmultiplefileupload

## Running the app
IDE: Go into `app.py` and press the play button to run the program.
Commandline: Type the command `python app.py` to run the program.
In either case, the site will be displated at this url: http://127.0.0.1:5000/

## Uploading Files
To upload one or more files, simply click the "choose files" button to choose file(s) to upload. From there, click "submit" to upload the file(s). The uploaded files will be in the `uploads` folder, which is hidden from public view via the `.gitignore`.