from manim import *

from _base import MyScene
from _imports import MyColors, latex


class CurrentScenario(MyScene):
    _intro = "Current Scenario"

    _desc = [
        "The use of AI in video dubbing is not new. There are many tools available that can be used to dub videos. However, these tools are not very accurate and capable for Indian languages.",
        "Here are some examples of existing AI-powered video dubbing tools for Indian languages:",
    ]

    _examples = [
        "1. Dubverse (https://dubverse.ai/) - Cloud-based video dubbing tool however supports only 8 Indian languages and robotic voices OR no option to upload custom audio.",
        "2. Deepdub (https://deepdub.ai/) - Cloud-based video dubbing tool however less options for Indian languages and no option to upload custom audio.",
        "3. Resemble AI (https://www.resemble.ai/) - Cloud-based video dubbing tool however only supports 6 Indian languages",
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
                    12,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "not very accurate and capable for Indian languages": self.highlight_color,
                    },
                )
                .set(width=10)
                .next_to(intro, gap, buff=0.5)
                .shift(down_shift)
                .align_to(intro, LEFT)
            )
            desc.add(line)
            down_shift -= line.height + 0.2

        examples = VGroup()

        for line in self._examples:
            line = (
                latex(
                    line,
                    12,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "Dubverse": self.highlight_color,
                        "Deepdub": self.highlight_color,
                        "Resemble AI": self.highlight_color,
                        "https://dubverse.ai/": MyColors.reference_color,
                        "https://deepdub.ai/": MyColors.reference_color,
                        "https://www.resemble.ai/": MyColors.reference_color,
                    },
                )
                .set(width=10)
                .next_to(desc, DOWN)
                .align_to(desc, LEFT)
            )
            examples.add(line)

        debverse_logo = ImageMobject("images/Dubverse.png")
        deepdub_logo = ImageMobject("images/Deepdub.png")
        resemble_logo = ImageMobject("images/Resemble.png")

        debverse_logo.set(width=1.5).scale(1.5)
        deepdub_logo.set(width=1.5).scale(1.5)
        resemble_logo.set(width=1.5).scale(1.5)

        debverse_logo.next_to(examples[0], RIGHT, buff=0.5)
        deepdub_logo.next_to(examples[1], RIGHT, buff=0.5)
        resemble_logo.next_to(examples[2], RIGHT, buff=0.5)

        logos = Group(debverse_logo, deepdub_logo, resemble_logo)

        self.add(title)

        self.play(
            LaggedStartMap(FadeIn, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeIn, desc[0], lag_ratio=0.2, run_time=2),
        )
        self.wait(41)
        self.play(LaggedStartMap(FadeIn, desc[1], lag_ratio=0.2, run_time=2))
        self.wait(3.5)
        self.play(FadeIn(examples[0], shift=UP * 0.5), FadeIn(logos[0], shift=UP * 0.5))
        self.wait(9)
        self.play(
            FadeOut(examples[0], shift=UP * 0.5),
            FadeOut(logos[0], shift=UP * 0.5),
            FadeIn(examples[1], shift=UP * 0.5),
            FadeIn(logos[1], shift=UP * 0.5),
        )
        self.wait(8)
        self.play(
            FadeOut(examples[1], shift=UP * 0.5),
            FadeOut(logos[1], shift=UP * 0.5),
            FadeIn(examples[2], shift=UP * 0.5),
            FadeIn(logos[2], shift=UP * 0.5),
        )
        self.wait(5)

        self.play(
            LaggedStartMap(FadeOut, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeOut, desc, lag_ratio=0.2, run_time=2),
            LaggedStartMap(FadeOut, examples[2], lag_ratio=0.2, run_time=2),
            LaggedStartMap(FadeOut, logos[2], lag_ratio=0.2, run_time=2),
        )
