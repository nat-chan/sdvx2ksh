#!/usr/bin/env python
# coding:utf-8
import sys

f = lambda src:[
	[k[12:18].lower(),k[34:-3]]
	for k in src.split('\n')
	if k[:12] == '<script>SORT'
]

if __name__ == '__main__':
	with open(sys.argv[1],'r') as fd:
		for k in f(fd.read()):
			print 'http://sdvx.in/'+k[0][:2]+'/obj/data'+k[0]+'.png'


