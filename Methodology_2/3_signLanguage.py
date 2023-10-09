from manim import *

from _imports import latex, MyColors, video_frame


class SignLanguage(Scene):
    _heading = "Sign Language Support"

    _desc = [
        "Sign Language Support is creating a video that can be understood by deaf and dumb people. An avatar will be created in video that will perform sign language. Every one finds vocal communication simpler and no one should ever be denied the right to communicate.",
        # Why is it needed?
        "It is needed because deaf and dumb people can't understand the content of the video. They can't understand the content of the video even if it is in their regional language.",
        # How SwaraAI will handle it?
        "SwaraAI will create an avatar that will perform sign language in the video. Avatar will perform sign language in the Indian Sign Language (ISL).",
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

        for line in self._desc[:-2]:
            line = (
                latex(
                    line,
                    11,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "Sign Language Support": MyColors.highlight_color,
                        "deaf and dumb people": MyColors.highlight_color,
                        "avatar": MyColors.highlight_color,
                        "Indian Sign Language (ISL)": MyColors.highlight_color,
                    },
                )
                .set(width=10)
                .next_to(heading, gap, buff=0.5)
                .shift(down_shift)
                .align_to(heading, LEFT)
            )
            desc.add(line)
            down_shift -= line.height + 0.2

        for line in self._desc[-2:]:
            line = (
                latex(
                    line,
                    16,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "Sign Language Support": MyColors.highlight_color,
                        "deaf and dumb people": MyColors.highlight_color,
                        "avatar": MyColors.highlight_color,
                        "Indian Sign Language (ISL)": MyColors.highlight_color,
                    },
                )
                .set(width=7)
                .next_to(desc, DOWN)
                .align_to(desc, LEFT)
            )
            desc.add(line)

        video = video_frame()
        video.set(width=5.5).to_corner(DR, buff=0.5)

        avatar = SVGMobject("images/avatar.svg")
        avatar.set(height=2.5)
        avatar.move_to(video).shift(RIGHT * 1.8)

        vid_avatar = VGroup(video, avatar)

        self.play(Write(heading))
        self.play(LaggedStartMap(FadeIn, desc, lag_ratio=0.2, run_time=2))
        self.play(
            LaggedStartMap(
                Write,
                vid_avatar,
                lag_ratio=0.2,
                run_time=2,
            )
        )
        self.wait(5)

        self.play(
            LaggedStartMap(FadeOut, desc, lag_ratio=0.2, run_time=2),
            Unwrite(heading),
            LaggedStartMap(FadeOut, vid_avatar, lag_ratio=0.2, run_time=2),
        )

        self.wait(0.5)
