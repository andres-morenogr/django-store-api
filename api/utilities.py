import json
import re

def get_city_name(string):
    city_name = string.split('name')[1].split(", ")[1]
    city_name = re.sub(r'[^\w\s]','', city_name)
    return city_name

def get_city_code(string):
    city_code = string.split('code')[1].split(", ")[1]
    city_code = re.sub(r'[^\w\s]','', city_code)
    return city_code

def get_pictures(pictures):
    pictures_list = pictures.split("'")
    for item in pictures_list:
        if len(item) < 3: pictures_list.remove(item)
    return(pictures_list)
