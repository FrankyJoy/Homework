#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : MainGui.py
# @Author: He Peng
# @Date  : 2017/11/22
# @Desc  :


from  MyGenWindow import *
import PyGenerateData as PyGen

'''
        创建仿真程序住窗口
'''
class MyMainWindow(wx.Frame):
    def __init__(self,parent=None,id=-1,title='',pos=wx.DefaultSize, size=wx.DefaultSize, style= wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.InitUI()
        pass

    def InitUI(self):
        Mainpanel = wx.Panel(self)
        Mainpanel.SetBackgroundColour('#E0EEE0')
        btn_gen = wxBtn.GenButton(Mainpanel, label = u'生成数据', pos = (200, 112), size = (100, 50))
        btn_gen.SetBackgroundColour('#D2B48C')
        self.Bind(wx.EVT_BUTTON,self.GenWindow,btn_gen)

        btn_sim = wxBtn.GenButton(Mainpanel, label = u'开始仿真', pos = (200, 224), size = (100, 50))
        btn_sim.SetBackgroundColour('#CD6889')
        self.Bind(wx.EVT_BUTTON, self.SimWindow, btn_sim)

        btn_exit = wxBtn.GenButton(Mainpanel,label = u'退出程序', pos = (200, 400), size = (100, 50))
        btn_exit.SetBackgroundColour('#FF4040')
        self.Bind(wx.EVT_BUTTON,self.CloseWin,btn_exit)
        pass

    #   生成数据窗口
    def GenWindow(self,handler):
        #   获取屏幕分辨率，计算使窗口居中
        scnWidth, scnHeight = wx.DisplaySize()
        winWidth = 500
        winHeight = 600
        posX = (scnWidth - winWidth) / 2
        posY = (scnHeight - winHeight) / 2
        style = wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX
        genframe = MyGenWindow(self,id=-1, title=u'综合管廊火灾仿真---数据生成', pos=(posX, posY),
                               size=(winWidth, winHeight), style=style)
        genframe.Show(True)
        return True
        pass

    #   仿真窗口
    def SimWindow(self,handler):
        pass

    def CloseWin(self,handler):
        print('仿真主窗口关闭')
        self.Close(True)
        pass



class MainApp(wx.App):
    def OnInit(self):
        #   获取屏幕分辨率，计算使窗口居中
        scnWidth,scnHeight=wx.DisplaySize()
        winWidth = 500
        winHeight = 600
        posX = (scnWidth - winWidth)/2
        posY = (scnHeight - winHeight)/2
        style = wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX
        self.frame = MyMainWindow(id=-1, title=u'综合管廊火灾仿真---主界面', pos=(posX, posY), size=(winWidth, winHeight), style=style)
        self.frame.Show(True)
        return True

def main():
    app = MainApp()
    app.MainLoop()

if __name__ == "__main__":
    main()







# app = wx.App()
# #   获取屏幕分辨率，计算使窗口居中
# scn=wx.DisplaySize()
# scnWidth = scn[0]
# scnHeight = scn[1]
# winWidth = 500
# winHeight = 600
# posX = (scnWidth - winWidth)/2
# posY = (scnHeight - winHeight)/2
# #   创建窗口
# MainWin = wx.Frame(None,title='火灾方针系统---主界面',
#         size=(winWidth,winHeight), pos=(posX, posY), style=wx.DEFAULT_FRAME_STYLE)
# #   开始布局并创建按钮
# pl_gen = wx.Panel(MainWin)
# pl_gen.SetBackgroundColour('#E0EEE0')
# btn_gen = wx.Button(pl_gen, label = u'生成数据', pos = (200, 112), size = (100, 50))
# btn_gen.SetBackgroundColour('#D2B48C')
#
# btn_sim = wx.Button(pl_gen, label = u'开始仿真', pos = (200, 224), size = (100, 50))
# btn_sim.SetBackgroundColour('#CD6889')
#
# btn_exit = wx.Button(pl_gen,label = u'退出程序', pos = (200, 400), size = (100, 50))
# btn_exit.SetBackgroundColour('#FF4040')
#
#
# def closeWin(self,event):
#     self.Close(True)
#
# MainWin.Show(True)
# app.MainLoop()

# 创建仿真窗口结束

'''
        数据生成窗口
'''
# def showGenWin():
#     GenWin = tk.Tk()
#     GenWin.title('火灾仿真--数据生成')
#     GenWin.geometry(tmpcnf)
#
#     frm = tk.Frame(GenWin,height=400,width=500,bg='pink')
#     frm.pack()
#
#     frm1 = tk.Frame(frm,height=150,width=500,bg='pink')
#     frm1.pack(side='top', pady=5)
#     blackbutton = tk.Button(frm1, text="Black", fg="black")
#     blackbutton.pack()
#
#     #
#     # frm2 = tk.Frame(frm,height=150,width=500,bg='grey')
#     # frm2.pack(side='top',pady = 5)
#     #
#     # frm3 = tk.Frame(frm, height=150, width=500, bg='#EEA9B8',border=5)
#     # frm3.pack(side='top', pady = 5)
#
#     # gen_exit = tk.Button(frm,text='返回主界面',width=8,height=7,bg='red',fg='black',command=GenWin.destroy)
#     # gen_exit.pack()
#
#
#     GenWin.mainloop()
#
#
# #  仿真主界面
# def showSimWin():
#     SimWin = tk.Toplevel()
#     SimWin.title('火灾仿真--主界面')
#     SimWin.geometry(tmpcnf)
#     gen_btn = tk.Label(SimWin, text='点击测试', width=8, height=7, bg='red', fg='black')
#     gen_btn.pack()
#     gen_exit = tk.Button(SimWin, text='返回主界面', width=8, height=7, bg='red', fg='black', command=SimWin.destroy)
#     gen_exit.pack()
#     SimWin.mainloop()
#
#
# # 三个按钮
# btn_gen = tk.Button(root,text='生成数据', width=8, height=7, bg='red', fg='black',command=showGenWin)
# btn_gen.pack()
# btn_sim = tk.Button(root,text='开始仿真', width=8, height=7, bg='green', fg='black',command=showSimWin)
# btn_sim.pack()
# btn_exit = tk.Button(root,text='退出程序', width=8, height=7, bg='grey', fg='black',command=root.destroy)
# btn_exit.pack(pady= 20)
# # 三个按钮结束
#
#
#
# PyGen.say_hi()
#
# root.mainloop()
