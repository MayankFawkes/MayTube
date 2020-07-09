# -*- coding: utf-8 -*-

__author__ = 'Mayank Gupta'
__version__ = '1.0a1'
__license__ = 'License :: MIT License'

import socket,select,re,ssl,threading,sys,os
from urllib.parse import urlparse
from time import sleep

class download(object):
	def __init__(self,url:str,name:str=None,status:bool=True)->None:
		self.filename=name
		self.status=status
		request=self.RawData(url)
		self.sock=self.connect()
		self.sock.sendall(request)
		data=self.sock.recv(2048)
		self.header,image=self.hparsec(data)
		if int(self.header["status"]) is not 200:
			try:
				self.sock.close()
				self.__init__(self.header["location"],self.filename,self.status)
			except:
				print("We cant download from this URL Contact Admin with URL")
				self.sock.close()
				sys.exit(1)
		else:
			if self.status:print("Downloading From: "+self.host)
			self.download(image)
		
	def download(self,image:bytes)-> bool:
		f = open(self.filename, 'wb')
		f.write(image)
		try:
			self.size=self.header["content-length"]
			if self.status:print("Total File Size {:.3f} MB".format(int(self.size)/1048576))
		except:
			if self.status:print("No File size Given")
		self.gg=len(image)
		self.when=True
		if self.status:threading.Thread(target=self.run).start()
		while True:
			data = self.sock.recv(5120)
			if not data: break
			f.write(data)
			self.gg+=len(data)
		self.when=False
		p=int(int(self.gg)*50/int(self.size))
		if self.status:print("Process: [{}] {}% Complete {:<10}".format("█"*p+"-"*(50-p), p*100/50,"0.0 Kb/s"))
		f.close()
		self.sock.close()
		if self.status:print("\nDownloading Completed Filename: {}\n".format(self.filename))
		return True

	def run(self):
		self.temp1=0
		while self.when:
			speed=(self.gg-self.temp1)/1024
			p=int(int(self.gg)*50/int(self.size))
			print("Process: [{}] {}% Complete {:<8}Kb/s".format("█"*p+"-"*(50-p), p*100/50,"{:.2f}".format(speed)),end="\r")
			self.temp1=self.gg
			sleep(1)

	def connect(self) -> socket:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if self.protocol=="https":
			s.connect((self.host, 443))
			s = ssl.create_default_context().wrap_socket(s, server_hostname=self.host)
		elif self.protocol=="http":
			s.connect((self.host, 80))
		else:
			print("we only support HTTP and HTTPS")
			s.close()
			sys.exit(1)
		return s

	def hparsec(self,data:bytes) -> list:
		header =  data.split(b'\r\n\r\n')[0]
		store =  data[len(header)+4:]
		html = data[len(header)+4:]
		header=header.decode().split("\r\n")
		out={}
		out["status"]=header[0].split()[1]
		for n in header[1:]:
			temp=n.split(":")
			value=""
			for n in temp[1:]:
				value+=n+":"
			out[temp[0].lower()]=value[1:len(value)-1]
		return out,store

	def __url(self,url:str,host:str) -> bytes:
		send='GET {} HTTP/1.1\r\nHOST:{}\r\nConnection: close\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15\r\nAccept: */*\r\n\r\n'.format(url,host)
		return send.encode('ascii')

	def RawData(self,web_url:str)->'bytes,str,int,str':
		o=urlparse(web_url)
		self.host=o.netloc
		self.protocol=o.scheme
		if o.query:
			url=(o.path+"?"+o.query)
			if not self.filename:self.filename=input("Enter Filename -->")
		else:
			url=o.path
			filename=o.path.split("/")[-1]
		request=self.__url(url,self.host)
		return request

if __name__ == '__main__':
	link=input("Enter Url -->")
	# link='https://storge.pic2.me/download/origin/257714.jpeg'
	download(link,name=None,status=True)