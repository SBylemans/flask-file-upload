from flask import Flask, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/music', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      files = request.files.getlist('file')
      for f in files:
          f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True)
