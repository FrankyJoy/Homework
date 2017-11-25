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
import random
import scipy.stats
import MysqlCon


class MyPlotWindow(wx.Frame):
    def __init__(self,parent=None,id=-1,title='',pos=wx.DefaultSize,
                 size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE,
                 funcFlag=0,timeFlag=0,frenFlag=0,genFlag=0):
        wx.Frame.__init__(self , parent ,id,title, pos, size, style)
        self.funcFlag = funcFlag
        self.timeFlag = timeFlag
        self.frenFlag = frenFlag
        self.genFlag = genFlag
        self.tlist = []
        self.ylist = []

        print(self.funcFlag+self.timeFlag+self.frenFlag)
        self.InitUI()
        pass

    def InitUI(self):

        if self.genFlag == 0:               #   生成CO数据
            self.SetTitle('CO数据生成预览')
        elif self.genFlag == 1 :
            self.SetTitle('烟雾浓度生成预览')
        elif self.genFlag == 2:
            self.SetTitle('温度生成预览')
        else:
            print('参数错误！！！')

        self.SetBackgroundColour('#FFF5EE')
        self.panel = wx.Panel(self)

        self.nm_a = wx.TextCtrl()
        self.nm_b = wx.TextCtrl()
        self.nm_c = wx.TextCtrl()

        self.time = 0
        self.fren = 0


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
            self.nm_a = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            self.nm_a.SetValue('0')
            txt_a = wx.StaticText(self.panel, -1, u"输入参数 a", style=wx.ALIGN_RIGHT)
            self.nm_b = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_b = wx.StaticText(self.panel, -1, u"输入参数 b", style=wx.ALIGN_RIGHT)
            self.nm_b.SetValue('0')

            inBox1.Add(tit_func, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_func, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_a, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(self.nm_a, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_b, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(self.nm_b, 0, wx.ALL | wx.LEFT, 5)
        elif self.funcFlag == 1:
            txt_func = "Y = aT + Rand(b~c)   | "
            txt_func = wx.StaticText(self.panel, -1, txt_func, style=wx.ALIGN_LEFT)
            self.nm_a = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_a = wx.StaticText(self.panel, -1, u"输入参数 a", style=wx.ALIGN_RIGHT)
            self.nm_b = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_b = wx.StaticText(self.panel, -1, u"b", style=wx.ALIGN_RIGHT)
            self.nm_c = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_c = wx.StaticText(self.panel, -1, u"c", style=wx.ALIGN_RIGHT)
            self.nm_a.SetValue('0')
            self.nm_b.SetValue('0')
            self.nm_c.SetValue('0')

            inBox1.Add(tit_func, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_func, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_a, 0, wx.ALL | wx.LEFT, 2)
            inBox1.Add(self.nm_a, 0, wx.ALL | wx.LEFT, 2)
            inBox1.Add(txt_b, 0, wx.ALL | wx.LEFT, 2)
            inBox1.Add(self.nm_b, 0, wx.ALL | wx.LEFT, 2)
            inBox1.Add(txt_c, 0, wx.ALL | wx.LEFT, 2)
            inBox1.Add(self.nm_c, 0, wx.ALL | wx.LEFT, 2)
        elif self.funcFlag == 2:
            txt_func = u"正态分布     | "
            txt_func = wx.StaticText(self.panel, -1, txt_func, style=wx.ALIGN_LEFT)
            self.nm_a = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_a = wx.StaticText(self.panel, -1, u"输入期望μ", style=wx.ALIGN_RIGHT)
            self.nm_b = wx.TextCtrl(self.panel, -1, size=(40, 20), style=wx.ALIGN_RIGHT)
            txt_b = wx.StaticText(self.panel, -1, u"输入标准差σ", style=wx.ALIGN_RIGHT)

            self.nm_a.SetValue('0')
            self.nm_b.SetValue('0')
            inBox1.Add(tit_func, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_func, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_a, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(self.nm_a, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(txt_b, 0, wx.ALL | wx.LEFT, 5)
            inBox1.Add(self.nm_b, 0, wx.ALL | wx.LEFT, 5)

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
        self.Bind(wx.EVT_BUTTON, self.DrawPic, self.btn_go)
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
        inBox4.Add(self.MyFig ,0,wx.ALL | wx.EXPAND,1)
        coSizer.Add(inBox4, 0, wx.ALL | wx.CENTER, 5)

        self.btn_go = wxBtn.GenButton(self.panel,-1,size=(80,30),label=u"确认生成")
        self.Bind(wx.EVT_BUTTON, self.genData, self.btn_go)
        inBox5 = wx.BoxSizer(wx.HORIZONTAL)
        inBox5.Add(self.btn_go,0,wx.ALL | wx.CENTER,5)
        coSizer.Add(inBox5,0,wx.ALL | wx.CENTER,1)

        # self.Bind(wx.EVT_BUTTON, self.btn_cb_co, self.btn_co_confirm)
        vbox.Add(coSizer, 0, wx.ALL | wx.EXPAND, 1)
        self.panel.SetSizer(vbox)
        self.Centre()

        pass

    def DrawPic(self,handler):
        print('run into DrawPic Func')
        self.axes_score.clear()
        self.ylist = []
        self.tlist = []
        #   确定图形标题 及横纵轴
        if self.genFlag == 0:
            self.axes_score.set_title(u'CO Data Curve')
            self.axes_score.set_xlabel(u't  Second')
            self.axes_score.set_ylabel(u'unKnow')
            pass
        elif self.genFlag == 1:
            self.axes_score.set_title(u'Smoke concentration Data Curve')
            self.axes_score.set_xlabel(u't  秒')
            self.axes_score.set_ylabel(u'unKnow')
            pass
        elif self.genFlag == 2:
            self.axes_score.set_title(u'Temperature Data Curve')
            self.axes_score.set_xlabel(u't second')
            self.axes_score.set_ylabel(u'unKnow')
            pass
        else:
            print("DrawPic Error")
            pass

        if self.timeFlag == 0:
            self.time = 30
            pass
        elif self.timeFlag == 1:
            self.time = 60
            pass
        elif self.timeFlag == 2 :
            self.time = 120
            pass
        else:
            print("DrawPic Error")
            pass

        if self.frenFlag == 0:
            self.fren = 1
            pass
        elif self.frenFlag == 1:
            self.fren = 2
            pass
        elif self.frenFlag == 2 :
            self.fren = 4
            pass
        else:
            print("DrawPic Error")
            pass

        #   生成数据
        if self.funcFlag == 0:      #y = at +b
            par_a,par_b = self._getPar()
            self.tlist = numpy.arange(0,self.time+(1 / self.fren),(1/self.fren))   # X 轴
            for x in self.tlist:
                self.ylist.append(par_a * x + par_b)
            print(self.ylist)
            pass
        elif self.funcFlag == 1:
            par_a, par_b, par_c = self._getPar()
            self.tlist = numpy.arange(0, self.time+(1 / self.fren), (1 / self.fren))  # X 轴
            random = numpy.random.RandomState(0)
            for x in self.tlist:
                self.ylist.append(par_a * x + (random.uniform(par_b,par_c)))
            print(self.ylist)
            # #####float('%.2f' % a)
            pass
        elif self.funcFlag == 2 :
            par_a, par_b = self._getPar()
            if par_a == 0:
                wx.MessageBox("输入的期望不能为0","正态分布参数错误",wx.OK | wx.ICON_INFORMATION)
                return None
            self.tlist = numpy.arange(0, self.time+(1 / self.fren), (1 / self.fren))  # X 轴
            for x in self.tlist:
                self.ylist.append(scipy.stats.norm.pdf(x,par_a,par_b))
            print(self.ylist)
            #   正态分布 函数
            # #####
            pass
        else:
            print("DrawPic Error")
            pass
        self.axes_score.plot(self.tlist, self.ylist, 'c^', self.tlist, self.ylist, 'k')
        self.axes_score.grid(True)
        self.MyFig.draw()
        pass

    #   判断数据是不是数字
    def _isNum(self,value):
        try:
            float(value)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(value)
            return True
        except (TypeError, ValueError):
            pass
        return False

    #   从输入框获取参数
    def _getPar(self):
        if self.funcFlag == 0 or self.funcFlag == 2:
            if self.nm_a.GetValue == '' or self.nm_b.GetValue() == '':
                wx.MessageBox("输入参数不全，请重新输入", "警告，参数不全！", wx.OK | wx.ICON_INFORMATION)
                return 0,0
            else:
                par_a = self.nm_a.GetValue()
                par_b = self.nm_b.GetValue()
                if not(self._isNum(par_a) and self._isNum(par_b)):
                    wx.MessageBox("参数应输入数字，请重新输入", "警告，参数错误！", wx.OK | wx.ICON_INFORMATION)
                    return 0,0
                else :
                    par_a = float(par_a)
                    par_b = float(par_b)
                    return par_a,par_b
        elif self.funcFlag == 1:
            if self.nm_a.GetValue == '' or self.nm_b.GetValue == '' or self.nm_c.GetValue == '':
                wx.MessageBox("输入参数不全，请重新输入", "警告，参数不全！", wx.OK | wx.ICON_INFORMATION)
                return 0,0,0
            else:
                par_a = self.nm_a.GetValue()
                par_b = self.nm_b.GetValue()
                par_c = self.nm_c.GetValue()
                if not (self._isNum(par_a) and self._isNum(par_b) and self._isNum(par_c)):
                    wx.MessageBox("参数应输入数字，请重新输入", "警告，参数错误！", wx.OK | wx.ICON_INFORMATION)
                    return 0,0,0
                else:
                    par_a = float(par_a)
                    par_b = float(par_b)
                    par_c = float(par_c)
                    return par_a, par_b,par_c
        else:
            wx.MessageBox("输入框取值错误", "ERROR！", wx.OK | wx.ICON_INFORMATION)

    #   确认生成按钮
    def genData(self,handler):
        if self.genFlag == 0:       #  CO数据生成
            MysqlCon.fillCoTable(self.ylist,self.time,self.fren,"CO_Data")
            wx.MessageBox("恭喜，数据生成成功，已存入数据库！","成功",wx.OK | wx.ICON_INFORMATION)
        elif self.genFlag == 1:
            MysqlCon.fillCoTable(self.ylist, self.time, self.fren, "SM_Data")
            wx.MessageBox("恭喜，数据生成成功，已存入数据库！", "成功", wx.OK | wx.ICON_INFORMATION)
        elif self.genFlag == 2:
            MysqlCon.fillCoTable(self.ylist, self.time, self.fren, "TP_Data")
            wx.MessageBox("恭喜，数据生成成功，已存入数据库！", "成功", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("参数错误，生成失败", "失败！", wx.OK | wx.ICON_INFORMATION)
        pass