from manim import *

from _imports import logo_bg, logo_text, MyColors


class MyScene(Scene):
    highlight_color = MyColors.highlight_color

    def get_title(self):
        _logo_bg = logo_bg(0.25)
        _logo_text = logo_text(0.5)
        _logo_text.set_opacity(0.5)
        _logo_bg.set(width=1.5)
        _logo_text.set(width=2.25)
        logo = VGroup(_logo_bg, _logo_text)
        logo.to_corner(UL, buff=1)
        logo.shift(UP * 0.25)
        return logo
