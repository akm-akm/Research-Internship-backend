import os
from flask import Flask, request, send_file, send_from_directory
import uuid
import shutil
from flask_cors import CORS, cross_origin
from object_detection import detect_objects

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


UPLOAD_FOLDER = './temp'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['GET', 'POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'there is no file in form!'
        file1 = request.files['file']
        rand = uuid.uuid4()
        try:
            shutil.rmtree('./runs')
            print("////////////////Folder deleted successfully")
        except OSError as e:
            print("///////////////////////////////////////////////Error: %s : %s" % ('runs', e.strerror))
        name = str(rand) + file1.filename
        path = os.path.join(app.config['UPLOAD_FOLDER'], name)
        file1.save(path)
        detected = detect_objects(path)
        if detected:
            return send_file(os.getcwd() + detected + '/' + name)
            # Use the shutil module to delete the folder and all its contents

        return 501
    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''


if __name__ == '__main__':
    app.run()