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

import pcbnew
import os


from .dialog.dialog_add_text import *


class KiCadFreeTypeTextPlugin(pcbnew.ActionPlugin, object):

    def __init__(self):
        super(KiCadFreeTypeTextPlugin, self).__init__()
        self.name = "Generate and edit stroke font text with FreeType2"
        self.category = "Read PCB"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')
        self.description = "Generate and edit the stroke font text" \
                           "with the help of external FreeType2 binaries."
        self.font_dict = {}
        self.font_settings = {
            'height', 5.0,
            'vertical_scale', 1.0,
            'horizontal_scale', 1.0,
            'line_spacing', 1.2,
            'character_spacing', 0.0
        }

    def defaults(self):
        pass

    def Run(self):
        b = kiftt_create_text_dialog(None, self.font_dict, self.font_settings)
        b.Show()
        

plugin = KiCadFreeTypeTextPlugin()
plugin.register()