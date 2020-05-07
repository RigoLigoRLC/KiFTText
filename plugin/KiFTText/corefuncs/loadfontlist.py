import os
from .. import freetype


def check_if_is_font_extension(filename):
    extension = filename[-3:]
    if extension == "ttf" or extension == "ttc" or extension == "otf":
        return True
    else:
        return False


def regressively_get_files_of(path):
    ret = []
    for root, dirs, files in os.walk(path):
        for individual_files in files:
            ret.append(os.path.join(root, individual_files))
    return ret


def get_linux_fonts():
    ret = {}
    for root, dirs, files in os.walk("/usr/share/fonts"):
        for font_group in dirs:
            current_group = []
            for individual_file in regressively_get_files_of(os.path.join(root, font_group)):
                if check_if_is_font_extension(individual_file):
                    temp_font = None
                    try:
                        temp_font = freetype.Face(individual_file)
                    except:
                        continue
                    else:
                        current_group.append([individual_file,
                                              str(temp_font.family_name, 'utf-8') + " " +
                                              str(temp_font.style_name, 'utf-8')
                                              ])
            if len(current_group) != 0:
                ret[font_group] = current_group
        break  # Only iterate through the first layer
    return ret


def get_windows_fonts():
    ret = {'Windows Default Group': []}
    for root, dirs, files in os.walk("C:\\Windows\\Fonts"):
        for individual_file in files:
            if check_if_is_font_extension(os.path.join(root, individual_file)):
                ret['Windows Default Group'].append(individual_file)
    return ret
