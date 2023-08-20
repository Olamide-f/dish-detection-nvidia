from jetcam.usb_camera import USBCamera
import ipywidgets
from IPython.display import display
from jetcam.utils import bgr8_to_jpeg


camera = USBCamera(width=224, height=224, capture_width=640, capture_height=480, capture_device=0)


image = camera.read()
print(camera.value.shape)
image = camera.value


image_widget = ipywidgets.Image(format='jpeg')
image_widget.value = bgr8_to_jpeg(image)

display(image_widget)


camera.running = True

def callback(change):
    new_image = change['new']
    # do some processing...

camera.observe(callback, names='value')