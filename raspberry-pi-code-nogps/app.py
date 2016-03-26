import datetime, picamera

FOLDER_TO_SAVE_IMAGES_TO = '/media/usb/nogps'

print 'Initializing camera...'
camera.hflip = True
camera = picamera.PiCamera()
camera.led = False

print 'Taking picture...'
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H%M')
filename = '{}/{}.{}'.format(FOLDER_TO_SAVE_IMAGES_TO, timestamp, 'jpg')
camera.capture(filename)
print '- Image saved as {}'.format(filename)
