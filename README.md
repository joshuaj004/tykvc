# tykvc
A repository to create your own tweet based off of the iconic "Thank you Kanye, very cool!" tweet.

![tykvc](https://github.com/joshuaj004/tykvc/blob/master/readme.png)

Can be used in one of two ways: Command line interface or Flask web page.

## Flask Set up
1. Install flask if you haven't already (`pip install flask`)
2. Set the flask app
* For osx/linux `export FLASK_APP=app.py`
* For windows cmd `set FLASK_APP=app.py`
* For powershell `$env:FLASK_APP = "app.py`
3. `flask run`

![ui](https://github.com/joshuaj004/tykvc/blob/master/webpage.png)

## Command Line
Pretty straight forward, you can even pass in a new image with the -oa flag. 

```
usage: tweet_process.py [-h] [-itn --innertweetname [itn]]
                        [-ith --innertweethandle [ith]]
                        [-itc --innertweetcontents [itc]]
                        [-otn --outertweetname [otn]]
                        [-oth --outertweethandle [oth]]
                        [-otc --outertweetcontents [otc]]
                        [-oa --outeravatar [oa]]

Create your own tweet based off of the iconic "Thank you Kanye, very cool!"
tweet.

optional arguments:
  -h, --help            show this help message and exit
  -itn --innertweetname [itn]
                        Replaces the inner tweet name
  -ith --innertweethandle [ith]
                        Replaces the inner tweet handle
  -itc --innertweetcontents [itc]
                        Replaces the inner tweet contents
  -otn --outertweetname [otn]
                        Replaces the outer tweet name
  -oth --outertweethandle [oth]
                        Replaces the outer tweet handle
  -otc --outertweetcontents [otc]
                        Replaces the outer tweet contents
  -oa --outeravatar [oa]
                        Replaces the avatar. In the form of a link.
```

![key](https://github.com/joshuaj004/tykvc/blob/master/key.png)

## Credit
Josh Johnson - Original POC (CLI & Local Flask)
Joe Violago - Infarts/Infra opppss

