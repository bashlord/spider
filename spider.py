import requests
from requests import cookies
from bs4 import BeautifulSoup
from fblogin import *
import re

def crawl():
	uid = []
	uname = []
	com = []
	comclass = []
	type = []

	response,homepage  = call_login("", "")
	plain_text = homepage.text
	soup = BeautifulSoup(plain_text)
	print plain_text
	for comment in soup.findAll('',{'':''}):
		print comment
		print "children"
		for c in comment.children:
			s = (c.get_text("|"))
			str = s.split("|")
			print str
			uname.append(str[0])
			if len(str)<2:
				type.append(str[0])
			else:
				type.append(str[1])
			com.append(str)
		for ahref in comment.findAll('a'):
			ah = ahref.get('')
			print ah
			ah1 = ah.split('?')
			uid.append(ah1[0])
			break
		print ""
		print ""
		for h3 in comment.findAll(''):
			h3id = h3.get('');
			print h3id
			comclass.append(h3id[0]+h3id[1])

	for i in range(0,len(uid)):
		requests.post('', data={
															'p1': uid[i],
															'p01': uname[i],
															'p2': com[i],
															'p3': type[i],
															'p4': comclass[i]
															})

if __name__ == '__main__':

	crawl()
