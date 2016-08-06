from PIL import Image
from PIL.ExifTags import TAGS

def open_image(path):
    img = Image.open(path) 
    return img

def get_exif_data(img_obj):
    tags = img_obj._getexif()

    try:
        metadata = {}
        if tags:
            print("Found meta data ! Scanning ...")
            for tag, value in tags.items():
                tagname = TAGS.get(tag)
                metadata[tagname] = value
            return metadata
    except:
        print("Sorry, no Exif data could be retrived from this image")


def get_gps_info(exifData):
    print("Scanning for coordinates ...")
    try:
        gpsInfo = exifData['GPSInfo']
        lat = [gpsInfo[2][0][0], gpsInfo[2][1][0], gpsInfo[2][2][0]]
        lon = [gpsInfo[4][0][0], gpsInfo[4][1][0], gpsInfo[4][2][0]]

        if lat and lon:
            print("Found LatLng values")
            return lat, lon
        else:
            print("Sorry no usable GPS info could be retrived")
    except:
        print("Sorry bruv, no GPS info is available for this image")

def convert_to_lat_lng(coords):
    pass

def launch_map():
    pass
