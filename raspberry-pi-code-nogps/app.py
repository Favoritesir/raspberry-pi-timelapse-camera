import picamera, datetime
camera = picamera.PiCamera()
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H%M')
filename = '{}/{}.{}'.format(FOLDER_TO_SAVE_IMAGES_TO, timestamp, 'jpg')
camera.capture(filename)
