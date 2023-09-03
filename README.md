# 🍽️ Project Dish Detection 🍽️

This project was made to help teens and adults alike who wish to be reminded when there are dishes in the sink. Through object detection with NVIDIA, user's can show their sink status to the camera and automatically get a message about whether or not there are dishes to be washed. From the lazy to productive and busy to time-free, this program is meant to aid people in their everyday lives.

![add image descrition here](direct image link here)

## The Algorithm
### OVERVIEW ~
To detect dishes well, I retrained NVDIA's basic DetectNet with images of various dishes, utensils, bottles, coffee cups and etc and uploaded that model into my program. From there, I coded the program to output images telling users to wash their dishes when the DetectNet finds any dishes, and depending on how many dishes there are detected a user may also receive an additional pop-up reminding them.

### Step 1: Importing Various Libraries
The first step to creating this algorithm was importing the libraries needed to ensure I could make my detection network and use the data it gave me to accomplish my program's purpose (outputting messages about dishes). I imported jetson_inference, jetson_utils, argparse, sys, and PySimpleGUI: all various libraries which help to initialize my Detect Network (the network which makes the detection of the dishes) in a way conducive to my program purpose. For instance, jetson_utils helps to initialize the camera feed (so that the program can take into account what users' cameras are showing) and add text onto the screen, while PySimpleGUI allows for pop-up messages to be shown after most of the program has run. 
[Image of my import statements](https://imgur.com/Y3MzzpR)

### Step 2: Creating the DetectNet Network
This part was simple, I loaded my re-trained detection network and the arguments necessary to making a DetectNet network based on a "custom"/re-trained model. Said arguments included: 
 model -- the name of my re-trained model (named ssd-mobilenet in this case)
 labels -- the different labels I was using to re-train my model (eg. Fork, Dishwasher, Bottle, Coffee Cup)
 output_cvg -- what I wanted the outputted confidence layer to be named (in my case score)
 input_blob -- what I wanted to be the first input layer of the model
 output_bbox -- the name I wanted to use for the bounding boxes layer (in my case boxes)
Some of this arguments were made with the purpose of simplifying my access to the data outputted by the detection model. For instance, I could easily refer to "boxes" when trying to gather the bounding boxes layer as opposed to using a convoluated path of code. Simple notes like this, made it easier to use the data recieved by my network for outputting messages when dishes were detected in the sink.

### Step 3: Capturing the Live Camera Feed and Basing Actions Off of It
On line 40, I told the program where I was getting my camera feed from, so it could use it when applying the detection network on the image. On line 41 however, I was letting the program know how to output the visuals it was showing (like the live feed with the boxes showing each detection and the program's confidence in it).

[Image of the code which outputs certain text depending on the detections gathered by my network](https://imgur.com/imRDs6c)
From there, I ran a while loop which goes on for every second the live feed is still going. It states that will the live feed is going, it wants to capture an image of the current screen and run the DetectNet on the image -- looking for each object and attempting to categorize what class its in. It will then save these detections, output the nunber of detections made to the console, and run a for loop which determines if the network saw and categorized any dishes, how many dishes it saw, and output certain text based off that. This step is very important as it is what tells/alerts the user of there being dishes in their sink.
--> If there are no dishes detected the program will output onto the screen that there are no dishes, whereas if there are ANY dishes, the program will immediately tell the user that they have dirty dishes to clean.
--> And if there are more than 2 dishes detected in the sink, users will further be prompted to clean up their sink with another pop-up reminder telling them to GO WASH THEIR DISHES!!

### Step 4: Output an Image Depending on What the Network Detected and Stopping the Program
All this does, is update the screen users are seeing after the program has made its detections and run its output statements and continue repeating step 3 until the user ends the program.

### That is it for the Program!!
I hope this helped you better understand what it is my Dish Detection Program Does


## Running this project
1. Install then import jetson_inference, jetson_utils, argparse, sys, PySimpleGUI, and (videoSource, videoOutput, cudaFont) -- from jetson_utils
2. Download my re-trained detection model .onnx -- "ssd-mobilenet.onnx"
3. Download my labels .txt -- "labels.txt"
4. Determine your camera source and update [input = videoSource("/dev/video0")] accordingly (/dev/video0 is for V4L2 cameras)
5. Likewise update [videoOutput("display://0")] accordingly depending on what you want your video output to be
6. Run the program


   
1. Add steps for running this project.
2. Make sure to include any required libraries that need to be installed for your project to run.

[View a video explanation here (PART 1)]([CODE ONLY DESCRIPTION](https://youtu.be/zc5OQhWhaa4))
[View a video explanation here (PART 2)]([LIVE FOOTAGE DESCRIPTION](https://youtu.be/Vcg7ZiEg6eY))

