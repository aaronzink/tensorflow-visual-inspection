# Screws data set

This data set simulates a visual quality inspection on an assembly line that installs four screws. The photos were taken with a cell phone placed about 15 cm away from a wooden block with four #2 Robertson wood screws in a square pattern. 

In some of the images one of the screws is missing. A missing screw is labeled as a hole. For every image four bounding boxes are defined and labeled as either a screw or a hole.

## Data Format
All images are 700 x 789 pixel JPGs.
There is variation between the images of up to: 
* 15 deg of rotation
* 100 pixels of translation


bounding_boxes = ((5,69,261,326),(305,69,561,326),(5,429,261,686),(325,429,581,686))

Every image uses the same bounding boxes in units of pixels (xmin, ymin, xmax, ymax). These boxes are drawn on the images in the ./bounding_boxes folder. eg.
<p align="center">
	<img src="https://raw.githubusercontent.com/aaronzink/tensorflow-visual-inspection/master/datasets/screws/bounding_boxes/95_1001.jpg" width="150">
</p>

File names are in the format 34_1001.jpg. 
34 is the image number, 1001 is a one hot encoding of the presence of screws from left to right, top to bottom. 1001 means there are two screws missing and two screws present eg.

<p align="center">
	<img src="https://raw.githubusercontent.com/aaronzink/tensorflow-visual-inspection/master/datasets/screws/train_val_set/100_1001.jpg"  width="150">
</p>