import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

app=Flask(__name__)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['txt']) #only text files work for this implementation


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Render page for uploading files
@app.route('/')
def upload_form():
    return render_template('upload.html')

#Uploading files
@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/')

#Render search page
@app.route('/search')
def searchpage():
    return render_template('search.html')

from flask_autoindex import AutoIndex
from flask import send_from_directory

'''#Searching files for specific keywords
@app.route('/search', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.lower() #text from the input converted to lowercase
    return processed_text'''

from flask_moment import Moment
from datetime import datetime
import os

def byte_units(value, units=-1):
    UNITS=('Bytes', 'KB', 'MB', 'GB', 'TB', 'EB', 'ZB', 'YB')
    i=1
    value /= 1000.0
    while value > 1000 and (units == -1 or i < units) and i+1 < len(UNITS):
        value /= 1000.0
        i += 1
    return f'{round(value,3):.3f} {UNITS[i]}'

app.jinja_env.filters.update(byte_units = byte_units)
moment = Moment(app)

#Make the upload folder if it doesn't exist already
try:
    os.makedirs(app.config['UPLOAD_FOLDER'])
except:
    pass

#Check the file to see if it contains all the keywords specified
def filter(file, words):
    f = open(file, "r") #read the file
    if words == []:
        return True #if wordlist is empty, return True; this will display all the resumes, as the user isn't using keywords, implying they want to see all the resumes.
    string = f.read().lower() #read file, convert to lowercase
    res = [ele for ele in words if(ele in string)] #test if all elements in the words list are in the string
    return res #returns true if all keywords are in resume, false otherwise

def get_files(target, words):
    for file in os.listdir(target):
        path = os.path.join(target, file) #path to the file
        if os.path.isfile(path) and filter(path, words): #check if the path is valid and the file contains all the keywords
            #yield statement to add file to list displayed
            yield (
                file,
                datetime.utcfromtimestamp(os.path.getmtime(path)),
                os.path.getsize(path)
            )

#Viewing the files in the directory
#This should take the data from search

#Searching files for specific keywords
@app.route('/search', methods=['POST'])
def my_form_post():
    text = request.form['text']
    keywords = text.lower().split() #text from the input converted to lowercase
    files = get_files(app.config['UPLOAD_FOLDER'], keywords) #get files from the uploads folder that contain the keywords
    return render_template('files.html', **locals(), variable = UPLOAD_FOLDER) #render the list of files, as well as date they were modified, and their size

#Dowload file from list
@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=False,threaded=True)