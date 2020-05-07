from . import dialog_text_base
from ..corefuncs import loadfontlist
from sys import platform


class kiftt_create_text_dialog(dialog_text_base.kiftt_text_dialog_base):
    def __init__(self, inheritance, parent_font_list_dict, parent_font_settings_dict):
        super().__init__(None)
        self.font_list_dict = parent_font_list_dict
        for i in self.font_list_dict:
            self.choice_fontgroup.Append(i)
        # Reload settings

    def pgui_reload_font(self, event):
        temp_font_list = {}
        # Clear lists
        self.font_list_dict.clear()
        self.choice_fontgroup.Clear()
        # Get fonts
        if platform == "linux" or platform == "linux2":
            temp_font_list = loadfontlist.get_linux_fonts().copy()
        # Get font group names
        font_groups = list(temp_font_list)
        # Only continue when there's actually any font group
        if len(font_groups) != 0:
            for i in font_groups:
                self.choice_fontgroup.Append(i)  # Add font group names to the choice list
                # Copy the obtained font groups to the global font group dictionary
                self.font_list_dict[i] = temp_font_list[i]
            # Select the first choice
            self.choice_fontgroup.Selection = 0
            # Add font face choices
            font_faces = temp_font_list[font_groups[0]]
            for i in font_faces:
                self.choice_fontface.Append(i[1])
            self.choice_fontface.Selection = 0

    def pgui_change_font_group(self, event):
        self.choice_fontface.Clear()
        for i in self.font_list_dict[list(self.font_list_dict)[self.choice_fontgroup.Selection]]:
            self.choice_fontface.Append(i[1])
        self.choice_fontface.Selection = 0
