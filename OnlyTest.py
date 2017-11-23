import wx

app = wx.App()
window = wx.Frame(None, title="wxPython - www.yiibai.com", size=(400, 300))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="Hello World", pos=(100, 100))
window.Show(True)
app.MainLoop()

#   烟雾浓度布局块
#         vi = wx.StaticBox(pl_gen, -1, '烟雾浓度生成:')
#
#         viSizer = wx.StaticBoxSizer(vi, wx.HORIZONTAL)  # RadioButton的StataicSizer
#         funcList_vi = ['Y = aX + b', 'Y = aX + Rand(b~c)', u'正态分布']
#         timeList_vi = [u'30 秒', u'60 秒', u'120 秒']
#         frenList_vi = ['1 次/秒', '2 次/秒', '4 次/秒']
#         radio_func_vi = wx.RadioBox(pl_gen, -1, "数据生成函数", (10, 10), wx.DefaultSize,
#                                  funcList_vi, 3, wx.RA_SPECIFY_ROWS)
#         radio_time_vi = wx.RadioBox(pl_gen, -1, "采样时间", (10, 10), wx.DefaultSize,
#                                  timeList_vi, 3, wx.RA_SPECIFY_ROWS)
#         radio_fren_vi = wx.RadioBox(pl_gen, -1, "采样频率", (10, 10), wx.DefaultSize,
#                                  frenList_vi, 3, wx.RA_SPECIFY_ROWS)
#         viSizer.Add(radio_func_vi, 0, wx.ALL | wx.ALIGN_LEFT, 5)
#         viSizer.Add(radio_time_vi, 0, wx.ALL | wx.ALIGN_LEFT, 5)
#         viSizer.Add(radio_fren_vi, 0, wx.ALL | wx.ALIGN_LEFT, 5)
#         #       按钮块
#         btn_vi_confirm = wxBtn.GenButton(pl_gen, label=u'预览&确认', size=(100, 20))
#         btn_vi_confirm.SetBackgroundColour('#D2B48C')
#         viSizer.Add(btn_vi_confirm, wx.ALL | wx.CENTER | wx.BOTTOM, 5)