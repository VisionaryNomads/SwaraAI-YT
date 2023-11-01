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

    def quality_box(self, quality):
        text = latex(
            quality,
            font_size=10,
            color=MyColors.highlight_color,
        )
        box = SurroundingRectangle(text, buff=0.2, corner_radius=0.025, color=WHITE)
        return VGroup(text, box)

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

        _360p = self.quality_box("360p")
        _480p = self.quality_box("480p")
        _720p = self.quality_box("720p")
        _1080p = self.quality_box("1080p")
        _4k = self.quality_box("4k")

        (
            VGroup(_360p, _480p, _720p, _1080p, _4k)
            .arrange(RIGHT, buff=1)
            .next_to(desc[-1], DOWN, buff=1)
            .set(width=10)
            .align_to(desc[-1], LEFT)
        )

        # Arrows
        _360_to_480 = Arrow(
            _360p.get_right(), _480p.get_left(), buff=0.1, stroke_width=2
        )
        _480_to_720 = Arrow(
            _480p.get_right(), _720p.get_left(), buff=0.1, stroke_width=2
        )
        _720_to_1080 = Arrow(
            _720p.get_right(), _1080p.get_left(), buff=0.1, stroke_width=2
        )
        _1080_to_4k = Arrow(
            _1080p.get_right(), _4k.get_left(), buff=0.1, stroke_width=2
        )

        qlt_grp = VGroup(
            _360p,
            _360_to_480,
            _480p,
            _480_to_720,
            _720p,
            _720_to_1080,
            _1080p,
            _1080_to_4k,
            _4k,
        )

        self.play(Write(heading))
        self.play(LaggedStartMap(FadeIn, desc, lag_ratio=0.2, run_time=2))
        self.play(Write(qlt_grp), run_time=2)

        self.wait(40)

        self.play(
            LaggedStartMap(FadeOut, desc, lag_ratio=0.2, run_time=2),
            LaggedStartMap(FadeOut, qlt_grp, lag_ratio=0.2, run_time=2),
            Unwrite(heading),
        )

        self.wait(0.5)
