from PIL import Image
import os, sys

path = "./your_path/";
dirs = os.listdir( path );

def convert():
    for item in dirs:
         if item == '.DS_Store':
             continue
         if os.path.isfile(path+item):
             im = Image.open(path+item);
             f, e = os.path.splitext(path+item);
             rgb_im = im.convert('RGB');  
             rgb_im.save(f + '.jpg', 'JPEG');
convert();
