import jetson_inference
import jetson_utils

import argparse
import sys

from jetson_utils import videoSource, videoOutput, cudaFont

# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.")

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)


# load the object detection network
net = jetson_inference.detectNet(
    model="ssd-mobilenet",
    labels="labels.txt",
    input_blob="input_0",
    output_cvg="scores",
    output_bbox="boxes",
    threshold=0.5
)



# create video sources & outputs
input = videoSource("/dev/video0")
output = videoOutput("display://0")

font = cudaFont()

###
# process frames until the user exits
while True:
	###### sg.popup('Basic Pop-up', 'And it can show multiline text and variables')
	# capture the next image
	img = input.Capture()

	# detect objects in the image (with overlay)
	detections = net.Detect(img, overlay=opt.overlay)

	# print the detections
	print("detected {:d} objects in image".format(len(detections)))

	dish_count = 0
	for detection in detections:
		#print(detection)
		label = net.GetClassLabel(detection.ClassID)
		print(label)
		if label == "bottle" or label == "bottle opener" or label == "bowl" or label == "coffee cup" or label == "countertop" or label == "dishwasher" or label == "drink" or label == "drinking straw":
			dish_count += 1
		elif label == "fork" or label == "juice" or label == "kitchen appliance" or label == "kitchen knife" or label == "kitchen utensil" or label == "knife" or label == "measuring cup" or label == "mixing bowl":
			dish_count += 1
		elif label == "mug" or label == "soap dispenser" or label == "wine glass" or label=="cup" or label=="spoon":
			dish_count += 1
		

		if label == "bottle" or label == "bottle opener" or label == "bowl" or label == "coffee cup" or label == "countertop" or label == "dishwasher" or label == "drink" or label == "drinking straw":
			font.OverlayText(img, text="Uh oh! There are {:d} dishes in the sink. Let's clean them up quickly!!".format(dish_count), 
            	x=200, y=100,
            	color=font.White, background=font.Blue)
		elif label == "fork" or label == "juice" or label == "kitchen appliance" or label == "kitchen knife" or label == "kitchen utensil" or label == "knife" or label == "measuring cup" or label == "mixing bowl":
			font.OverlayText(img, text="Uh oh! There are {:d} dishes in the sink. Let's clean them up quickly!!".format(dish_count), 
            	x=200, y=100,
            	color=font.White, background=font.Blue)
		elif label == "mug" or label == "soap dispenser" or label == "wine glass" or label=="cup" or label=="spoon":
			font.OverlayText(img, text="Uh oh! There are {:d} dishes in the sink. Let's clean them up quickly!!".format(dish_count), 
            	x=200, y=100,
            	color=font.White, background=font.Blue)
		else:
			font.OverlayText(img, text="Lucky you! There are no dishes in the sink.", 
            	x=200, y=100,
            	color=font.White, background=font.Black)
	if len(detection) == 0:
		font.OverlayText(img, text="Lucky you! There are no dishes in the sink.", 
    		x=200, y=100,
        	color=font.White, background=font.Black)
	
	dish_count = 0
	###############

	# render the image
	output.Render(img)

	# update the title bar
	output.SetStatus("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))

	# print out performance info
	net.PrintProfilerTimes()

	# exit on input/output EOS
	if not input.IsStreaming() or not output.IsStreaming():
		break

