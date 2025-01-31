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
from MyObject import *
import MysqlCon

class MySimWindow(wx.Frame):
    def __init__(self, parent=None, id=-1, title='', pos=wx.DefaultSize, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.InitUI()
        pass

    def InitUI(self):
        #   声明Panel，改变背景色
        self.SetBackgroundColour('#FFF5EE')
        self.panel = wx.Panel(self)
        #   布局块
        vbox = wx.BoxSizer(wx.HORIZONTAL)
        nm = wx.StaticBox(self.panel, -1, '控制台输出:')
        sizer_left = wx.StaticBoxSizer(nm, wx.HORIZONTAL)

        nm_center = wx.StaticBox(self.panel, -1, '仿真绘图窗口:')
        sizer_center = wx.StaticBoxSizer(nm_center, wx.HORIZONTAL)

        nm_right = wx.StaticBox(self.panel, -1, '仿真控制按钮:')
        sizer_right = wx.StaticBoxSizer(nm_right, wx.HORIZONTAL)
        #   左侧控制台输出
        inBox1 = wx.BoxSizer(wx.VERTICAL)

        self.outInfo = wx.TextCtrl(self.panel, value = "当前未开始仿真",
                                   style = wx.TE_READONLY|wx.TE_LEFT,size=(210,660))
        self.out_save = wxBtn.GenButton(self.panel,-1,u"清空控制台输出",size=(95,30),)
        self.out_save.SetBackgroundColour('#E0EEEE')
        inBox1.Add(self.outInfo, 0, wx.ALL | wx.CENTER, 1)
        inBox1.Add(self.out_save, 0, wx.ALL | wx.CENTER, 1)
        sizer_left.Add(inBox1, 0, wx.ALL | wx.EXPAND, 0)

        #   中部绘图窗口
        inBox2 = wx.BoxSizer(wx.VERTICAL)
        scores = [89, 98, 70, 80, 60, 78, 85, 90]
        sum = 0
        for s in scores:
            sum += s
        average = sum / len(scores)

        t_score = numpy.arange(1, len(scores) + 1, 1)
        s_score = numpy.array(scores)

        self.figure_map = Figure()
        self.figure_map.set_figheight(6.7)
        self.figure_map.set_figwidth(8)

        # self.sub_co = self.subplots()
        self.axes_co = self.figure_map.add_subplot(221)
        self.axes_sm = self.figure_map.add_subplot(222)
        self.axes_tp = self.figure_map.add_subplot(223)
        self.axes_cal = self.figure_map.add_subplot(224)

        self.axes_co.plot(t_score, s_score, 'ro', t_score, s_score, 'k')
        self.axes_co.axhline(y=average, color='r')
        self.axes_co.grid(True)
        self.axes_co.set_title(u'Please Input Parameter -- CO')
        self.axes_co.set_ylabel(u'Empty Now ')
        # self.axes_co.set_major_locator()

        self.axes_sm.plot(t_score, s_score, 'ro', t_score, s_score, 'k')
        self.axes_sm.axhline(y=average, color='r')
        self.axes_sm.grid(True)
        self.axes_sm.set_title(u'Please Input Parameter -- sm')
        self.axes_sm.set_ylabel(u'Empty Now ')

        self.axes_tp.plot(t_score, s_score, 'ro', t_score, s_score, 'k')
        self.axes_tp.axhline(y=average, color='r')
        self.axes_tp.grid(True)
        self.axes_tp.set_title(u'Please Input Parameter -- tp')
        self.axes_tp.set_xlabel(u'Empty Now ')
        self.axes_tp.set_ylabel(u'Empty Now ')

        self.axes_cal.plot(t_score, s_score, 'ro', t_score, s_score, 'k')
        self.axes_cal.axhline(y=average, color='r')
        self.axes_cal.grid(True)
        self.axes_cal.set_title(u'Please Input Parameter --cal')
        self.axes_cal.set_xlabel(u'Empty Now ')
        self.axes_cal.set_ylabel(u'Empty Now ')

        self.MyFig = FigureCanvas(self.panel, -1, self.figure_map)
        inBox2.Add(self.MyFig, 0, wx.ALL | wx.EXPAND, 1)
        self.out_save = wxBtn.GenButton(self.panel, -1, u"暂停仿真", size=(95, 30), )
        self.out_save.SetBackgroundColour('#E0EEEE')
        inBox2.Add(self.out_save, 0, wx.ALL | wx.CENTER, 1)
        sizer_center.Add(inBox2, 0, wx.ALL | wx.CENTER, 0)


        #   右侧控制按钮
        sampleList = MysqlCon.getListOfTable('testDb')
        inBox3 = wx.BoxSizer(wx.VERTICAL)
        load_co_txt = wx.StaticText(self.panel,-1,"CO数据表选择")
        self.dwlist_co =  wx.Choice(self.panel, -1, (85, 18), choices=sampleList)
        self.dwlist_co.SetSelection(0)

        load_sm_txt = wx.StaticText(self.panel, -1, "烟雾浓度数据表选择")
        self.dwlist_sm = wx.Choice(self.panel, -1, (85, 18), choices=sampleList)
        self.dwlist_sm.SetSelection(1)

        load_tp_txt = wx.StaticText(self.panel, -1, "温度数据表选择")
        self.dwlist_tp = wx.Choice(self.panel, -1, (85, 18), choices=sampleList)
        self.dwlist_tp.SetSelection(2)

        self.btn_setData = wxBtn.GenButton(self.panel, -1, u"读取数据", size=(95, 30), )
        self.btn_setData.SetBackgroundColour('#E0EEEE')
        self.Bind(wx.EVT_BUTTON,self.btn_setData_cb,self.btn_setData)



        inBox3.Add(load_co_txt, 0, wx.ALL | wx.CENTER, 1)
        inBox3.Add(self.dwlist_co, 0, wx.ALL | wx.CENTER, 1)

        inBox3.Add(load_sm_txt, 0, wx.ALL | wx.CENTER, 1)
        inBox3.Add(self.dwlist_sm, 0, wx.ALL | wx.CENTER, 1)

        inBox3.Add(load_tp_txt, 0, wx.ALL | wx.CENTER, 1)
        inBox3.Add(self.dwlist_tp, 0, wx.ALL | wx.CENTER, 1)

        inBox3.Add(self.btn_setData, 0, wx.ALL | wx.EXPAND, 15)

        funcList = ['功能测试用','D-S数据融合','RBF神经网络']
        load_tp_fuc = wx.StaticText(self.panel, -1, "数据融合方法选择")
        self.dwlist_fuc = wx.Choice(self.panel, -1, (85, 18), choices=funcList)
        self.cont_fuc = wxBtn.GenButton(self.panel, -1, u"开始仿真", size=(95, 30), )
        self.cont_fuc.SetBackgroundColour('#E0EEEE')
        inBox3.Add(load_tp_fuc, 0, wx.ALL | wx.CENTER, 1)
        inBox3.Add(self.dwlist_fuc, 0, wx.ALL | wx.CENTER, 1)
        inBox3.Add(self.cont_fuc, 0, wx.ALL | wx.EXPAND, 1)

        sizer_right.Add(inBox3, 0, wx.ALL | wx.CENTER, 1)

        # self.btn_go = wxBtn.GenButton(self.panel, label=u"点击预览", size=(80, 30))
        # self.btn_go.Centre()
        # self.Bind(wx.EVT_BUTTON, self.DrawPic, self.btn_go)
        # inBox3.Add(self.btn_go, 0, wx.ALL | wx.EXPAND, 1)


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
        # self.figure_map = Figure()
        # self.figure_map.set_figheight(4.1)
        # self.figure_map.set_figwidth(8.0)
        # self.axes_cal = self.figure_map.add_subplot(111)
        #
        # self.axes_cal.plot(t_score, s_score, 'ro', t_score, s_score, 'k')
        # self.axes_cal.axhline(y=average, color='r')
        # self.axes_cal.grid(True)
        # self.axes_cal.set_title(u'Please Input Parameter ')
        # self.axes_cal.set_xlabel(u'Empty Now ')
        # self.axes_cal.set_ylabel(u'Empty Now ')
        #
        # self.MyFig = FigureCanvas(self.panel, -1, self.figure_map)
        # inBox4.Add(self.MyFig, 0, wx.ALL | wx.EXPAND, 1)
        # sizer_left.Add(inBox4, 0, wx.ALL | wx.CENTER, 5)
        #
        # self.btn_go = wxBtn.GenButton(self.panel, -1, size=(80, 30), label=u"确认生成")
        # self.Bind(wx.EVT_BUTTON, self.genData, self.btn_go)
        # inBox5 = wx.BoxSizer(wx.HORIZONTAL)
        # inBox5.Add(self.btn_go, 0, wx.ALL | wx.CENTER, 5)
        # sizer_left.Add(inBox5, 0, wx.ALL | wx.CENTER, 1)

        # self.Bind(wx.EVT_BUTTON, self.btn_cb_co, self.btn_co_confirm)


        vbox.Add(sizer_left, 0, wx.ALL | wx.LEFT, 1)
        vbox.Add(sizer_center, 0, wx.ALL | wx.CENTER, 1)
        vbox.Add(sizer_right, 0, wx.ALL | wx.RIGHT, 1)
        self.panel.SetSizer(vbox)
        # self.Fit()  有此函数会缩成一团！！！
        self.Centre()

        pass

    #       读取数据按钮的回调函数
    def btn_setData_cb(self,handler):
        tb_data_co = self.dwlist_co.GetStringSelection()
        tb_data_sm = self.dwlist_sm.GetStringSelection()
        tb_data_tp = self.dwlist_tp.GetStringSelection()
        tb_data_fuc = self.dwlist_fuc.GetStringSelection()

        self.data_co = MysqlCon.getDataOfTable("testDb", tb_data_co)
        self.data_sm = MysqlCon.getDataOfTable("testDb", tb_data_sm)
        self.data_tp = MysqlCon.getDataOfTable("testDb", tb_data_tp)

        #        需要补充异常情况判断      ？？？
        #        获取数据表时间和频率\长度
        time_co = self.data_co[0].time
        time_sm = self.data_sm[0].time
        time_tp = self.data_tp[0].time

        fren_co = self.data_co[0].fren
        fren_sm = self.data_sm[0].fren
        fren_tp = self.data_tp[0].fren

        len_co = len(self.data_co)
        len_sm = len(self.data_sm)
        len_tp = len(self.data_tp)

        axes_x_co = []
        axes_x_sm = []
        axes_x_tp = []
        axes_y_co = []
        axes_y_sm = []
        axes_y_tp = []


        temp = 1
        for row in self.data_co:
            axes_x_co.append(temp*(1/fren_co))
            axes_y_co.append(row.value)
            temp = temp + 1
            pass
        self.axes_co.clear()
        self.axes_co.plot(axes_x_co, axes_y_co, 'ro', axes_x_co, axes_y_co, 'k')
        self.axes_co.grid(True)
        self.axes_co.set_title(u'CO Data Is Ready!')
        self.axes_co.set_ylabel(u'??!!## ')

        for row in self.data_sm:
            axes_x_sm.append(temp*(1/fren_sm))
            axes_y_sm.append(row.value)
            temp = temp + 1
            pass
        self.axes_sm.clear()
        self.axes_sm.plot(axes_x_sm, axes_y_sm, 'ro', axes_x_sm, axes_y_sm, 'k')
        self.axes_sm.grid(True)
        self.axes_sm.set_title(u'Smoke Data Is Ready!')
        self.axes_sm.set_ylabel(u'??!!## ')

        for row in self.data_tp:
            axes_x_tp.append(temp*(1/fren_tp))
            axes_y_tp.append(row.value)
            temp = temp + 1
            pass
        self.axes_tp.clear()
        self.axes_tp.plot(axes_x_tp, axes_y_tp, 'ro', axes_x_tp, axes_y_tp, 'k')
        self.axes_tp.grid(True)
        self.axes_tp.set_title(u'Temperature Data Is Ready!')
        self.axes_tp.set_ylabel(u'??!!## ')
        self.MyFig.draw()
        pass

    #       开始仿真按钮
    def btn_beginSim_cb(self,handler):
        # 暂时只实现以1秒为单位的动态演示
        # 之后实现 以加权平均为方法的数据融合图形展示
        # 之后实现，对仿真过程的控制
        
        pass



    #   dropdownList 按钮变化后的效果
    def dwlist_cb_co(self):
        pass
    def dwlist_cb_sm(self):
        pass
    def dwlist_cb_tp(self):
        pass
    def dwlist_cb_fuc(self):
        pass
