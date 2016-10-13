#!/usr/bin/env python
# coding:utf-8
from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

option = {
	"compressed"   : 1,
	"optimize"     : 2,
	"bundle_files" : 3
}

setup(
	options = {"py2exe" : option},
	windows = [{"script" : "gui.py"}],
	zipfile = None
)
