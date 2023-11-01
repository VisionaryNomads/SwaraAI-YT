from manim import *

from _base import MyScene
from _imports import latex


class Team(MyScene):
    _intro = "Meet the Team"

    def construct(self):
        title = self.get_title()
        intro = (
            latex(
                self._intro,
                10,
                color=WHITE,
                tex_environment="flushleft",
            )
            .next_to(title, RIGHT * 3.5, buff=0.5)
            .align_to(title, ORIGIN)
        )

        size = 2

        images = [["gopal", "riddhi", "naman"], ["parth", "ritesh", "prem"]]
        names = [
            ["Gopal Saraf", "Riddhi Sabane", "Naman Labhsetwar"],
            ["Parth Sali", "Ritesh Mahajan", "Prem Gaikwad"],
        ]

        images_objects = [
            [
                Group(
                    ImageMobject("images/team/{}".format(name)).set(
                        width=size, height=size
                    ),
                    Text(
                        names[0][i],
                        color=WHITE,
                        font_size=25,
                        font="Arial",
                    ).shift(DOWN * size * 0.7),
                )
                for i, name in enumerate(images[0])
            ],
            [
                Group(
                    ImageMobject("images/team/{}".format(name)).set(
                        width=size, height=size
                    ),
                    Text(
                        names[1][i],
                        color=WHITE,
                        font_size=25,
                        font="Arial",
                    ).shift(DOWN * size * 0.7),
                )
                for i, name in enumerate(images[1])
            ],
        ]

        images_group_1 = Group(*images_objects[0]).arrange(RIGHT, buff=1.5)
        images_group_2 = Group(*images_objects[1]).arrange(RIGHT, buff=1.5)

        images_group = (
            Group(images_group_1, images_group_2)
            .move_to(ORIGIN)
            .arrange(DOWN, buff=0.25)
        )

        images_group.shift(DOWN * 1)

        names_labels_1 = [Text(name, color=WHITE) for name in names[0]]
        names_labels_2 = [Text(name, color=WHITE) for name in names[1]]

        for label, image in zip(names_labels_1, images_objects[0]):
            label.next_to(image, DOWN)
        for label, image in zip(names_labels_2, images_objects[1]):
            label.next_to(image, DOWN)

        self.add(title)
        self.play(LaggedStartMap(FadeIn, intro, lag_ratio=0.2, run_time=1))
        self.play(LaggedStartMap(FadeIn, images_group[0], lag_ratio=0.2, run_time=1))
        self.play(LaggedStartMap(FadeIn, images_group[1], lag_ratio=0.2, run_time=1))
        self.wait(4)
        self.play(
            LaggedStartMap(FadeOut, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeOut, images_group, lag_ratio=0.2, run_time=1),
        )
