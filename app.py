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

#Searching files for specific keywords
@app.route('/search', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.lower()
    return processed_text


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=False,threaded=True)