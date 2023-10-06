from manim import *


class WriteLogoAnimation(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        alpha = self.rate_func(alpha)


class Tester(Scene):
    def construct(self):
        bg = SVGMobject("logo/bg.svg")
        _height = 6
        bg.height = _height
        bg.width = _height

        text = SVGMobject(
            "logo/text.svg",
            fill_color=WHITE,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=2,
        )
        # text.height = _height / 2
        text.width = _height * 1.5

        # Give color gradient to bg
        bg.set_fill(
            color=color_gradient(
                # ["#43cbff", "#4bb9fa", "#6088ee", "#813cda", "#9708cc"],
                ["#0080FF", "#00FF80"],
                _height,
            ),
            opacity=1,
            family=True,
        )

        bg_copy = bg.copy()
        bg_copy.set_opacity(0.75)

        bg.scale(1.2)

        self.play(WriteLogoAnimation(bg, run_time=2))

        self.wait(0.5)

        self.play(
            Transform(bg, bg_copy, run_time=3),
            Write(text, run_time=4),
        )

        self.wait(2)
