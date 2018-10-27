from shutil import copyfile
import fileinput, argparse

def main():
    print("Copying file")
    copyfile("cropped_tweet.html", "cropped_tweet_temp.html")
    print("replacing text")
    replace_dict = process_flags()
    replace_text(replace_dict)
    print("Done")

def process_flags():
    parser = argparse.ArgumentParser(description='Create your own tweet based off of the iconic "Thank you Kanye, very cool!" tweet.')
    parser.add_argument('-itn --innertweetname', metavar='metavar', type=str, nargs='?',
                    help='Replaces the inner tweet name',
                    default='ye')

    parser.add_argument('-ith --innertweethandle', metavar='metavar', type=str, nargs='?',
                    help='Replaces the inner tweet handle',
                    default='kanyewest')

    parser.add_argument('-itc --innertweetcontents', metavar='metavar', type=str, nargs='?',
                    help='Replaces the inner tweet contents',
                    default='tiger blood or something')

    parser.add_argument('-otn --outertweetname', metavar='metavar', type=str, nargs='?',
                    help='Replaces the outer tweet name',
                    default='Donald J. Trump')

    parser.add_argument('-oth --outertweethandle', metavar='metavar', type=str, nargs='?',
                    help='Replaces the outer tweet handle',
                    default='realDonaldTrump')

    parser.add_argument('-otc --outertweetcontents', metavar='metavar', type=str, nargs='?',
                    help='Replaces the outer tweet contents',
                    default='Thank you {{INNERTWEETNAME}}, very cool!"')

    args = parser.parse_args()

    replace_dict = {
        "{{OUTERTWEETNAME}}": vars(args)['otn __outertweetname'],
        "{{OUTERTWEETHANDLE}}": vars(args)['oth __outertweethandle'],
        "{{OUTERTWEETCONTENTS}}": vars(args)['otc __outertweetcontents'],
        "{{INNERTWEETNAME}}": vars(args)['itn __innertweetname'],
        "{{INNERTWEETHANDLE}}": vars(args)['ith __innertweethandle'],
        "{{INNERTWEETCONTENTS}}": vars(args)['itc __innertweetcontents']
    }

    print(vars(args))
    return replace_dict

def replace_text(replace_dict):
    f = open("cropped_tweet_temp.html", encoding="utf8")
    filedata = f.read()
    f.close()

    for key in replace_dict:
        filedata = filedata.replace(key, replace_dict[key])

    f = open("cropped_tweet_temp.html", 'w', encoding="utf8")
    f.write(filedata)
    f.close()

if __name__ == "__main__":
    main()