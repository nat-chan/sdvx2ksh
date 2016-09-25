#!/usr/bin/env python
# coding:utf-8
import sys
import urllib2
from urllib2 import HTTPError
import numpy as np
from selenium import webdriver
from cStringIO import StringIO
from PIL import Image

###デバッグ用関数
show = lambda a: Image.fromarray(np.uint8(a)).show()
D = lambda l: [i-j for i,j in zip(l[:-1],l[1:])]

def toStr(arr):
	return '\r\n'.join(
		[
			''.join(i)
			for i in arr
		]
	)

def color_picker(arr):
	'''
	与えた領域に含まれる色とその量を表示する関数
	'''
	def rgba2hex(rgba):
		r, g, b, a = rgba
		R = r*6/256
		G = g*6/256
		B = b*6/256
		c = 36*R + 6*G + B + 16
		return "\033[48;5;"+str(c)+"m  \033[m"

	colors = [str(k) for k in arr.reshape((-1,4))]
	dic = {c:str(colors.count(c)) for c in set(colors)}
	for k in sorted(dic.items(), key=lambda x:int(x[1]), reverse=True):
		c = rgba2hex([int(i) for i in k[0][1:-1].split()])
		print k[0] + ' : ' + c + ' : ' + str(k[1])

###雑記
'''
color
ショート
黄縁(255,181,0)
黄(255,148,27,255)
ロング
黄(255,159,7,107)
黄赤(252,102,106)
17,37
12,22,32,42
 A or B or C ... の時はAを最もTrueになりやすいものにする
mt = np.r_[tuple(arr)]
'''

class Score:
	'''
	SOUND VOLTEXの譜面を表現するクラス
	インスタンス化の時はsdvx.inの譜面ページのurlを食べさせる
	'''
	def __init__(self, url):
		self.img = {}
		self.arr = {}
		self.url = {}
		self.version = url[19:21]
		self.id = url.split('/')[4]
		self._d = url[-5]
		self.difficulty = {'n':'NOVICE',   'a':'ADVANCED', 'e':'EXHAUST',
		              'i':'INFINITE', 'g':'GRAVITY'}[self._d]
		self.path = '/'.join(url.split('/')[:4]) + '/'
		self.url['url']    = url
		self.url['bg']     = self.path + self.id + '/' + self.id + 'bg.png'
		self.url['bar']    = self.path + self.id + '/' + self.id + 'bar.png'
		self.url['jacket'] = self.path + self.id + '/' + self.id + self._d + '.jpg'
		self.url['data']   = self.path + 'obj/data' + self.id + self._d + '.png'

	def setDetail(self):
		'''
		譜面サイトをjavascriptレンダリングして詳しい譜面情報を入手
		'''
		driver = webdriver.PhantomJS()
		driver.get(self.url['url'])

		self.title  = driver.find_elements_by_class_name('f1')[2].text
		self.artist = driver.find_elements_by_class_name('b2')[0].text[2:]
		self.level  = driver.find_elements_by_tag_name('a')
		self.bpm    = driver.find_elements_by_class_name('f1')[3].text
#TODO DIABLOSIS::Nāgaにてclass_nameがb2になっている
		self.chain  = driver.find_element_by_class_name('e1').text

		elements = driver.find_elements_by_tag_name('a')
		self.url['fx']   = elements[2].get_attribute('href')
		self.url['nofx'] = elements[3].get_attribute('href')

		texts = driver.find_elements_by_class_name('ef')[2].text.split('\n')
		self.effect      = texts[0]
		self.illustrator = texts[1]

		self.screenshot = Image.open(StringIO(driver.get_screenshot_as_png()))

		driver.close()

	def getImg(self, key):
		if key not in self.img:
			try:
				url = self.url[key]
				imgdata = urllib2.urlopen(url).read()
				self.img[key] = Image.open(StringIO(imgdata))
			except HTTPError:
				if key == 'bg':
					self.url['bg'] = self.url['bg'][:-6] + self._d + 'bg.png'
				elif key == 'bar':
					self.url['bar'] = self.url['bar'][:-7] + self._d + 'bar.png'
				else:
					raise HTTPError(str(key)+'のurlが不正です')
				url = self.url[key]
				imgdata = urllib2.urlopen(url).read()
				self.img[key] = Image.open(StringIO(imgdata))
		return self.img[key]

	def getArr(self, key):
		if key not in self.arr:
			self.arr[key] = np.array(self.getImg(key).convert('RGBA'))
		return self.arr[key]

	def setSubscripts(self):
		bg =  self.getArr('bg')
		sample = bg[-1,:,3]
		x = np.where(sample != 0)[0][::55]
		Y = []
		for i in x:
			sample = bg[:,i+8,0]
			Y.append(np.where(sample == 204)[0])
		self.subscripts = [x, Y]

	def __getitem__(self, j):
		if 'subscripts' not in dir(self):
			self.setSubscripts()

		data = self.getArr('data')
		x, Y = self.subscripts

		for i, y in enumerate(Y):
			if j < len(y) - 1:
				return data[y[-2-j]:y[-1-j],x[i]:x[i]+55]
			else:
				j -= len(y) -1
		raise IndexError('Score index out of range')

	def __len__(self):
		if 'subscripts' not in dir(self):
			self.setSubscripts()
		return sum(len(i) - 1 for i in self.subscripts[1])

	def show(self):
		if 'self' not in self.img:
			bg   = self.getArr('bg').astype('float')
			data = self.getArr('data').astype('float')
			bar  = self.getArr('bar')

			tmp = (bg[:,:,:3]*bg[:,:,(3,3,3)]+data[:,:,:3]*data[:,:,(3,3,3)])/255
			mask = tmp > 256

			tmp = np.uint8(~mask*tmp + 255*mask)
			mask = bar[:,:,(3,3,3)] == 255
			tmp = ~mask*tmp + bar[:,:,:3]

			self.img['self'] = Image.fromarray(tmp)

		self.img['self'].show()

