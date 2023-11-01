from manim import *

from _base import MyScene
from _imports import latex


class Conclusion(MyScene):
    _intro = "Conclusion"

    _desc = [
        "SwaraAI is defined to empower voices, enrich content and bridge gaps.",
        "We are looking forward to your support and guidance in our journey. Join us on this journey to make the digital world accessible, engaging, and inclusive for all !",
        "We are a team of 6 members, who are passionate about our work and are determined to make a difference in the world.",
    ]

    def construct(self):
        gap = DOWN * 1.5

        title = self.get_title()
        intro = (
            latex(
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
                latex(
                    line,
                    14,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "empower voices": self.highlight_color,
                        "enrich content": self.highlight_color,
                        "bridge gaps": self.highlight_color,
                        "6 members": self.highlight_color,
                        "make a difference in the world": self.highlight_color,
                        "support and guidance": self.highlight_color,
                        "make the digital world accessible, engaging, and inclusive for all": self.highlight_color,
                    },
                )
                .set(width=8)
                .next_to(intro, gap, buff=0.5)
                .shift(down_shift)
                .align_to(intro, LEFT)
            )
            desc.add(line)
            down_shift -= line.height + 0.2

        team = SVGMobject("images/team.svg").set(width=4).next_to(desc, RIGHT, buff=0.5)

        self.add(title)
        self.play(
            LaggedStartMap(FadeIn, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeIn, desc, lag_ratio=0.2, run_time=2),
        )
        self.play(Write(team, run_time=2))

        self.wait(9)

        self.play(
            LaggedStartMap(FadeOut, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeOut, desc, lag_ratio=0.2, run_time=2),
            FadeOut(team),
        )
