from manim import *
import os

from _base import MyScene


class Solution(MyScene):
    _title = "SwaraAI"
    _intro = "Solution"

    _desc = [
        "SwaraAI provides a solution to this problem. It allows users to quickly and easily dub videos into other Indian regional languages.",
        "The software produces a voiceover in a human-like voice, as well as text supers that are dubbed from English to other Indian regional languages.",
        "The translated voiceover is also in simple language, easy to understand, and not colloquial in nature.",
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
                    15,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "quickly and easily": RED,
                        "human-like voice": RED,
                        "text supers": RED,
                        "simple language, easy to understand, and not colloquial in nature": RED,
                    },
                )
                .set(width=8)
                .next_to(intro, gap, buff=0.5)
                .shift(down_shift)
                .align_to(intro, LEFT)
            )
            desc.add(line)
            down_shift -= line.height + 0.2

        self.add(title)

        self.play(
            LaggedStartMap(FadeIn, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeIn, desc, lag_ratio=0.2, run_time=2),
        )

        self.wait(2)

        self.play(
            LaggedStartMap(FadeOut, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeOut, desc, lag_ratio=0.2, run_time=2),
        )
