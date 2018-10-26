from shutil import copyfile

def main():
    print("Copying file")
    copyfile("cropped_tweet.html", "cropped_tweet_temp.html")
    print("Done")

if __name__ == "__main__":
    main()