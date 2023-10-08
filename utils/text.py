from manim import *


def latex(text, font_size, **kwargs):
    latex_string = r"\fontsize{%d}{%d}\selectfont %s" % (font_size, 1, text)
    return Tex(latex_string, **kwargs)
