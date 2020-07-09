import requests, re, os
from time import sleep
from json import loads
from random import choice,randint
from download import download

class y2mate(download):
	Generate="https://{}.y2mate.com/analyze/ajax"
	Convert="https://{}.y2mate.com/convert"
	Headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.",
		"Referer": "https://y2mate.com/",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
	}
	def __init__(self,vid:str,ftype:str="mp4",fquality:str="720p")->None:
		self.ftype=ftype
		self.fquality=fquality
		self.v_id=vid
		self._id,self.v_id=self._videourl()
		self._videourl(True)
	def _save(self,status:bool=True)-> bool:
		super().__init__(url=self.videolink,name=self.name,status=status)
		return True
	def _server(self,new:bool=True):
		if new:
			self.Data_Gen={"url": f"https://www.youtube.com/watch?v={self.v_id}","q_auto": 0,"ajax": "1"}
		if not new:
			self.Data_Convert={"type":"youtube","_id":self._id,"v_id":self.v_id,"ajax":"1","ftype":self.ftype,"fquality":self.fquality}
		self.sub="mate"+str(choice([f"{i:02d}" for i in range(1,12)]))
	def _videourl(self,new:bool=False)->list:
		if not new:
			self._server()
			gen=requests.post(self.Generate.format(self.sub), data=self.Data_Gen, headers=self.Headers).text
			return re.findall("_id: '(.*?)'", gen)
		if new:
			self._server(False)
			res=requests.post(self.Convert.format(self.sub), data=self.Data_Convert, headers=self.Headers)
			self.name=f'{randint(10000000,99999999)}.{self.ftype}'
			self.videolink=re.findall('<a href="(.*?)"',loads(res.text)['result'])[0]
