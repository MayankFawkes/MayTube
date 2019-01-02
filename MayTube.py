import requests, re, os
from time import sleep
class YouTube():
	def __init__(self,link=""):
		videos={}
		url="https://y2mate.com/analyze/ajax"
		headers={
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.",
			"Referer": "https://y2mate.com/",
			"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
		}
		data={
			"url": "https://www.youtube.com/watch?v={}".format(link),
			"ajax": "1"
		}
		yes=requests.post(url, data=data, headers=headers)
		data=(yes.json()["result"])
		self.find=re.findall("_id: '(.*?)'", data)
	def Download(self,ftype="",fquality=""):
		url="https://y2mate.com/convert"
		headers={
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.",
			"Referer": "https://y2mate.com/",
			"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
		}
		data={
			"type":"youtube",
			"_id":"5bfb2d467527f8ed778b4568",
			"v_id":"HVl0zT0fXes",
			"ajax":"1",
			"ftype":"mp4",
			"fquality":"720"
		}
		data["_id"]=self.find[0]
		data["v_id"]=self.find[1]
		data["ftype"]=ftype
		data["fquality"]=fquality
		yes=requests.post(url, data=data, headers=headers)
		data=(yes.json()["result"])
		find=re.findall('<a href="(.*?)"', data)
		#print(find)
		if(find):
			if("dl85.y2mate.com" in find[0].split("/")):
				return (find[0])
		else:
			yes=requests.post(url, data=data, headers=headers)
			data=(yes.json()["result"])
			find=re.findall('<a href="(.*?)"', data)
			#print(find)
			if(find):
				if("dl85.y2mate.com" in find[0].split("/")):
					return(find[0])
			else:
				return "try again"
