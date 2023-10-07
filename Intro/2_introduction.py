from manim import *
import os

from _base import MyScene


class Introduction(MyScene):
    _intro = "Introduction"

    _desc = [
        "CIPAM is engaged in creation of promotional and awareness videos on intellectual property in India.",
        "Our software that can be used for dubbing of videos from English to other Indian regional languages will help in outreach of such videos for public awareness.",
    ]

    def construct(self):
        file_path = os.path.realpath(__file__)
        parent_dir = os.path.dirname(file_path)
        image_files = os.listdir(
            os.path.join(parent_dir, "..", "assets", "images", "intro")
        )

        images = [
            ImageMobject(f"images/intro/{image_file}") for image_file in image_files
        ]

        loop = 2
        image_width = 4
        current_height = 8

        image_group = Group()
        for _ in range(loop):
            for image in images:
                image.set(width=image_width)
                image.move_to(UP * current_height + RIGHT * 4.5)
                image_group.add(image)
                current_height -= image.height + 0.5

        image_group_height = images[0].height * loop * 2 + 0.5 * (loop - 1) * 2

        image_group.shift(UP * image_group_height)

        gap = DOWN * 1.5

        title = self.get_title()
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
                        "promotional": self.highlight_color,
                        "awareness": self.highlight_color,
                        "intellectual property": self.highlight_color,
                        "outreach of such videos for public awareness": self.highlight_color,
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

        self.play(
            LaggedStartMap(FadeIn, image_group, lag_ratio=0.2, run_time=2),
            Transform(
                image_group,
                image_group.copy().shift((UP * image_group_height + UP * 2) * 0.05),
                run_time=2,
                rate_func=linear,
            ),
        )

        self.play(
            Transform(
                image_group,
                image_group.copy().shift((UP * image_group_height + UP * 2) * 0.9),
                run_time=36,
                rate_func=linear,
            ),
        )

        self.play(
            Transform(
                image_group,
                image_group.copy().shift((UP * image_group_height + UP * 2) * 0.1),
                run_time=4,
                rate_func=linear,
            ),
            LaggedStartMap(FadeOut, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeOut, desc, lag_ratio=0.2, run_time=2),
            LaggedStartMap(FadeOut, image_group, lag_ratio=0.2, run_time=2),
        )
