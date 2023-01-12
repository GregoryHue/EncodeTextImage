# EncodeTextImage

Light python program that allows the user to encode a text to a picture, and decode a picture to a text.

## Project setup

Get into the project folder:
```bash
cd EncodeTextImage
```

Create a new environment:

```bash
virtualenv --python="/usr/local/bin/python3" env
```

Get into that environment:

```bash
source env/bin/activate 
```

Install the librairies:

```bash
pip install -r requirements.txt
```

## Usage

Run:

```bash
python3 app/src/main.py
```

This will encode the file `app/files/intxt.txt` into a png `app/files/intxt_Ncoded.png`, and decode that png file into a new text file `app/files/intxt_Ncoded_Dcoded.txt`. This new text file should be the exact same file as the original text file.


## Versions

* Python 3.8.10
* Ubuntu 20.04.5

## Structure

```
app/
env/
.gitignore
README.md
requirement.txt
```

## TODO

* Make it executable with command line
* Add parameters
* Add interface
