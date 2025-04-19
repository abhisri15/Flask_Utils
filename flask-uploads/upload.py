from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES, UploadNotAllowed, TEXT

app = Flask(__name__)

# Configure the upload set
photos = UploadSet('photos', IMAGES+TEXT+('py','cpp''java','html','css','js'))
docs = UploadSet('docs', TEXT)

app.config['UPLOADED_PHOTOS_DEST'] = 'pictures'
app.config['UPLOADED_PHOTOS_ALLOW'] = ['jpg', 'jpeg', 'png', 'gif']
app.config['UPLOADED_PHOTOS_DENY'] = ['exe', 'bat', 'sh']
app.config['UPLOADS_DEFAULT_DEST'] = 'other '

configure_uploads(app,(photos,docs))

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST' and 'thefile' in request.files:

        try:
            # Save the uploaded file
            doc_filename = docs.save(request.files['thefile'])
            return '<h1>'+docs.url(doc_filename)+'</h1>'

        except UploadNotAllowed:
            return '<h1>File type not allowed</h1>'

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)