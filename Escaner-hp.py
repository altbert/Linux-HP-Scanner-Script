#!/usr/bin/python3

import requests
import time

url = 'http://192.168.0.203/eSCL/ScanJobs'

payload = {
'Host': '192.168.0.203',
'Connection': 'keep-alive',
'Content-Length': '999',
'Origin': 'http://192.168.0.203',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
'Content-Type': 'text/xml',
'Accept': '*/*',
'Referer': 'http://192.168.0.203',
'Accept-Encoding': 'gzip,deflate',
'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
'Cookie': 'sid=sb8e54d7f-3d948d3d1817d3b06bfa528dcefad1be'
}

xml = '<scan:ScanSettings xmlns:scan="http://schemas.hp.com/imaging/escl/2011/05/03" xmlns:dd="http://www.hp.com/schemas/imaging/con/dictionaries/1.0/" xmlns:dd3="http://www.hp.com/schemas/imaging/con/dictionaries/2009/04/06" xmlns:fw="http://www.hp.com/schemas/imaging/con/firewall/2011/01/05" xmlns:scc="http://schemas.hp.com/imaging/escl/2011/05/03" xmlns:pwg="http://www.pwg.org/schemas/2010/12/sm"><pwg:Version>2.1</pwg:Version><scan:Intent>Photo</scan:Intent><pwg:ScanRegions><pwg:ScanRegion><pwg:Height>3507</pwg:Height><pwg:Width>2481</pwg:Width><pwg:XOffset>0</pwg:XOffset><pwg:YOffset>0</pwg:YOffset></pwg:ScanRegion></pwg:ScanRegions><pwg:InputSource>Platen</pwg:InputSource><scan:DocumentFormatExt>image/jpeg</scan:DocumentFormatExt><scan:XResolution>200</scan:XResolution><scan:YResolution>200</scan:YResolution><scan:ColorMode>RGB24</scan:ColorMode><scan:CompressionFactor>25</scan:CompressionFactor><scan:Brightness>600</scan:Brightness><scan:Contrast>600</scan:Contrast></scan:ScanSettings>'


ing = 0
def get_url():
	r = requests.post(url,data=xml,headers=payload)
	print(r.status_code)

	try:
		x = r.headers
		url_img = x['Location']
	except:
		url_img = ""

	return url_img,r.status_code 



while True:
	url_img,stat_code = get_url()

	if stat_code == 201:
		print("all done")
		
		time.sleep(4)
		
		img = requests.get(url_img+"/NextDocument")
		file = open("/tmp/img"+str(ing)+".jpg", "wb")
		file.write(img.content)
		file.close()
		ing = ing + 1
	
	else:
		print("Impresora ocupada")

	input("Presiona enter para continuar...")
