from manim import *

from _imports import logo_bg, logo_text, MyColors


class MyScene(Scene):
    highlight_color = MyColors.highlight_color

    def latex(self, text, font_size, **kwargs):
        latex_string = r"\fontsize{%d}{%d}\selectfont %s" % (font_size, 0, text)
        return Tex(latex_string, **kwargs)

    def get_title(self):
        _logo_bg = logo_bg(0.25)
        _logo_text = logo_text(0.5)
        logo = VGroup(_logo_bg, _logo_text)
        logo.scale(0.25)
        logo.to_corner(UL, buff=1)
        logo.shift(UP * 0.25)
        return logo
