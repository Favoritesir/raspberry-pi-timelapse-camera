import os, datetime
from flask import Flask, render_template, send_from_directory, request

FOLDER_TO_SAVE_IMAGES_TO = '/media/usb'
#FOLDER_TO_SAVE_IMAGES_TO = '/Users/manoj/Downloads/usbstick'

app = Flask(__name__)

@app.route('/')
def hello():
    files = os.listdir(FOLDER_TO_SAVE_IMAGES_TO)
    files = sorted(files, reverse=True)
    images = []
    for image in files:30:
        if '.jpg' in image:
            images.append('/image/{}'.format(image))
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', images=images, timestamp=timestamp)

@app.route('/image/<path:filename>')
def base_static(filename):
    return send_from_directory(FOLDER_TO_SAVE_IMAGES_TO, filename)

@app.route('/image/delete/', methods=['POST'])
def delete_image():
    image = request.form["image"].split("/")[2]
    move_from = FOLDER_TO_SAVE_IMAGES_TO + "/" + image
    move_to = FOLDER_TO_SAVE_IMAGES_TO + "/deleted/" + image
    os.rename(move_from, move_to)
    return "Deleting img: {}".format(image)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
