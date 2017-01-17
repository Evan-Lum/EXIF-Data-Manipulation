'''
Exchangeable Image File
Python 3.5+
File Format: JPEG, RAW, and TIFF
'''

# https://gist.github.com/erans/983821

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from helper import *
import os
import sys



image_file = "img.jpg"

def main():

    # Get Image
    image = get_Image(image_file)
    # Display Image
    #image.show()

    # Get Exif Dictionary from Image
    exif_dict = image._getexif()

    # Search for Tag and retrieve data
    tagData = getEXIF_Tag(exif_dict) # Returns a tuple of Tag Name and Data

    # Print All Contents of Exif Dictionary
    printAll_EXIF_Data(exif_dict)

    # Extract GPS Coordinates from Image --> Exif Dictionary
    exifData = getEXIF_GPS_Info(exif_dict)
    latitude, latitude_Dir, longitude, longitude_Dir = get_latitude_longitude(exifData)

    printIMG_GPS_Coordinates(latitude, latitude_Dir, longitude, longitude_Dir)

    # Wipe EXIF Data from JPG
    #data = list(Image.getdata())
    #image_WO_exif = Image.new(image.mode, image.size)
    #image_WO_exif.putdata(data)
    #image_WO_exif.save('image_file_without_exif_Data.jpg')
    #print("[$] File Saved:")


main()
