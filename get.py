#!/usr/bin/env python

from PIL import Image
import urllib.request
import io
import time
import requests
import lxml.html as lh

def get_foto(url):
	URL = url
	response = urllib.request.urlopen(URL)
	f = io.BytesIO(response.read())
	img = Image.open(f)
	img.show()
	
def check_nim(nim):

	url = 'http://www.amikom.ac.id/index.php/status'
	user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


	data= {
		'nim': nim,
		'cek': 'Cek+Status+%BB'
	}

	respon = requests.post(url, headers=user_agent, data=data)
	tree = lh.document_fromstring(respon.content)

	nama = tree.xpath('//div[@class="nama"]/text()')
	nim = tree.xpath('//div[@class="npm"]/text()')
	jurusan = tree.xpath('//div[@class="jurusan"]/text()')
	foto = tree.xpath('//img[@class="foto"]/@src')

	if nama:
		print('\x1b[1;32;40m'+'============[OK]============'+'\x1b[0m')
		print('\x1b[1;32;40m'+'NAMA \t: {nama}'.format(nama = nama[0])+'\x1b[0m')
		print('\x1b[1;32;40m'+'NIM  \t: {nim}'.format(nim = nim[0])+'\x1b[0m')
		print('\x1b[1;32;40m'+'JUR  \t: {jur}'.format(jur = jurusan[0])+'\x1b[0m')
		print ('\x1b[1;32;40m'+'FOTO  \t: {foto}'.format(foto = foto[0])+'\x1b[0m')
		print('\x1b[1;32;40m'+'============================'+'\x1b[0m')
		print('')
		get_foto(foto[0])
	else:
		print ('\x1b[1;31;40m'+'==========[NODATA]=========='+'\x1b[0m')
		print ('')
	

if __name__ == '__main__':

	#input	
	sum_nim = input('Masukkan Jumlah NIM yang ingin dicari : ')
	start_nim = input('Start NIM : ')

	#split
	nim_incr = start_nim.split('.')
	nim_first = nim_incr[0]
	nim_midd = nim_incr[1]
	nim_last = nim_incr[2]


#TEST
#	print nim_first
#	print nim_midd
#	print nim_last
	
#	nim_last = int(nim_last)+1
#	print str(nim_last).zfill(4)

	
	#for
	for i in range(0, int(sum_nim)):
		full_nim = str(nim_first) +'.'+ str(nim_midd) +'.'+ str(nim_last).zfill(4)
		check_nim(full_nim)
		nim_last = int(nim_last)+1
		time.sleep(0.30)	
