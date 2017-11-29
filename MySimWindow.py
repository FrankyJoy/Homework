#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : MySimWindow.py
# @Author: He Peng
# @Date  : 2017/11/25
# @Desc  : 仿真程序主界面
import wx as wx
import wx.lib.buttons as wxBtn
import numpy
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import scipy.stats
import MysqlCon

class MySimWindow(wx.Frame):
    def __init__(self, parent=None, id=-1, title='', pos=wx.DefaultSize, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.InitUI()
        pass

    def InitUI(self):
        self.SetBackgroundColour('#FFF5EE')
        self.panel = wx.Panel(self)
        #  重型布局BoxSizer
        vbox = wx.BoxSizer(wx.VERTICAL)
        #   左侧控制台输出
        nm = wx.StaticBox(self.panel, -1, '')
        coSizer = wx.StaticBoxSizer(nm, wx.HORIZONTAL)  # RadioButton的StataicSizer

        inBox1 = wx.BoxSizer(wx.VERTICAL)

        self.outInfo = wx.TextCtrl(self.panel, value = "当前未开始仿真",
                                   style = wx.TE_READONLY|wx.TE_LEFT,size=(285,660))
        self.out_save = wxBtn.GenButton(self.panel,-1,u"清空控制台输出",size=(95,30),)
        self.out_save.SetBackgroundColour('#E0EEEE')
        inBox1.Add(self.outInfo, 0, wx.ALL | wx.CENTER, 1)
        inBox1.Add(self.out_save, 0, wx.ALL | wx.CENTER, 1)

        #   中部绘图窗口
        inBox2 = wx.BoxSizer(wx.VERTICAL)
        scores = [89, 98, 70, 80, 60, 78, 85, 90]
        sum = 0
        for s in scores:
            sum += s
        average = sum / len(scores)

        t_score = numpy.arange(1, len(scores) + 1, 1)
        s_score = numpy.array(scores)

        self.figure_score = Figure()
        self.figure_score.set_figheight(4.1)
        self.figure_score.set_figwidth(8.0)
        self.axes_score = self.figure_score.add_subplot(111)

        self.axes_score.plot(t_score, s_score, 'ro', t_score, s_score, 'k')
        self.axes_score.axhline(y=average, color='r')
        self.axes_score.grid(True)
        self.axes_score.set_title(u'Please Input Parameter ')
        self.axes_score.set_xlabel(u'Empty Now ')
        self.axes_score.set_ylabel(u'Empty Now ')

        self.MyFig = FigureCanvas(self.panel, -1, self.figure_score)
        inBox2.Add(self.MyFig, 0, wx.ALL | wx.EXPAND, 1)
        self.out_save = wxBtn.GenButton(self.panel, -1, u"暂停仿真", size=(95, 30), )
        self.out_save.SetBackgroundColour('#E0EEEE')
        inBox2.Add(self.out_save, 0, wx.ALL | wx.CENTER, 1)

        #   右侧控制按钮
        inBox3 = wx.BoxSizer(wx.VERTICAL)

        self.cont_co = wxBtn.GenButton(self.panel, -1, u"暂停仿真", size=(95, 30), )
        self.cont_co.SetBackgroundColour('#E0EEEE')

        self.cont_sm = wxBtn.GenButton(self.panel, -1, u"暂停仿真", size=(95, 30), )
        self.cont_sm.SetBackgroundColour('#E0EEEE')

        self.cont_tp = wxBtn.GenButton(self.panel, -1, u"暂停仿真", size=(95, 30), )
        self.cont_tp.SetBackgroundColour('#E0EEEE')

        self.cont_fuc = wxBtn.GenButton(self.panel, -1, u"暂停仿真", size=(95, 30), )
        self.cont_fuc.SetBackgroundColour('#E0EEEE')

        inBox3.Add(self.cont_co, 0, wx.ALL | wx.EXPAND, 1)
        inBox3.Add(self.cont_sm, 0, wx.ALL | wx.EXPAND, 1)
        inBox3.Add(self.cont_tp, 0, wx.ALL | wx.EXPAND, 1)
        inBox3.Add(self.cont_fuc, 0, wx.ALL | wx.EXPAND, 1)

        # inBox2 = wx.BoxSizer(wx.HORIZONTAL)
        # inBox2.Add(tit_timeandfren, 0, wx.ALL | wx.EXPAND, 1)

        # self.btn_go = wxBtn.GenButton(self.panel, label=u"点击预览", size=(80, 30))
        # self.btn_go.Centre()
        # self.Bind(wx.EVT_BUTTON, self.DrawPic, self.btn_go)
        # inBox3.Add(self.btn_go, 0, wx.ALL | wx.EXPAND, 1)
        coSizer.Add(inBox1, 0, wx.ALL | wx.EXPAND, 1)
        coSizer.Add(inBox2, 0, wx.ALL | wx.CENTER, 5)
        coSizer.Add(inBox3, 0, wx.ALL | wx.CENTER, 1)

        #   画图部分
        # inBox4 = wx.BoxSizer(wx.HORIZONTAL)
        # scores = [89, 98, 70, 80, 60, 78, 85, 90]
        # sum = 0
        # for s in scores:
        #     sum += s
        # average = sum / len(scores)
        #
        # t_score = numpy.arange(1, len(scores) + 1, 1)
        # s_score = numpy.array(scores)
        #
        # self.figure_score = Figure()
        # self.figure_score.set_figheight(4.1)
        # self.figure_score.set_figwidth(8.0)
        # self.axes_score = self.figure_score.add_subplot(111)
        #
        # self.axes_score.plot(t_score, s_score, 'ro', t_score, s_score, 'k')
        # self.axes_score.axhline(y=average, color='r')
        # self.axes_score.grid(True)
        # self.axes_score.set_title(u'Please Input Parameter ')
        # self.axes_score.set_xlabel(u'Empty Now ')
        # self.axes_score.set_ylabel(u'Empty Now ')
        #
        # self.MyFig = FigureCanvas(self.panel, -1, self.figure_score)
        # inBox4.Add(self.MyFig, 0, wx.ALL | wx.EXPAND, 1)
        # coSizer.Add(inBox4, 0, wx.ALL | wx.CENTER, 5)
        #
        # self.btn_go = wxBtn.GenButton(self.panel, -1, size=(80, 30), label=u"确认生成")
        # self.Bind(wx.EVT_BUTTON, self.genData, self.btn_go)
        inBox5 = wx.BoxSizer(wx.HORIZONTAL)
        # inBox5.Add(self.btn_go, 0, wx.ALL | wx.CENTER, 5)
        coSizer.Add(inBox5, 0, wx.ALL | wx.CENTER, 1)

        # self.Bind(wx.EVT_BUTTON, self.btn_cb_co, self.btn_co_confirm)


        vbox.Add(coSizer, 0, wx.ALL | wx.EXPAND, 1)
        self.panel.SetSizer(vbox)
        self.Centre()

        pass







        #       左侧控制台输出部分pos=(5,10),pos=(10,27),pos=(95,690)

        #
        # self.out_con.SetBackgroundColour('#FFFAF0')
        # ssizer.Add(self.out_con, 0, wx.ALL | wx.EXPAND, 2)
        #


        # self.vboxSizer.Add(ssizer, 0, wx.ALL | wx.LEFT, 2)

        #       中央控制台输出部分
        # sb_center = wx.StaticBox()
        # fig = plt.figure()






        # sb_right = wx.StaticBox(self.panel, -1, u"仿真控制按钮:", pos=(925, 10), size=(270, 720))

        #

        # box_left = wx.StaticBox()

        # self.box_left = wx.StaticBox(self.panel,-1,'控制台输出')
        # self.box_center = wx.StaticBox(self.panel,-1,'仿真图形演示')
        # self.box_right = wx.StaticBox(self.panel,-1,'控制按钮')
        #
        # sizer_left = wx.StaticBoxSizer(self.box_left,wx.HORIZONTAL)
        # sizer_left.Add(label1,0, wx.ALL | wx.EXPAND,2)
        # sizer_center = wx.StaticBoxSizer(self.box_center,wx.HORIZONTAL)
        # sizer_center.Add(label2,0,wx.ALL | wx.EXPAND,2)
        # sizer_right = wx.StaticBoxSizer(self.box_right,wx.HORIZONTAL)
        # sizer_right.Add(label3,0, wx.ALL | wx.EXPAND ,2)
        #
        # vboxSizer.Add(self.box_left,0, wx.ALL | wx.EXPAND ,2)
        # vboxSizer.Add(self.box_center, 0, wx.ALL | wx.EXPAND, 2)

        #
        # # self.nm_a, 0, wx.ALL | wx.LEFT, 5

