from PIL import Image, ImageDraw
import sys, os,random

path = "/Users/zink/screws/labeled/"
output = "/Users/zink/screws/tst/"
dirs = os.listdir( path )
del dirs[0]
deck = list(range(1, 146+1))
random.shuffle(deck)

rects = ((5,69,261,326),(305,69,561,326),(5,429,261,686),(325,429,581,686))
t=5
i=0

def resize():
    for item in dirs:
        im = Image.open(path+item)
        draw = ImageDraw.Draw(im)
        for rect in rects:
            draw.rectangle(((rect[0],rect[1]-t),(rect[2]+t,rect[1])), fill="blue", outline = "blue")
            draw.rectangle(((rect[2],rect[1]-t),(rect[2]+t,rect[3])), fill="blue", outline = "blue")
            draw.rectangle(((rect[2]+t,rect[3]),(rect[0],rect[3]+t)), fill="blue", outline = "blue")
            draw.rectangle(((rect[0],rect[3]+t),(rect[0]-t,rect[1]-t)), fill="blue", outline = "blue")

        del draw
        f, e = os.path.splitext(output+item)
        im.save(f + '.jpg', 'JPEG', quality=90)

resize()