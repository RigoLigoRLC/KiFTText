'''
/**
 * KiFTText, a plugin for KiCad which supports the use of outline font.
 * Copyright (C) 2020 RigoLigo.
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */
 '''

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Apr  4 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class kiftt_text_dialog_base
###########################################################################

def pgui_enter_horizontal_scale(event):
	event.Skip()


class kiftt_text_dialog_base ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Create New KiFTText Text Object", pos = wx.DefaultPosition, size = wx.Size( 622,453 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.MINIMIZE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sizer_master = wx.FlexGridSizer( 0, 1, 0, 0 )
		sizer_master.SetFlexibleDirection( wx.BOTH )
		sizer_master.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sizer_fontselector = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer_fontselector.SetFlexibleDirection( wx.BOTH )
		sizer_fontselector.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.text_fontgroup = wx.StaticText( self, wx.ID_ANY, u"Font Group", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_fontgroup.Wrap( -1 )

		sizer_fontselector.Add( self.text_fontgroup, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choice_fontgroupChoices = []
		self.choice_fontgroup = wx.Choice( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 512,35 ), choice_fontgroupChoices, 0 )
		self.choice_fontgroup.SetSelection( 0 )
		sizer_fontselector.Add( self.choice_fontgroup, 0, wx.ALL, 5 )

		self.text_fontface = wx.StaticText( self, wx.ID_ANY, u"Font Face", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_fontface.Wrap( -1 )

		sizer_fontselector.Add( self.text_fontface, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choice_fontfaceChoices = []
		self.choice_fontface = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 512,35 ), choice_fontfaceChoices, 0 )
		self.choice_fontface.SetSelection( 0 )
		sizer_fontselector.Add( self.choice_fontface, 0, wx.ALL, 5 )


		sizer_master.Add( sizer_fontselector, 1, wx.EXPAND, 5 )

		sizer_fontsize = wx.BoxSizer( wx.HORIZONTAL )

		self.text_fontsizemm = wx.StaticText( self, wx.ID_ANY, u"Font Height (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_fontsizemm.Wrap( -1 )

		sizer_fontsize.Add( self.text_fontsizemm, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		combo_fontsizemmChoices = [ u"1", u"2", u"3", u"4", u"5", u"6", u"8", u"10", u"12", u"15", u"20", u"25", u"30", wx.EmptyString ]
		self.combo_fontsizemm = wx.ComboBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, combo_fontsizemmChoices, 0, wx.DefaultValidator, u"Create New KiFTText Text" )
		self.combo_fontsizemm.SetMinSize( wx.Size( 90,-1 ) )

		sizer_fontsize.Add( self.combo_fontsizemm, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		sizer_fontmanipulation = wx.GridSizer( 0, 2, 0, 0 )

		self.button_reloadfonts = wx.Button( self, wx.ID_ANY, u"Reload Fonts", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.button_reloadfonts.SetBitmapMargins( wx.Size( 0,-1 ) )
		sizer_fontmanipulation.Add( self.button_reloadfonts, 0, wx.ALL|wx.EXPAND, 5 )

		self.button_useexternalfont = wx.Button( self, wx.ID_ANY, u"Use External Font", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_fontmanipulation.Add( self.button_useexternalfont, 0, wx.ALL|wx.EXPAND, 5 )


		sizer_fontsize.Add( sizer_fontmanipulation, 1, wx.EXPAND, 5 )


		sizer_master.Add( sizer_fontsize, 1, wx.EXPAND, 5 )

		sizer_adjustments = wx.FlexGridSizer( 0, 4, 0, 0 )
		sizer_adjustments.SetFlexibleDirection( wx.BOTH )
		sizer_adjustments.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.text_verticalscale = wx.StaticText( self, wx.ID_ANY, u"Vertical Scale", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_verticalscale.Wrap( -1 )

		sizer_adjustments.Add( self.text_verticalscale, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.spin_verticalscale = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0.001, 100, 1, 0.01 )
		self.spin_verticalscale.SetDigits( 2 )
		sizer_adjustments.Add( self.spin_verticalscale, 1, wx.ALL|wx.EXPAND, 5 )

		self.text_horizontalscale = wx.StaticText( self, wx.ID_ANY, u"Horizontal Scale", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_horizontalscale.Wrap( -1 )

		sizer_adjustments.Add( self.text_horizontalscale, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.spin_horizontalscale = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0.001, 100, 1, 0.01 )
		self.spin_horizontalscale.SetDigits( 2 )
		sizer_adjustments.Add( self.spin_horizontalscale, 1, wx.ALL|wx.EXPAND, 5 )

		self.text_linespacing = wx.StaticText( self, wx.ID_ANY, u"Line Spacing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_linespacing.Wrap( -1 )

		sizer_adjustments.Add( self.text_linespacing, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.spin_linespacing = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0.001, 100, 1.2, 0.01 )
		self.spin_linespacing.SetDigits( 2 )
		sizer_adjustments.Add( self.spin_linespacing, 0, wx.ALL, 5 )

		self.text_characterspacing = wx.StaticText( self, wx.ID_ANY, u"Character Spacing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_characterspacing.Wrap( -1 )

		sizer_adjustments.Add( self.text_characterspacing, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.spin_characterspacing = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0.001, 100, 0, 0.01 )
		self.spin_characterspacing.SetDigits( 2 )
		sizer_adjustments.Add( self.spin_characterspacing, 0, wx.ALL, 5 )


		sizer_master.Add( sizer_adjustments, 1, wx.EXPAND, 5 )

		sizer_text = wx.BoxSizer( wx.VERTICAL )

		sizer_text.SetMinSize( wx.Size( -1,150 ) )
		self.text_text = wx.StaticText( self, wx.ID_ANY, u"Text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_text.Wrap( -1 )

		sizer_text.Add( self.text_text, 0, wx.ALL, 5 )

		self.text_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.TE_LEFT|wx.TE_MULTILINE|wx.TE_PROCESS_ENTER )
		sizer_text.Add( self.text_text, 1, wx.ALL|wx.EXPAND, 5 )


		sizer_master.Add( sizer_text, 1, wx.EXPAND, 5 )

		sizer_generate = wx.FlexGridSizer( 0, 2, 0, 0 )
		sizer_generate.SetFlexibleDirection( wx.BOTH )
		sizer_generate.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.button_generateoutlinetext = wx.Button( self, wx.ID_ANY, u"Generate Outline Text", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_generate.Add( self.button_generateoutlinetext, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sizer_master.Add( sizer_generate, 1, wx.EXPAND, 5 )


		self.SetSizer( sizer_master )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.choice_fontgroup.Bind( wx.EVT_CHOICE, self.pgui_change_font_group )
		self.combo_fontsizemm.Bind( wx.EVT_COMBOBOX, self.pgui_change_font_height )
		self.combo_fontsizemm.Bind( wx.EVT_TEXT_ENTER, self.pgui_enter_font_height )
		self.button_reloadfonts.Bind( wx.EVT_BUTTON, self.pgui_reload_font )
		self.spin_verticalscale.Bind( wx.EVT_SPINCTRLDOUBLE, self.pgui_change_vertical_scale )
		self.spin_verticalscale.Bind( wx.EVT_TEXT_ENTER, self.pgui_enter_vertical_scale )
		self.spin_horizontalscale.Bind( wx.EVT_SPINCTRLDOUBLE, self.pgui_change_horizontal_scale )
		self.spin_horizontalscale.Bind( wx.EVT_TEXT_ENTER, pgui_enter_horizontal_scale )
		self.spin_linespacing.Bind( wx.EVT_SPINCTRLDOUBLE, self.pgui_change_line_spacing )
		self.spin_linespacing.Bind( wx.EVT_TEXT_ENTER, self.pgui_enter_line_spacing )
		self.spin_characterspacing.Bind( wx.EVT_SPINCTRLDOUBLE, self.pgui_change_character_spacing )
		self.spin_characterspacing.Bind( wx.EVT_TEXT_ENTER, self.pgui_enter_character_spacing )
		self.button_generateoutlinetext.Bind( wx.EVT_BUTTON, self.pgui_generate_text )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def pgui_change_font_group( self, event ):
		event.Skip()

	def pgui_change_font_height( self, event ):
		event.Skip()

	def pgui_enter_font_height( self, event ):
		event.Skip()

	def pgui_reload_font( self, event ):
		event.Skip()

	def pgui_change_vertical_scale( self, event ):
		event.Skip()

	def pgui_enter_vertical_scale( self, event ):
		event.Skip()

	def pgui_change_horizontal_scale( self, event ):
		event.Skip()

	def pgui_change_line_spacing( self, event ):
		event.Skip()

	def pgui_enter_line_spacing( self, event ):
		event.Skip()

	def pgui_change_character_spacing( self, event ):
		event.Skip()

	def pgui_enter_character_spacing( self, event ):
		event.Skip()

	def pgui_generate_text( self, event ):
		event.Skip()


