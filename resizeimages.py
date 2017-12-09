from PIL import Image
from os import listdir
from os.path import isdir, isfile, join

basewidth = 300

ext= ['.jpg', '.png', '.gif', '.png', '.jpeg']
base_path = "/home/droid/gitbox/ImageSizer/info"

def testsize(pathofimage):
    with Image.open(pathofimage) as img:
        width, height = img.size

        if width == 300:
            return 1
        else:
            return 0

def imagespider():
    import os
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(tuple(ext)):
                pathofimage = (os.path.join(root, file))
                y = testsize(pathofimage)
                if y == 1:


                    pass
                else:

                    #resize
                    img = Image.open(pathofimage)
                    wpercent = (basewidth/float(img.size[0]))
                    hsize = int((float(img.size[1])*float(wpercent)))
                    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
                    img.save(os.path.join(root, file))


imagespider()