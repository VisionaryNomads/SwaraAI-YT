from manim import *


class MyScene(Scene):
    def latex(self, text, font_size, **kwargs):
        latex_string = r"\fontsize{%d}{%d}\selectfont %s" % (font_size, 0, text)
        return Tex(latex_string, **kwargs)
