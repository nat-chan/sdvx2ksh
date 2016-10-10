#!/usr/bin/env python
# coding:utf-8
from __future__ import unicode_literals
import wx
import sys, time
import pafy

class myConsole(wx.TextCtrl):
	def __init__(self, *args, **kwargs):
		wx.TextCtrl.__init__(self,style=wx.TE_MULTILINE|\
		                                wx.TE_READONLY|\
		                                wx.HSCROLL|\
		                                wx.VSCROLL, *args, **kwargs)
		self.SetBackgroundColour('black')
		self.SetForegroundColour('cyan')
		sys.stdout = self
		sys.stderr = self
		self.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL))

	def flush(self):
			print '\033[2A',
			wx.Yield()

class myFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, 'sdvx2ksh_ver0.1β')
		self.SetSize((600,700))
		self.panel = wx.Panel(self, size=self.GetSize())
		self.panel.SetBackgroundColour('white')
		font = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

		self.text = wx.StaticText(self.panel, -1, 'url')
		self.text.SetFont(font)

		self.urlctrl = wx.TextCtrl(self.panel, -1)
		self.urlctrl.SetFont(font)

		self.button = wx.Button(self.panel, -1, 'run', size=(40,30))
		self.button.SetFont(font)
		self.button.Bind(wx.EVT_BUTTON, self.run)

		self.log = myConsole(self.panel, -1, pos=(0,50))

		layout_url = wx.BoxSizer(wx.HORIZONTAL)
		layout_url.Add(self.text, proportion=0)
		layout_url.Add(self.urlctrl, proportion=1)
		layout_url.Add(self.button, proportion=0)

		layout_outer = wx.BoxSizer(wx.VERTICAL)
		layout_outer.Add(layout_url, proportion=0)
		layout_outer.Add(self.log, proportion=1)
		self.panel.SetSizer(layout_outer)

#		self.timer = wx.Timer(self)
#		self.Bind(wx.EVT_TIMER, self.OnTimer)
#		self.timer.Start(500)
#
#	def OnTimer(self, event):
#		wx.Yield()


	def run(self, event):
		url = self.urlctrl.GetValue()
		self.button.Disable()
		try:
#			video = pafy.new('https://www.youtube.com/watch?v=TYUnccLCQnw')
			video = pafy.new(url)
			best = video.getbestaudio()
			best.download('test.m4a')
		finally:
			self.urlctrl.SetValue('')
			self.button.Enable()

if __name__ == '__main__':
	app = wx.App()
	frame = myFrame()
	frame.Show()
	app.MainLoop()
	sys.stdout = sys.__stdout__
