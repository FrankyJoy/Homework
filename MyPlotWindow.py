#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : MyPlotWindow.py
# @Author: He Peng
# @Date  : 2017/11/22
# @Desc  : 数据生成窗口--预览绘图

import wx as wx
import wx.lib.buttons as wxBtn
import numpy
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure


class MyPlotWindow(wx.Frame):
    def __init__(self,parent=None,id=-1,title='',pos=wx.DefaultSize,
                 size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE,
                 funcFlag=0,timeFlag=0,frenFlag=0,genFlag=0):
        wx.Frame.__init__(self , parent ,id,title, pos, size, style)
        self.funcFlag = funcFlag
        self.timeFlag = timeFlag
        self.frenFlag = frenFlag
        self.genFlag = genFlag
        print(self.funcFlag+self.timeFlag+self.frenFlag)
        self.InitUI()
        pass

    def InitUI(self):

        if self.genFlag == 0:               #   生成CO数据
            self.SetTitle('CO数据生成预览')
        elif self.genFlag == 1 :
            self.SetTitle('采样时间生成预览')
        elif self.genFlag == 2:
            self.SetTitle('采样频率生成预览')
        else:
            print('参数错误！！！')

        self.SetBackgroundColour('#FFF5EE')
        self.panel = wx.Panel(self)

        #  重型布局BoxSizer
        vbox = wx.BoxSizer(wx.VERTICAL)
        #   CO浓度布局块
        nm = wx.StaticBox(self.panel, -1, '参数确认与补全 :')
        coSizer = wx.StaticBoxSizer(nm, wx.VERTICAL)  # RadioButton的StataicSizer

        inBox1 = wx.BoxSizer(wx.HORIZONTAL)
        tit_func = wx.StaticText(self.panel,-1,"生成函数 ：",style = wx.ALIGN_LEFT)

        if self.funcFlag == 0:
            txt_func = "Y = aT + b    |"
            txt_func = wx.StaticText(self.panel, -1, txt_func, style=wx.ALIGN_LEFT)
            nm_a = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_a = wx.StaticText(self.panel, -1, u"输入参数 a", style=wx.ALIGN_RIGHT)
            nm_b = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_b = wx.StaticText(self.panel, -1, u"输入参数 b", style=wx.ALIGN_RIGHT)

            inBox1.Add(tit_func, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_func, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_a, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(nm_a, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_b, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(nm_b, 0, wx.ALL | wx.LEFT, 5)
        elif self.funcFlag == 1:
            txt_func = "Y = aT + Rand(b~c)   | "
            txt_func = wx.StaticText(self.panel, -1, txt_func, style=wx.ALIGN_LEFT)
            nm_a = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_a = wx.StaticText(self.panel, -1, u"输入参数 a", style=wx.ALIGN_RIGHT)
            nm_b = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_b = wx.StaticText(self.panel, -1, u"b", style=wx.ALIGN_RIGHT)
            nm_c = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_c = wx.StaticText(self.panel, -1, u"c", style=wx.ALIGN_RIGHT)

            inBox1.Add(tit_func, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_func, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_a, 0, wx.ALL | wx.LEFT, 2)
            inBox1.Add(nm_a, 0, wx.ALL | wx.LEFT, 2)
            inBox1.Add(txt_b, 0, wx.ALL | wx.LEFT, 2)
            inBox1.Add(nm_b, 0, wx.ALL | wx.LEFT, 2)
            inBox1.Add(txt_c, 0, wx.ALL | wx.LEFT, 2)
            inBox1.Add(nm_c, 0, wx.ALL | wx.LEFT, 2)
        elif self.funcFlag == 2:
            txt_func = u"正态分布     | "
            txt_func = wx.StaticText(self.panel, -1, txt_func, style=wx.ALIGN_LEFT)
            nm_a = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_a = wx.StaticText(self.panel, -1, u"输入期望μ", style=wx.ALIGN_RIGHT)
            nm_b = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_b = wx.StaticText(self.panel, -1, u"输入标准差σ", style=wx.ALIGN_RIGHT)

            inBox1.Add(tit_func, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_func, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_a, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(nm_a, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_b, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(nm_b, 0, wx.ALL | wx.LEFT, 5)

        else:
            print("参数错误")

        if self.timeFlag == 0:
            txt_time = u"30 秒            |"
        elif self.timeFlag == 1:
            txt_time = u"60 秒            |"
        elif self.timeFlag == 2:
            txt_time = u"120 秒           |"
        else:
            txt_time = u"Error！"

        if self.frenFlag == 0:
            txt_fren = u"1 次/秒"
        elif self.frenFlag == 1:
            txt_fren = u"2 次/秒"
        elif self.frenFlag == 2:
            txt_fren = u"4 次/秒"
        else:
            txt_fren = u"Error!"

        tit_time = u" 采样时间:       "
        tit_fren = u"采样频率:       "
        txt = tit_time + txt_time + "    " + tit_fren + txt_fren
        tit_timeandfren = wx.StaticText(self.panel, -1, txt, style=wx.ALIGN_LEFT)

        inBox2 = wx.BoxSizer(wx.HORIZONTAL)
        inBox2.Add(tit_timeandfren, 0, wx.ALL|wx.EXPAND ,1)
        inBox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_go = wxBtn.GenButton(self.panel,label=u"点击预览",size=(80,30))
        self.btn_go.Centre()
        inBox3.Add(self.btn_go,0,wx.ALL|wx.EXPAND,1)
        coSizer.Add(inBox1,0,wx.ALL|wx.EXPAND,1)
        coSizer.Add(inBox2,0,wx.ALL|wx.EXPAND,1)
        coSizer.Add(inBox3,0,wx.ALL|wx.CENTER,1)

        #   画图部分
        inBox4 = wx.BoxSizer(wx.HORIZONTAL)
        scores = [89, 98, 70, 80, 60, 78, 85, 90]
        sum = 0
        for s in scores:
            sum += s
        average = sum / len(scores)

        t_score = numpy.arange(1, len(scores) + 1, 1)
        s_score = numpy.array(scores)

        self.figure_score = Figure()
        self.figure_score.set_figheight(3.6)
        self.figure_score.set_figwidth(7.8)
        self.axes_score = self.figure_score.add_subplot(111)

        self.axes_score.plot(t_score, s_score, 'ro', t_score, s_score, 'k')
        self.axes_score.axhline(y=average, color='r')
        self.axes_score.set_title(u'My Scores')
        self.axes_score.grid(True)
        self.axes_score.set_xlabel('T')
        self.axes_score.set_ylabel('score')
        self.MyFig = FigureCanvas(self.panel, -1, self.figure_score)
        inBox4.Add(self.MyFig ,0,wx.ALL | wx.EXPAND,1)
        coSizer.Add(inBox4, 0, wx.ALL | wx.CENTER, 5)

        #
        # self.btn_co_confirm = wxBtn.GenButton(self.pl_gen, label=u'预览&确认', size=(100, 20))
        # self.btn_co_confirm.SetBackgroundColour('#D2B48C')
        # coSizer.Add(self.btn_co_confirm, wx.ALL | wx.CENTER | wx.BOTTOM, 5)
        #
        # self.Bind(wx.EVT_RADIOBOX, self.getFuncID, self.radio_func)
        # self.Bind(wx.EVT_RADIOBOX, self.getTimeID, self.radio_time)
        # self.Bind(wx.EVT_RADIOBOX, self.getFrenID, self.radio_fren)
        #
        # self.Bind(wx.EVT_BUTTON, self.btn_cb_co, self.btn_co_confirm)
        vbox.Add(coSizer, 0, wx.ALL | wx.EXPAND, 5)
        # vbox.Add(viSizer, 0, wx.ALL | wx.EXPAND, 5)
        self.panel.SetSizer(vbox)
        self.Centre()

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
        # self.figure_score.set_figheight(3.6)
        # self.figure_score.set_figwidth(7.8)
        # self.axes_score = self.figure_score.add_subplot(111)
        #
        # self.axes_score.plot(t_score, s_score, 'ro', t_score, s_score, 'k')
        # self.axes_score.axhline(y=average, color='r')
        # self.axes_score.set_title(u'My Scores')
        # self.axes_score.grid(True)
        # self.axes_score.set_xlabel('T')
        # self.axes_score.set_ylabel('score')
        # FigureCanvas(self.scorePanel, -1, self.figure_score)
        pass