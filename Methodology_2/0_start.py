from manim import *

from _imports import latex


class AdditionalFeatures(Scene):
    def construct(self):
        additional_features = latex(
            "SwaraAI's Additional Features",
            font_size=15,
            color=WHITE,
        )

        feature_1_0 = latex(
            "1.",
            color=WHITE,
            font_size=10,
        )

        feature_1_1 = latex(
            "Video Summarization",
            color=WHITE,
            font_size=10,
        )

        feature_1_1.next_to(feature_1_0, RIGHT, buff=0.25)
        feature_1 = VGroup(feature_1_0, feature_1_1)

        feature_2 = latex(
            "2. Video Enhancement",
            color=WHITE,
            font_size=10,
        )

        feature_3 = latex(
            "3. Sign Language support (future scope)",
            color=WHITE,
            font_size=10,
        )

        features = VGroup(feature_1, feature_2, feature_3)

        additional_features.to_corner(UL, buff=1)
        features.align_to(additional_features, LEFT)
        features.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        features.next_to(additional_features, DOWN, buff=1)

        summarization_heading = latex(
            "Video Summarization",
            color=WHITE,
            font_size=15,
        )

        summarization_heading.to_corner(UL, buff=1)

        self.play(Write(additional_features))
        self.wait(0.5)
        self.play(
            LaggedStartMap(
                Write,
                features,
                lag_ratio=0.5,
            )
        )
        self.wait(2)

        self.play(
            FadeOut(additional_features),
            FadeOut(feature_2),
            FadeOut(feature_3),
            FadeOut(feature_1_0),
            Transform(feature_1_1, summarization_heading),
        )
