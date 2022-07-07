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
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


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

#Searching files for specific keywords
@app.route('/search', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.lower() #text from the input converted to lowercase
    return processed_text

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

try:
    os.makedirs(app.config['UPLOAD_FOLDER'])
except:
    pass

def get_files(target):
    for file in os.listdir(target):
        path = os.path.join(target, file)
        if os.path.isfile(path):
            yield (
                file,
                datetime.utcfromtimestamp(os.path.getmtime(path)),
                os.path.getsize(path)
            )

#Viewing the files in the directory
@app.route('/files')
def files():
    files = get_files(app.config['UPLOAD_FOLDER'])
    return render_template('files.html', **locals(), variable = UPLOAD_FOLDER)

@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=False,threaded=True)