from PIL import Image, ExifTags
import sys, os,random

path = "/Users/zink/screws/images/"
output = "/Users/zink/screws/out/"
dirs = os.listdir( path )
del dirs[0]
deck = list(range(1, 146+1))
random.shuffle(deck)

def resize():
    for item in dirs:
        im = Image.open(path+item)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        exif=dict(im._getexif().items())

        if exif[orientation] == 3:
            im=im.rotate(180, expand=True)
        elif exif[orientation] == 6:
            im=im.rotate(270, expand=True)
        elif exif[orientation] == 8:
            im=im.rotate(90, expand=True)

        im = im.crop((0,2350,1750,4650))
        im = im.resize((600,789), Image.ANTIALIAS)
        f, e = os.path.splitext(output+str(deck.pop()))
        im.save(f + '.jpg', 'JPEG', quality=90)

resize()