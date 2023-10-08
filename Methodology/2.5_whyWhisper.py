from manim import *

from _imports import MyColors, latex


class WhyWhisper(Scene):
    _intro = "Why Whisper?"

    _desc = [
        "Whisper is an automatic speech recognition (ASR) system developed by OpenAI.",
        "Whisper approaches human level robustness and accuracy on English speech recognition.",
        "As it is trained on 680,000 hours of multilingual and multitask supervised data, it enables transcription in multiple languages, as well as translation from those languages into English.",
    ]
    _ref = "https://openai.com/research/whisper/"

    def construct(self):
        gap = DOWN * 0.5

        intro = (
            latex(
                self._intro,
                15,
                color=WHITE,
                tex_environment="flushleft",
                tex_to_color_map={
                    "Whisper": MyColors.highlight_color,
                },
            )
            .to_corner(UL, buff=1)
            .shift(UP * 0.5)
        )

        down_shift = 0
        desc = VGroup()
        for line in self._desc:
            line = (
                latex(
                    line,
                    10,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "automatic speech recognition (ASR) system": MyColors.highlight_color,
                        "human level robustness and accuracy on English speech recognition": MyColors.highlight_color,
                        "enables transcription in multiple languages, as well as translation from those languages into English": MyColors.highlight_color,
                    },
                )
                .set(width=12)
                .next_to(intro, gap, buff=0.5)
                .shift(down_shift)
                .align_to(intro, LEFT)
            )
            desc.add(line)
            down_shift -= line.height + 0.2

        whisper_svg = SVGMobject("assets/images/whisper.svg")
        whisper_svg.width = 12
        whisper_svg.next_to(desc, DOWN, buff=0.3)
        whisper_svg.align_to(desc, LEFT)

        ref = latex(
            self._ref,
            4,
            color=MyColors.reference_color,
            tex_environment="flushleft",
        )

        ref_ul = Underline(
            ref,
            buff=0.05,
            stroke_width=1,
            color=MyColors.reference_color,
        )

        reference = VGroup(ref, ref_ul)
        reference.to_corner(DL, buff=0.5)
        reference.shift(RIGHT * 0.5)

        self.play(Write(intro))
        self.play(
            LaggedStart(
                *[FadeIn(line, shift=UP * 0.5) for line in desc],
                lag_ratio=0.1,
                run_time=3,
            )
        )
        self.play(Write(whisper_svg))
        self.play(FadeIn(reference))
        self.wait(5)
        self.play(
            LaggedStartMap(
                FadeOut,
                VGroup(intro, desc, whisper_svg, reference),
                lag_ratio=0.1,
                run_time=2,
            )
        )
