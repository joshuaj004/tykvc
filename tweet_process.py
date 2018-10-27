from shutil import copyfile
import fileinput

def main():
    print("Copying file")
    copyfile("cropped_tweet.html", "cropped_tweet_temp.html")
    print("replacing text")
    replace_dict = replacement_vars()
    replace_text(replace_dict)
    print("Done")


def replacement_vars():
    replace_dict = {
        "{{INNERTWEETNAME}}": "ye",
        "{{INNERTWEETHANDLE}}": "kanyewest",
        "{{INNERTWEETCONTENTS}}": "tiger blood or something",
        "{{OUTERTWEETNAME}}": "Donald J. Trump",
        "{{OUTERTWEETHANDLE}}": "realDonaldTrump",
        "{{OUTERTWEETCONTENTS}}": "Thank you Kanye, very cool!",
    }
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