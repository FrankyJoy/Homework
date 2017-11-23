#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : MyPlotWindow.py
# @Author: He Peng
# @Date  : 2017/11/22
# @Desc  : 数据生成窗口--预览绘图

import wx as wx
import numpy
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure


class MyPlotWindow(wx.Frame):
    def __init__(self,parent=None,id=-1,title='',pos=wx.DefaultSize,
                 size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE,
                 funcFlag=0,timeFlag=0,frenFlag=0):
        wx.Frame.__init__(self , parent ,id,title, pos, size, style)
        self.funcFlag = funcFlag
        self.timeFlag = timeFlag
        self.frenFlag = frenFlag
        print(self.funcFlag+self.timeFlag+self.frenFlag)
        self.InitUI()
        pass

    def InitUI(self):
        self.SetBackgroundColour('#FFF5EE')
        self.scorePanel = wx.Panel(self)
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
        FigureCanvas(self.scorePanel, -1, self.figure_score)
        pass