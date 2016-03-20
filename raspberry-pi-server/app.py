import os
from flask import Flask
from flask import url_for, render_template

FOLDER_TO_SAVE_IMAGES_TO = '/media/usbstick'

app = Flask(
    __name__,
    static_folder=FOLDER_TO_SAVE_IMAGES_TO
)

@app.route('/')
def hello():
    files = os.listdir(app.static_folder)
    images = []
    for image in files:
        images.append(url_for('static', filename=image))
    return render_template('index.html', files=images)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
