#! env python
# -*- coding: utf-8 -*-

import wx
from MyProject1MyFrame1Child import MyProject1MyFrame1Child

if __name__ == '__main__':
	app = wx.App(False)
	frame = MyProject1MyFrame1Child(None)
	frame.Show(True)
	app.MainLoop()
