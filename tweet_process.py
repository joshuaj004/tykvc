#! /usr/bin/env python

from shutil import copyfile
import fileinput, argparse, os

def main():
    original_file = "cropped_tweet.html"
    temp_file = "cropped_tweet_temp.html"
    # must process flags first to see if running in server mode
    replace_dict, server_mode = process_flags()
    if server_mode:
        temp_file = "templates/" + temp_file
    copyfile(original_file, temp_file)
    replace_text(replace_dict, temp_file)
    if not server_mode:
        open_html(temp_file)    

def open_html(temp_file):
    if os.name == 'nt':
        file_test = "start " + temp_file
    else:
        file_test = "open " + temp_file
    os.system(file_test)

def process_flags():
    parser = argparse.ArgumentParser(description='Create your own tweet based off of the iconic "Thank you Kanye, very cool!" tweet.')
    parser.add_argument('-itn --innertweetname', metavar='itn', type=str, nargs='?',
                    help='Replaces the inner tweet name',
                    default='ye')

    parser.add_argument('-ith --innertweethandle', metavar='ith', type=str, nargs='?',
                    help='Replaces the inner tweet handle',
                    default='kanyewest')

    parser.add_argument('-itc --innertweetcontents', metavar='itc', type=str, nargs='?',
                    help='Replaces the inner tweet contents',
                    default='tiger blood or something')

    parser.add_argument('-otn --outertweetname', metavar='otn', type=str, nargs='?',
                    help='Replaces the outer tweet name',
                    default='Donald J. Trump')

    parser.add_argument('-oth --outertweethandle', metavar='oth', type=str, nargs='?',
                    help='Replaces the outer tweet handle',
                    default='realDonaldTrump')

    parser.add_argument('-otc --outertweetcontents', metavar='otc', type=str, nargs='?',
                    help='Replaces the outer tweet contents',
                    default='Thank you {{INNERTWEETNAME}}, very cool!')

    parser.add_argument('-s --server', metavar='s', type=str, nargs='?',
                    help='True when running on a Flask server',
                    default='False')
    
    parser.add_argument('-oa --outeravatar', metavar='oa', type=str, nargs='?',
                    help='Replaces the avatar. In the form of a link.',
                    default="cropped_tweet_files/kUuht00m_bigger.jpg")

    args = parser.parse_args()

    # If running in server mode, we assume this is being served on a Flask server
    # Hence the prepend of static/
    server_mode = vars(args)['s __server']
    server_mode = True if server_mode == "True" else False
    if server_mode:
        vars(args)['oa __outeravatar'] = "static/" + vars(args)['oa __outeravatar']
    
    replace_dict = {
        "{{OUTERTWEETNAME}}": vars(args)['otn __outertweetname'],
        "{{OUTERTWEETHANDLE}}": vars(args)['oth __outertweethandle'],
        "{{OUTERTWEETCONTENTS}}": vars(args)['otc __outertweetcontents'],
        "{{INNERTWEETNAME}}": vars(args)['itn __innertweetname'],
        "{{INNERTWEETHANDLE}}": vars(args)['ith __innertweethandle'],
        "{{INNERTWEETCONTENTS}}": vars(args)['itc __innertweetcontents'],
        "{{OUTERAVATAR}}": vars(args)['oa __outeravatar']
    }

    return replace_dict, server_mode

def replace_text(replace_dict, temp_file):
    f = open(temp_file, encoding="utf8")
    filedata = f.read()
    f.close()

    for key in replace_dict:
        filedata = filedata.replace(key, replace_dict[key])

    f = open(temp_file, 'w', encoding="utf8")
    f.write(filedata)
    f.close()

if __name__ == "__main__":
    main()
