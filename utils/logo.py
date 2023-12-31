from manim import *

from .colors import MyColors

_height = 6
_bg_opacity = 0.75


def logo_bg(opacity=_bg_opacity):
    bg = SVGMobject("logo/bg.svg")
    bg.height = _height
    bg.width = _height

    bg.set_fill(
        color=color_gradient(
            MyColors.logo_bg,
            _height,
        ),
        opacity=opacity,
        family=True,
    )

    return bg


def logo_text(opacity=1):
    text = SVGMobject(
        "logo/text.svg",
        fill_color=MyColors.logo_text,
        fill_opacity=0.8,
        stroke_color=MyColors.logo_text,
        stroke_width=2,
    )
    text.width = _height * 1.5
    text.set_opacity(opacity)
    return text


def logo_text(stroke_width=2):
    text = SVGMobject(
        "logo/text.svg",
        fill_color=MyColors.logo_text,
        fill_opacity=0.8,
        stroke_color=MyColors.logo_text,
        stroke_width=stroke_width,
    )
    text.width = _height * 1.5
    return text


class Logo(Scene):
    """
    SwaraAI Logo

    To create the logo, use the following command:
    ```bash
    manim utils/logo.py Logo -p -qk -t
    ```
    """

    def construct(self):
        _logo_bg = logo_bg(0.75)
        _logo_text = logo_text(2)

        self.add(_logo_bg)
        self.add(_logo_text)
