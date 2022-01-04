# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "SOLAR POWER PLANT PREDICTION", pos = wx.DefaultPosition, size = wx.Size( 967,592 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel2 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Data preprocessing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self.m_panel2, wx.ID_ANY, u"Preporcessing", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer3.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self.m_panel2, wx.ID_ANY, u"Check", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer3.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Prediction", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self.m_panel2, wx.ID_ANY, u"Dicrect model", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer3.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self.m_panel2, wx.ID_ANY, u"Combine model", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer3.Add( self.m_button5, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Export to Excel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_button51 = wx.Button( self.m_panel2, wx.ID_ANY, u"Export result to Excel", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer3.Add( self.m_button51, 0, wx.ALL, 5 )
		
		
		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		self.m_notebook2.AddPage( self.m_panel2, u"Function", False )
		
		bSizer1.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel5 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		# x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		# y_data = [2, 4, 6, 4, 2, 5, 6, 7, 1]
		# xy_data = list(zip(x_data, y_data))
		
		# line = wxplot.PolySpline(
		# 	xy_data,
		# 	colour=wx.Colour(128, 128, 0),   # Color: olive
		# 	width=3,         )

        # # Create your graphics object.
		# graphics = wxplot.PlotGraphics([line])
		# # Create your canvas.
		# panel = wxplot.PlotCanvas(self)

		# # Edit panel-wide settings.
		# axes_pen = wx.Pen(wx.BLUE, 1, wx.PENSTYLE_LONG_DASH)
		# panel.axesPen = axes_pen
		# # Draw the graphics object on the canvas.
		# panel.Draw(graphics)

		self.m_panel5.SetSizer( bSizer8 )
		self.m_panel5.Layout()
		bSizer8.Fit( self.m_panel5 )
		bSizer5.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer5, 10, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBox1 = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Show Grid", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_checkBox1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Show Legend", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_checkBox2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( bSizer4 )
		self.m_panel3.Layout()
		bSizer4.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"Graph", False )
		
		bSizer1.Add( self.m_notebook1, 4, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame1(None)
    # frame.SetIcon(wx.Icon("icon3.png"))
    frame.Show(True)
    app.MainLoop()