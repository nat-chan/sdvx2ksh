#!/usr/bin/env python
# coding:utf-8
import numpy as np

def isVOL(arr):
	btfx = (
		(0,0,0,0),
		(255,255,255,255),
		(255,159,7,107),
		(151,153,150,255),
		(230,231,228,255),
		(246,248,245,255),
		(255,180,61,179),
		(209,210,207,255),
		(255,181,0,255),
		(225,148,27,255),
		(254,255,252,255)
	)
	mask = reduce(
		lambda a,b:a&b,
		(np.any(arr != c,axis=2) for c in btfx)
	)
	return mask

def LR(s,arr):
	a = (-38039 + 9417*s)/(571 + 17307*s)
	b = (1061 + 44267*s)/(571 + 17307*s)
	c = (9535243 - 9318639*s)/(571 + 17307*s)
	x = arr[:,:,0]
	y = arr[:,:,1]
	z = arr[:,:,2]
	mask = a*x + b*y + c > z
	return mask

def isL(arr):
	return isVOL(arr) & LR(0.2,arr)

def isR(arr):
	return isVOL(arr) & ~LR(0.5,arr)

def P(arr):
	pos = np.where(arr)[0]
	ave = np.average(pos)
	num = len(pos)
	if num < 8:
		return None
	if num > 23:
		return (np.min(pos)+4, np.max(pos)-4)
	return ave

def Q(x):
	dic = [chr(i) for i in range(ord('0'), ord('9')+1)+
	                       range(ord('A'), ord('Z')+1)+
	                       range(ord('a'), ord('o')+1)]
	y = int(49/46.*x - 173/46.) % 50
	return dic[y]

def stringVOL(l):
	size = len(l)-2
	L = np.array(['-']*size)
	i = 0
	while i < size:
		a,b,c = l[i-1],l[i],l[i+1]
		if type(b) == tuple:
			if abs(c-b[0]) > abs(c-b[1]):
				s,e = b
			else:
				e,s = b
			L[i-1] = Q(s)
			L[i] = Q(e)
		elif type(b) == np.float64:
			if type(c) == np.float64:
				if type(a) == np.float64:
					if abs(a+b+c - 3*b) < 2:
						L[i] = ':'
					else:
						L[i] = Q(b)
				else:
					L[i] = Q(b)
			elif type(c) == tuple:
				L[i] = ':'
			else:
				L[i] = Q(b)
		i += 1
	return L

def parseVOL(self, N):
	d = 4#可変,引数にする
	try:
		top = self[N-1][d-4]
	except IndexError:
		top = np.zeros((55,4),dtype='int')
	try:
		bottom = self[N+1][::-1][3]
	except IndexError:
		bottom = np.zeros((55,4),dtype='int')

	sample = self[N][::-1][3::d]
	size = sample.shape[0]
	sample = np.r_[top[np.newaxis], sample, bottom[np.newaxis]]
	l = [P(i) for i in isL(sample)]
	r = [P(i) for i in isR(sample)]
	L = stringVOL(l)
	R = stringVOL(r)
	return np.c_[L,R]

def scoreVOL(self,N):
	arr = parseVOL(self,N)
	size = arr.shape[0]
	dummy = np.array([['0']*4+['|']+['0']*2+['|']]*size)
	return '--\r\n'+'\r\n'.join(
		[
			''.join(i)
			for i in np.c_[dummy,arr]
		]
	)
	
def removeHat(arr):
	hat = np.load('hat.npy')
	H,W = arr.shape
	h,w = hat.shape
#	dst = np.empty((H-h,W-w),dtype=int)
	for i in range(W-w):
		for j in range(H-h):
			part = arr[j:j+h,i:i+w]
			det = part^hat
			if np.abs(np.sum(det) - w*h/2)  > 17:
				part = det
