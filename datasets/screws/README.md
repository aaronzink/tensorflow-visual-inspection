# Screws data set

## Data Format
All images are 700 x 789 pixel JPGs.
There is variation between the image: Up to 15 deg of rotation and 100 pixels of translation between images.
Every image uses the same bounding boxes.
The four boxes used in pixels (xmin, ymin, xmax, ymax)
bounding_boxes = ((5,69,261,326),(305,69,561,326),(5,429,261,686),(325,429,581,686))
These boxes are drawn on the images in the ./bounding_boxes folder.

File names are in the format 34_0110.jpg. 
34 is the image number, 0110 is a one hot encoding of the presence or screws from left to right, top to bottom. 0110 means there are two screws missing and two screws present eg.
``` bash
[ ][S]
[S][ ]
```