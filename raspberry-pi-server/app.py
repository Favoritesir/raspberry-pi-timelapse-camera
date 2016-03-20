import os
from flask import Flask
from flask import render_template

FOLDER_TO_SAVE_IMAGES_TO = '/media/usbstick'

app = Flask(__name__)
app = Flask(static_folder=FOLDER_TO_SAVE_IMAGES_TO)

@app.route('/')
def hello():
    names = os.listdir(os.path.join(app.static_folder, 'imgs'))
    files = url_for('static', filename=os.path.join('imgs', names))
    return render_template('index.html', files=files)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