def isBTshort(arr):
	return np.all(arr == (254,255,252,255),axis=2)

#def isBTlong(sample):
#	white_l = (
#		(209,210,207,255),#灰
#
#		(226,148,191,255),#灰の上に赤
#		(220,174,200,255),
#		(234,125,191,255),
#		(209,201,206,255),
#
#		(152,168,224,255),#灰の上に青
#		(137,159,229,255),
#		(174,187,218,255),
#		(189,200,221,255),
#		(209,201,206,255)
#	)
#	return np.any(
#		np.c_[
#			tuple(
#				np.all(sample == w,axis=1)
#				for w in white_l
#			)
#		]
#	,axis=1)

def isBTlong(arr):
	x = arr[:,:,0]
	y = arr[:,:,1]
	z = arr[:,:,2]
	return -0.835*x -1.015*y + 483.48 < z
#	return 0.835*arr[:,:,0] + 1.015*arr[:,:,1] + arr[:,:,2] > 483.48

def parseBT(arr, mode):
	if arr.shape[0] % mode == 0:
		d = arr.shape[0]/mode
	else:
		raise Exception('画像を'+str(mode)+'分割できません')
	sample = arr[:,(12,22,32,42)][::-1][1::d]
	s = isBTshort(sample)
	l = isBTlong(sample) & ~s
	return (2*l+s).astype('|S1')

def isFXshort(sample):
	#yellow_s = ((255,148,27,255),(225,148,27,255))
	return sample[:,:,3] == 255

#def isFXlong(sample):
#	yellow_l = (
#		(255,159,7,107),#黄
#
#		(252,102,106,166),#黄の上に赤
#		(251,88,133,189),
#		(252,93,124,182),
#		(251,96,116,174),
#		(251,98,110,170),
#		(254,138,42,122),
#		(253,110,95,151),
#		(251,93,120,178),
#		(254,124,69,135),
#
#		(140,125,153,166),#黄の上に青
#		(115,123,187,189),
#		(128,125,171,176),
#		(122,123,178,182),
#		(136,126,160,169),
#		(200,147,76,128),
#		(155,137,135,154),
#		(132,124,165,172),
#		(238,153,31,114),
#		(176,141,109,141),
#		(143,129,153,164)
#	)
#	return np.any(
#		np.c_[
#			tuple(
#				np.all(sample == y,axis=1)
#				for y in yellow_l
#			)
#		]
#	,axis=1)
def isFXlong(arr):
	return (0.171104*arr[:,:,0] - 0.681597*arr[:,:,1] + arr[:,:,2] < 156.169) & \
	       ~np.all(arr == [0,0,0,0],axis=2)

def parseFX(arr, mode):
	if arr.shape[0] % mode == 0:
		d = arr.shape[0]/mode
	else:
		raise Exception('画像を'+str(mode)+'分割できません')

	sample = arr[:,(17,37)][::-1][1::d]
	s = isFXshort(sample)
	l = isFXlong(sample) & ~s
	return (2*s+l).astype('|S1')
	
def parseVOL(arr, mode):
	return np.array([['-','-']]*mode)

def parseMeasure(arr, mode):
	bt  = parseBT(arr, mode)
	fx  = parseFX(arr, mode)
	vol = parseVOL(arr, mode)
	v   = np.array(['|']*mode)
	return toStr(np.c_[bt,v,fx,v,vol])

def parseScore(score, mode):
	h = '\r\n--\r\n'
	score = h.join([parseMeasure(k, mode) for k in score])
	return h + score + h
