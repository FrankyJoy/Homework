#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : MySimWindow.py
# @Author: He Peng
# @Date  : 2017/11/25
# @Desc  : 仿真程序主界面
import wx as wx


class MySimWindow(wx.Frame):
    def __init__(self, parent=None, id=-1, title='', pos=wx.DefaultSize, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.InitUI()
        pass

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.SetBackgroundColour('#FFF8DC')

        

        pass