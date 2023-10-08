from manim import *

from _imports import latex, MyColors


class Enhancement(Scene):
    _heading = "Video Enhancement"

    _desc = [
        "Video Enhancement is a process of enhancing the video quality.",
        # Why is it needed?
        "It is needed because the video quality of the videos uploaded is not always good. It is difficult to understand the content of the video due to poor video quality.",
        # How SwaraAI will handle it?
        "SwaraAI will enhance the video quality and make it easier to understand the content of the video. User can choose the video quality from the settings.",
        "SwaraAI can enhance the blurry frames of the video or the entire video.",
    ]

    def construct(self):
        gap = DOWN * 1.5

        heading = latex(
            self._heading,
            font_size=15,
            color=WHITE,
        )

        heading.to_corner(UL, buff=1)

        down_shift = 0
        desc = VGroup()

        for line in self._desc:
            line = (
                latex(
                    line,
                    11,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "Video Enhancement": MyColors.highlight_color,
                        "blurry frames": MyColors.highlight_color,
                        "entire video": MyColors.highlight_color,
                    },
                )
                .set(width=10)
                .next_to(heading, gap, buff=0.5)
                .shift(down_shift)
                .align_to(heading, LEFT)
            )
            desc.add(line)
            down_shift -= line.height + 0.2

        self.play(Write(heading))
        self.play(
            LaggedStartMap(FadeIn, desc, lag_ratio=0.2, run_time=2),
        )
        self.wait(5)

        self.play(
            LaggedStartMap(FadeOut, desc, lag_ratio=0.2, run_time=2),
            Unwrite(heading),
        )

        self.wait(0.5)
