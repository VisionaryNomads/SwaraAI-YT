from manim import *
import os

from _base import MyScene


class Introduction(MyScene):
    _title = "SwaraAI"
    _intro = "Introduction"

    _desc = [
        "CIPAM is engaged in creation of promotional and awareness videos on intellectual property in India.",
        "Our software that can be used for dubbing of videos from English to other Indian regional languages will help in outreach of such videos for public awareness.",
    ]

    def construct(self):
        file_path = os.path.realpath(__file__)
        parent_dir = os.path.dirname(file_path)
        image_files = os.listdir(os.path.join(parent_dir, "..", "assets", "images"))

        images = [ImageMobject(f"images/{image_file}") for image_file in image_files]

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

        image_group.shift(UP * 12)

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
                        "promotional": RED,
                        "awareness": RED,
                        "intellectual property": RED,
                        "outreach of such videos for public awareness": RED,
                    },
                )
                .set(width=8)
                .next_to(intro, gap, buff=0.5)
                .shift(down_shift)
                .align_to(intro, LEFT)
            )
            desc.add(line)
            down_shift -= 1

        self.add(title)

        self.play(
            LaggedStartMap(FadeIn, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeIn, desc, lag_ratio=0.2, run_time=2),
            # LaggedStartMap(FadeIn, image_group, lag_ratio=0.2, run_time=2),
        )

        image_group_copy = image_group.copy().shift(UP * 12)

        self.play(
            LaggedStartMap(FadeIn, image_group, lag_ratio=0.2, run_time=2),
            Transform(image_group, image_group_copy, run_time=40, rate_func=linear),
        )

        # self.play(
        #     *[Transform(image, image.copy().shift(UP * 12)) for image in images],
        #     run_time=40,
        #     rate_func=linear,
        # )

        self.wait(1)
