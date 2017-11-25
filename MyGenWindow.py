#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : MyGenWindow.py
# @Author: He Peng
# @Date  : 2017/11/22
# @Desc  : 数据生成窗口

from MyPlotWindow import *

class MyGenWindow(wx.Frame):
    def __init__(self, parent=None, id=-1, title='', pos=wx.DefaultSize, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.InitUI()
        self.funcID = 0
        self.timeID = 0
        self.frenID = 0

        self.funcID_sm = 0
        self.timeID_sm = 0
        self.frenID_sm = 0

        self.funcID_tp = 0
        self.timeID_tp = 0
        self.frenID_tp = 0
        pass

    #   填充数据生成窗口组件
    def InitUI(self):
        self.pl_gen = wx.Panel(self)
        self.pl_gen.SetBackgroundColour('#F0F8FF')

        #  重型布局BoxSizer
        vbox = wx.BoxSizer(wx.VERTICAL)
        #########################################   CO浓度布局块    #######################################
        nm = wx.StaticBox(self.pl_gen, -1, 'CO浓度生成:')

        coSizer = wx.StaticBoxSizer(nm, wx.HORIZONTAL)   #   RadioButton的StataicSizer
        funcList = ['Y = aT + b', 'Y = aT + Rand(b~c)',u'正态分布']
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

        #########################################   烟雾浓度布局块    #######################################
        sm = wx.StaticBox(self.pl_gen, -1, '烟雾浓度生成:')

        smSizer = wx.StaticBoxSizer(sm, wx.HORIZONTAL)  # RadioButton的StataicSizer
        self.radio_func_sm = wx.RadioBox(self.pl_gen, -1, "数据生成函数", (10, 10), wx.DefaultSize,
                                      funcList, 3, wx.RA_SPECIFY_ROWS)
        self.radio_time_sm = wx.RadioBox(self.pl_gen, -1, "采样时间", (10, 10), wx.DefaultSize,
                                      timeList, 3, wx.RA_SPECIFY_ROWS)
        self.radio_fren_sm = wx.RadioBox(self.pl_gen, -1, "采样频率", (10, 10), wx.DefaultSize,
                                      frenList, 3, wx.RA_SPECIFY_ROWS)
        smSizer.Add(self.radio_func_sm, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        smSizer.Add(self.radio_time_sm, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        smSizer.Add(self.radio_fren_sm, 0, wx.ALL | wx.ALIGN_LEFT, 5)

        self.btn_sm_confirm = wxBtn.GenButton(self.pl_gen, label=u'预览&确认', size=(100, 20))
        self.btn_sm_confirm.SetBackgroundColour('#D2B48C')
        smSizer.Add(self.btn_sm_confirm, wx.ALL | wx.CENTER | wx.BOTTOM, 5)

        self.Bind(wx.EVT_RADIOBOX, self.getFuncID_sm, self.radio_func_sm)
        self.Bind(wx.EVT_RADIOBOX, self.getTimeID_sm, self.radio_time_sm)
        self.Bind(wx.EVT_RADIOBOX, self.getFrenID_sm, self.radio_fren_sm)

        self.Bind(wx.EVT_BUTTON, self.btn_cb_sm, self.btn_sm_confirm)

        #########################################   温度布局块    #######################################
        tp = wx.StaticBox(self.pl_gen, -1, '温度生成:')

        tpSizer = wx.StaticBoxSizer(tp, wx.HORIZONTAL)  # RadioButton的StataicSizer
        self.radio_func_tp = wx.RadioBox(self.pl_gen, -1, "数据生成函数", (10, 10), wx.DefaultSize,
                                         funcList, 3, wx.RA_SPECIFY_ROWS)
        self.radio_time_tp = wx.RadioBox(self.pl_gen, -1, "采样时间", (10, 10), wx.DefaultSize,
                                         timeList, 3, wx.RA_SPECIFY_ROWS)
        self.radio_fren_tp = wx.RadioBox(self.pl_gen, -1, "采样频率", (10, 10), wx.DefaultSize,
                                         frenList, 3, wx.RA_SPECIFY_ROWS)
        tpSizer.Add(self.radio_func_tp, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        tpSizer.Add(self.radio_time_tp, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        tpSizer.Add(self.radio_fren_tp, 0, wx.ALL | wx.ALIGN_LEFT, 5)

        self.btn_tp_confirm = wxBtn.GenButton(self.pl_gen, label=u'预览&确认', size=(100, 20))
        self.btn_tp_confirm.SetBackgroundColour('#D2B48C')
        tpSizer.Add(self.btn_tp_confirm, wx.ALL | wx.CENTER | wx.BOTTOM, 5)

        self.Bind(wx.EVT_RADIOBOX, self.getFuncID_tp, self.radio_func_tp)
        self.Bind(wx.EVT_RADIOBOX, self.getTimeID_tp, self.radio_time_tp)
        self.Bind(wx.EVT_RADIOBOX, self.getFrenID_tp, self.radio_fren_tp)

        self.Bind(wx.EVT_BUTTON, self.btn_cb_tp, self.btn_tp_confirm)


        vbox.Add(coSizer, 0, wx.ALL | wx.EXPAND, 5)
        vbox.Add(smSizer, 0, wx.ALL | wx.EXPAND, 5)
        vbox.Add(tpSizer, 0, wx.ALL | wx.EXPAND, 5)
        # vbox.Add(viSizer, 0, wx.ALL | wx.EXPAND, 5)
        self.pl_gen.SetSizer(vbox)
        self.Centre()

    pass
    ###############        绑定CO的Buttons点击事件        #############
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
                               funcFlag=self.funcID,timeFlag=self.timeID,frenFlag=self.frenID,genFlag=0)
        self.genPlot.Center()
        self.genPlot.Show(True)
        pass

    ###############        绑定烟雾浓度的Buttons点击事件        #############
    def getFuncID_sm(self,handle):
        self.funcID_sm = self.radio_func_sm.GetSelection()
        print("选择的functionID为"+str(self.funcID_sm))
        pass
    def getTimeID_sm(self,handle):
        self.timeID_sm = self.radio_time_sm.GetSelection()
        print("选择的timeID为"+str(self.timeID_sm))
        pass
    def getFrenID_sm(self,handle):
        self.frenID_sm = self.radio_fren_sm.GetSelection()
        print("选择的frencyID为"+str(self.frenID_sm))
        pass
    def btn_cb_sm(self, handle):
        print('创建数据生预览窗口')
        self.genPlot = MyPlotWindow(self, id=-1, title=u'综合管廊火灾仿真---数据生成', pos=(10, 10),
                                    size=(500, 600), style=wx.DEFAULT_FRAME_STYLE,
                                    funcFlag=self.funcID_sm, timeFlag=self.timeID_sm, frenFlag=self.frenID_sm, genFlag=1)
        self.genPlot.Center()
        self.genPlot.Show(True)
        pass

    ###############        绑定温度数据的Buttons点击事件        #############
    def getFuncID_tp(self, handle):
        self.funcID_tp = self.radio_func_tp.GetSelection()
        print("选择的functionID为" + str(self.funcID_tp))
        pass

    def getTimeID_tp(self, handle):
        self.timeID_tp = self.radio_time_tp.GetSelection()
        print("选择的timeID为" + str(self.timeID_tp))
        pass

    def getFrenID_tp(self, handle):
        self.frenID_tp = self.radio_fren_tp.GetSelection()
        print("选择的frencyID为" + str(self.frenID_tp))
        pass

    def btn_cb_tp(self, handle):
        print('创建数据生预览窗口')
        self.genPlot = MyPlotWindow(self, id=-1, title=u'综合管廊火灾仿真---数据生成', pos=(10, 10),
                                    size=(500, 600), style=wx.DEFAULT_FRAME_STYLE,
                                    funcFlag=self.funcID_tp, timeFlag=self.timeID_tp, frenFlag=self.frenID_tp,
                                    genFlag=2)
        self.genPlot.Center()
        self.genPlot.Show(True)
        pass
    #