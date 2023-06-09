Python script to convert greek text to speech, using the acapela online service. Tested on Mac OS X & Ubuntu Linux 12.04.

**Update: a new script that works with Python3 (`acapely.python3.py`) has been tested and uploaded.**

Usage: 

```$ python acapela.py
Enter greek phrase to be converted to speech:
(File will be downloaded and saved to current directory as 'voice.mp3')
<ENTER PHRASE HERE>
```

Now play the file:

`$ mpg123 voice.mp3`

Requirements:

Feedparser	(Python Module)
(Ubuntu Linux => sudo apt-get install python-feedparser)
