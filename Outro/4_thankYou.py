from manim import *

from _base import MyScene
from _imports import latex, logo_bg, logo_text


class ThankYou(MyScene):
    _intro = "Thank You !"

    def construct(self):
        gap = DOWN * 1.5

        logo = self.get_title()
        intro = latex(
            self._intro,
            20,
            color=WHITE,
            tex_environment="flushleft",
        ).move_to(ORIGIN)

        _logo_bg = logo_bg(0.75)
        _logo_text = logo_text(2)
        _logo = VGroup(_logo_bg, _logo_text)

        self.add(logo)
        self.play(
            LaggedStartMap(FadeIn, intro, lag_ratio=0.2, run_time=1),
        )

        self.wait(2)

        self.play(FadeOut(intro))
        self.play(ReplacementTransform(logo, _logo), run_time=1.5)
        self.wait(0.5)

        self.play(Unwrite(_logo_text, run_time=3))
        self.play(Unwrite(_logo_bg, run_time=2))
        self.wait(0.5)
