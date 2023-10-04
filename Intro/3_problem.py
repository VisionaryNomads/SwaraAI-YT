from manim import *

from _base import MyScene


class Problem(MyScene):
    _title = "SwaraAI"
    _intro = "Problem"

    _desc = [
        "India is a diverse country with over 22 official languages. This diversity can be a challenge when it comes to communicating with a wide audience.",
        "For example, if a video is created in English, it may not be accessible to people who do not speak English as their first language.",
    ]

    def construct(self):
        gap = DOWN * 1.5

        title = self.latex(self._title, 80, color=YELLOW).to_corner(UL, buff=1)
        intro = (
            self.latex(
                self._intro,
                10,
                color=WHITE,
                tex_environment="flushleft",
            )
            .next_to(title, gap, buff=0.5)
            .align_to(title, LEFT)
        )

        down_shift = 0
        desc = VGroup()
        for line in self._desc:
            line = (
                self.latex(
                    line,
                    16,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "22 official languages": RED,
                        "challenge": RED,
                        "communicating with a wide audience": RED,
                    },
                )
                .set(width=7)
                .next_to(intro, gap, buff=0.5)
                .shift(down_shift)
                .align_to(intro, LEFT)
            )
            desc.add(line)
            down_shift -= line.height + 0.2

        langs = SVGMobject("images/languages.svg")
        langs.height = 6.68
        langp = ImageMobject("images/languages.png")
        langp.height = 6
        langs.move_to(UP * 0.1 + LEFT * 0.04)
        lang = Group(langs, langp)
        lang.to_edge(RIGHT, buff=0.5)

        self.add(title)

        self.play(
            LaggedStartMap(FadeIn, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeIn, desc, lag_ratio=0.2, run_time=2),
            LaggedStartMap(
                DrawBorderThenFill,
                langs,
                lag_ratio=0.2,
                run_time=4,
            ),
        )

        self.play(FadeIn(langp))

        self.wait(2)

        self.play(
            LaggedStartMap(FadeOut, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeOut, desc, lag_ratio=0.2, run_time=2),
            LaggedStartMap(FadeOut, langs, lag_ratio=0.2, run_time=0.5),
            LaggedStartMap(FadeOut, langp, lag_ratio=0.2, run_time=2),
        )
