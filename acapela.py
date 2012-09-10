#!/usrc/bin/python
# -*- coding: utf-8 -*-

import sys
import urllib
import urllib2
import re
import feedparser
from subprocess import call
from urllib2 import Request, urlopen, URLError, HTTPError

url = "http://vaassl3.acapela-group.com/Services/Synthesizer"

class bcolors:
	HEADER = "\033[95m"
	OKBLUE = "\033[94m"
	OKGREEN = "\033[92m"
	WARNING = "\033[93m"
	FAIL = "\033[91m"
	ENDC = "\033[0m"

print "Enter greek phrase to be converted to speech:"
print "(File will be downloaded and saved to current directory as 'voice.mp3')"
txt = raw_input()

def acapela( text = "δοκιμή", filename = 'voice.mp3' ):

	values = {
		'cl_env' : 'FLASH_AS_3.0',
		'req_snd_kbps' : 'EXT_CBR_128',
		'cl_vers' : '1-30',
		'req_snd_type' : '',
		'cl_login' : 'demo_web',
		'cl_app' : '',
		'req_asw_type' : 'INFO',
		'req_voice' : 'dimitris22k',
		'cl_pwd' : 'demo_web',
		'prot_vers' : '2',
		'req_text' : text
		}

	data = urllib.urlencode(values)
	
	headers = { 
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0",
		"Content-Type" : "application/x-www-form-urlencoded",
		"Host" : "vaassl3.acapela-group.com" 
		}

	req = urllib2.Request(url, data, headers)

	try:
		response = urllib2.urlopen(req)
		page = response.read()
		match = re.search(r'http://(.*)mp3', page)
		if match:
			urllib.urlretrieve(match.group(), filename)
	except URLError as e:
		print "Error", e
	except HTTPError as e:
		print "HTTPError", e

acapela( txt )

