import requests, re, os
def YouTube(link="",vtype="720mp4"):

	videos={}
	type={1:"1080mp4",2:"720mp4",3:"360mp4" ,4:"2403gp",5:"1443gp",6:"128mp3"}
	url="https://y2mate.com/analyze/ajax"
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.",

	}
	data={
		"url": "https://www.youtube.com/watch?v={}".format(link),
		"ajax": "1"
	}
	yes=requests.post(url, data=data, headers=headers)
	data=(yes.json()["result"])
	fi=re.findall("<td>(.*?)</td>",data)
	#print(fi)
	vis=re.findall('data-vlink="(.*?)" >',data)
	c=0
	for n,m in type.items():
		videos[m]=vis[c]
		c+=1
	return (videos[vtype])
