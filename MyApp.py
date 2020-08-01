# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1346,781 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Sample Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gbSizer1.Add( self.m_staticText1, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_textCtrl1, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_button1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Sharpening", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_textCtrl2, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.m_staticTitle1 = wx.StaticText( self, wx.ID_ANY, u"Smoothing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTitle1.Wrap( -1 )

		gbSizer1.Add( self.m_staticTitle1, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Blur", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_slider2 = wx.Slider( self, wx.ID_ANY, 1, 1, 5, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		gbSizer1.Add( self.m_slider2, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticTitlet3 = wx.StaticText( self, wx.ID_ANY, u"Binarization", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTitlet3.Wrap( -1 )

		gbSizer1.Add( self.m_staticTitlet3, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_spinCtrl5 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 255, 150 )
		gbSizer1.Add( self.m_spinCtrl5, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"threshold", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gbSizer1.Add( self.m_staticText4, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"medianBlur", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_slider4 = wx.Slider( self, wx.ID_ANY, 1, 1, 9, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		gbSizer1.Add( self.m_slider4, wx.GBPosition( 7, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticTitle2 = wx.StaticText( self, wx.ID_ANY, u"Edge", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTitle2.Wrap( -1 )

		gbSizer1.Add( self.m_staticTitle2, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"threshold1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer1.Add( self.m_staticText6, wx.GBPosition( 9, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10000, 1 )
		gbSizer1.Add( self.m_spinCtrl1, wx.GBPosition( 9, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"threshold2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer1.Add( self.m_staticText7, wx.GBPosition( 10, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10000, 1 )
		gbSizer1.Add( self.m_spinCtrl2, wx.GBPosition( 10, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"dilate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gbSizer1.Add( self.m_staticText8, wx.GBPosition( 11, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_slider5 = wx.Slider( self, wx.ID_ANY, 1, 1, 5, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		gbSizer1.Add( self.m_slider5, wx.GBPosition( 11, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticTitle3 = wx.StaticText( self, wx.ID_ANY, u"Extracted height", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTitle3.Wrap( -1 )

		gbSizer1.Add( self.m_staticTitle3, wx.GBPosition( 12, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"area", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gbSizer1.Add( self.m_staticText9, wx.GBPosition( 13, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_spinCtrl3 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 1000, 40 )
		gbSizer1.Add( self.m_spinCtrl3, wx.GBPosition( 13, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"height", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gbSizer1.Add( self.m_staticText10, wx.GBPosition( 14, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_spinCtrlDouble1 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 100, 10.000000, 1 )
		self.m_spinCtrlDouble1.SetDigits( 0 )
		gbSizer1.Add( self.m_spinCtrlDouble1, wx.GBPosition( 14, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Marker", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetValue(True)
		gbSizer1.Add( self.m_checkBox1, wx.GBPosition( 15, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Rect", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_checkBox2, wx.GBPosition( 15, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_button2, wx.GBPosition( 16, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_button3, wx.GBPosition( 16, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer1.Add( self.m_panel4, wx.GBPosition( 12, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetMinSize( wx.Size( 512,512 ) )
		self.m_panel2.SetMaxSize( wx.Size( 512,512 ) )

		bSizer5.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetMinSize( wx.Size( 512,512 ) )
		self.m_panel3.SetMaxSize( wx.Size( 512,512 ) )

		bSizer5.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 1, 2 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelValue( 0, u"params" )
		self.m_grid2.SetColLabelValue( 1, u"value" )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid2.SetMinSize( wx.Size( 258,150 ) )

		bSizer3.Add( self.m_grid2, 0, wx.ALL, 5 )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 1, 3 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"area [nm2]" )
		self.m_grid1.SetColLabelValue( 1, u"height [nm]" )
		self.m_grid1.SetColLabelValue( 2, u"display" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid1.SetMinSize( wx.Size( 340,150 ) )

		bSizer3.Add( self.m_grid1, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_spinCtrl4 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10000, 0 )
		bSizer3.Add( self.m_spinCtrl4, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )


		gbSizer1.Add( bSizer2, wx.GBPosition( 0, 4 ), wx.GBSpan( 17, 12 ), wx.EXPAND, 5 )


		self.SetSizer( gbSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
		self.m_slider2.Bind( wx.EVT_SCROLL, self.m_slider2OnScroll )
		self.m_spinCtrl5.Bind( wx.EVT_TEXT_ENTER, self.m_spinCtrl5OnTextEnter )
		self.m_slider4.Bind( wx.EVT_SCROLL, self.m_slider4OnScroll )
		self.m_spinCtrl1.Bind( wx.EVT_TEXT_ENTER, self.m_spinCtrl1OnTextEnter )
		self.m_spinCtrl2.Bind( wx.EVT_TEXT_ENTER, self.m_spinCtrl2OnTextEnter )
		self.m_slider5.Bind( wx.EVT_SCROLL, self.m_slider5OnScroll )
		self.m_spinCtrl3.Bind( wx.EVT_TEXT_ENTER, self.m_spinCtrl3OnTextEnter )
		self.m_spinCtrlDouble1.Bind( wx.EVT_TEXT, self.m_spinCtrlDouble1OnSpinCtrlText )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.m_checkBox1OnCheckBox )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.m_checkBox2OnCheckBox )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
		self.m_button3.Bind( wx.EVT_BUTTON, self.m_button3OnButtonClick )
		self.m_grid1.Bind( wx.grid.EVT_GRID_EDITOR_CREATED, self.m_grid1OnGridEditorCreated )
		self.m_grid1.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.m_grid1OnGridSelectCell )
		self.m_spinCtrl4.Bind( wx.EVT_TEXT, self.m_spinCtrl4OnSpinCtrlText )
		self.m_spinCtrl4.Bind( wx.EVT_TEXT_ENTER, self.m_spinCtrl4OnTextEnter )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button1OnButtonClick( self, event ):
		event.Skip()

	def m_slider2OnScroll( self, event ):
		event.Skip()

	def m_spinCtrl5OnTextEnter( self, event ):
		event.Skip()

	def m_slider4OnScroll( self, event ):
		event.Skip()

	def m_spinCtrl1OnTextEnter( self, event ):
		event.Skip()

	def m_spinCtrl2OnTextEnter( self, event ):
		event.Skip()

	def m_slider5OnScroll( self, event ):
		event.Skip()

	def m_spinCtrl3OnTextEnter( self, event ):
		event.Skip()

	def m_spinCtrlDouble1OnSpinCtrlText( self, event ):
		event.Skip()

	def m_checkBox1OnCheckBox( self, event ):
		event.Skip()

	def m_checkBox2OnCheckBox( self, event ):
		event.Skip()

	def m_button2OnButtonClick( self, event ):
		event.Skip()

	def m_button3OnButtonClick( self, event ):
		event.Skip()

	def m_grid1OnGridEditorCreated( self, event ):
		event.Skip()

	def m_grid1OnGridSelectCell( self, event ):
		event.Skip()

	def m_spinCtrl4OnSpinCtrlText( self, event ):
		event.Skip()

	def m_spinCtrl4OnTextEnter( self, event ):
		event.Skip()


