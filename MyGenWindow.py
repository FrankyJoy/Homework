#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : MyGenWindow.py
# @Author: He Peng
# @Date  : 2017/11/22
# @Desc  : 数据生成窗口

import wx as wx
import wx.lib.buttons as wxBtn
from MyPlotWindow import *

class MyGenWindow(wx.Frame):
    def __init__(self, parent=None, id=-1, title='', pos=wx.DefaultSize, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.InitUI()
        self.funcID = 0
        self.timeID = 0
        self.frenID = 0
        pass

    #   填充数据生成窗口组件
    def InitUI(self):
        self.pl_gen = wx.Panel(self)
        self.pl_gen.SetBackgroundColour('#F0F8FF')

        #  重型布局BoxSizer
        vbox = wx.BoxSizer(wx.VERTICAL)
        #   CO浓度布局块
        nm = wx.StaticBox(self.pl_gen, -1, 'CO浓度生成:')

        coSizer = wx.StaticBoxSizer(nm, wx.HORIZONTAL)   #   RadioButton的StataicSizer
        funcList = ['Y = aX + b', 'Y = aX + Rand(b~c)',u'正态分布']
        timeList = [u'30 秒',u'60 秒',u'120 秒']
        frenList = ['1 次/秒','2 次/秒','4 次/秒']
        self.radio_func =wx.RadioBox(self.pl_gen, -1, "数据生成函数", (10, 10), wx.DefaultSize,
                    funcList, 3, wx.RA_SPECIFY_ROWS)
        self.radio_time = wx.RadioBox(self.pl_gen, -1, "采样时间", (10, 10), wx.DefaultSize,
                                timeList, 3, wx.RA_SPECIFY_ROWS)
        self.radio_fren = wx.RadioBox(self.pl_gen, -1, "采样频率", (10, 10), wx.DefaultSize,
                                frenList, 3, wx.RA_SPECIFY_ROWS)
        coSizer.Add(self.radio_func, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        coSizer.Add(self.radio_time, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        coSizer.Add(self.radio_fren, 0, wx.ALL | wx.ALIGN_LEFT, 5)

        self.btn_co_confirm = wxBtn.GenButton(self.pl_gen, label = u'预览&确认', size = (100, 20))
        self.btn_co_confirm.SetBackgroundColour('#D2B48C')
        coSizer.Add(self.btn_co_confirm, wx.ALL | wx.CENTER | wx.BOTTOM, 5)

        self.Bind(wx.EVT_RADIOBOX,self.getFuncID,self.radio_func)
        self.Bind(wx.EVT_RADIOBOX, self.getTimeID, self.radio_time)
        self.Bind(wx.EVT_RADIOBOX, self.getFrenID, self.radio_fren)

        self.Bind(wx.EVT_BUTTON,self.btn_cb_co,self.btn_co_confirm)
        vbox.Add(coSizer, 0, wx.ALL | wx.EXPAND, 5)
        # vbox.Add(viSizer, 0, wx.ALL | wx.EXPAND, 5)
        self.pl_gen.SetSizer(vbox)
        self.Centre()

    pass
    ###############        绑定CO的RadioButton点击事件        #############
    def getFuncID(self,handle):
        self.funcID = self.radio_func.GetSelection()
        print("选择的functionID为"+str(self.funcID))
        pass
    def getTimeID(self,handle):
        self.timeID = self.radio_time.GetSelection()
        print("选择的timeID为"+str(self.timeID))
        pass
    def getFrenID(self,handle):
        self.frenID = self.radio_fren.GetSelection()
        print("选择的frencyID为"+str(self.frenID))
        pass

    def btn_cb_co(self,handle):
        print('创建数据生预览窗口')
        self.genPlot = MyPlotWindow(self,id=-1, title=u'综合管廊火灾仿真---数据生成', pos=(10, 10),
                               size=(500, 600), style=wx.DEFAULT_FRAME_STYLE,
                               funcFlag=self.funcID,timeFlag=self.timeID,frenFlag=self.frenID)
        self.genPlot.Center()
        self.genPlot.Show(True)
        pass
        #