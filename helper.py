# Python Modules
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
import sys

tagList = ["ImageWidth", "ImageLength", "ApertureValue", "ExifImageHeight", "DateTimeDigitized", "MaxApertureValue", "ExifVersion", "ColorSpace", "Contrast", "Saturation", "FocalLength", "SubjectDistanceRange", "ExposureMode", "Model", "SubsecTimeOriginal", "Orientation", "YCbCrPositioning", "ensingMethod","ExposureBiasValue", "XResolution", "YResolution", "ExposureTime", "ExifInteroperabilityOffset", "ExposureProgram", "GPSInfo", "ISOSpeedRatings", "ResolutionUnitWhiteBalanceMeteringMode", "ComponentsConfiguration", "FNumber","Software", "DateTime", "ShutterSpeedValue",
"Flash", "SceneType", "Sharpness", "ExifImageWidth", "CustomRendered", "FlashPixVersion", "SubjectDistance", "SceneCaptureType", "DateTimeOriginal", "SubsecTime", "ExifOffset", "SubsecTimeDigitized", "BrightnessValue", "MakerNote"]


'''
General Functions
'''

def get_Image(image_file):
    image = Image.open(image_file)
    return image

def printAll_EXIF_Data(exif_dict):
    for tag, value in exif_dict.items():
        key = TAGS.get(tag, tag)
        print(key + ": " + str(value))

def getEXIF_Tag(exif_dict):
    flag = 0
    tagRequest = None
    tag_data = None

    while (flag == 0):
        tagRequest = input("Tag name: ")

        # Check for legitimate Tag
        for tag in tagList:
            if tagRequest == tag:
                # Set Flag to 1 to exit while loop
                flag = 1
                break

        if flag == 1:
            print("Tag Found")
        else:
            print("No Such Tag Found")
            # Continue while loop
    # END of While Loop

    if exif_dict:
        for tag, value in exif_dict.items():
            decoded = TAGS.get(tag, tag)

            if decoded == tagRequest:
                tag_data = value
                break
    # Create Tuple
    exif_data_request = (tagRequest, tag_data)

    return exif_data_request


'''
GPS Tag
'''
def getEXIF_GPS_Info(exif_dict):
    exif_data = {}
    gpsData = {}
    if exif_dict:
        for tag, value in exif_dict.items():
            decoded = TAGS.get(tag, tag)

            if decoded == "GPSInfo":
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gpsData[sub_decoded] = value[t]
                exif_data[decoded] = gpsData
            else:
                exif_data[decoded] = value
    return exif_data

def get_if_exist(data, key):
    if key in data:
        return data[key]
    else:
        return None

def convert_to_degress(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)

def get_latitude_longitude(exif_data):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    latitude = None
    longitude = None

    if "GPSInfo" in exif_data:
        gps_info = exif_data["GPSInfo"]

        gps_latitude = get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = get_if_exist(gps_info, 'GPSLatitudeRef')

        gps_longitude = get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = get_if_exist(gps_info, 'GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            latitude = convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":
                latitude = 0 - latitude
            else:
                pass

            longitude = convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                longitude = 0 - (longitude)
            else:
                pass
        else:
            pass
    else:
        return None

    return latitude, gps_latitude_ref, longitude, gps_longitude_ref

def printIMG_GPS_Coordinates(latitude, latitude_Dir, longitude, longitude_Dir):
    print('Latitude: {} degrees {}\n'
          'Longitude: {} degrees {}'.format(latitude, latitude_Dir, longitude, longitude_Dir))
    return None

