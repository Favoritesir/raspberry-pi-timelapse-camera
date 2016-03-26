import picamera, datetime

FOLDER_TO_SAVE_IMAGES_TO = '/media/usb'


camera = picamera.PiCamera()

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H%M')
filename = '{}/{}.{}'.format(FOLDER_TO_SAVE_IMAGES_TO, timestamp, 'jpg')
camera.capture(filename)
