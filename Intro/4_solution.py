from manim import *

from _base import MyScene
from _imports import video_frame


class Solution(MyScene):
    _intro = "Solution"

    _desc = [
        "SwaraAI provides a solution to this problem. It allows users to quickly and easily dub videos into other Indian regional languages.",
        "The software produces a voiceover in a human-like voice, as well as text supers that are dubbed from English to other Indian regional languages.",
        "The translated voiceover is also in simple language, easy to understand, and not colloquial in nature.",
    ]

    def construct(self):
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
                        "quickly and easily dub videos": self.highlight_color,
                        "human-like voice": self.highlight_color,
                        "text supers": self.highlight_color,
                        "simple language, easy to understand, and not colloquial in nature": self.highlight_color,
                    },
                )
                .set(width=8)
                .next_to(intro, gap, buff=0.5)
                .shift(down_shift)
                .align_to(intro, LEFT)
            )
            desc.add(line)
            down_shift -= line.height + 0.2

        eng_video = video_frame()
        hin_video = video_frame(add_subtitle=True)

        eng_text = Text("English Video", color=WHITE, font="Sans", font_size=15)
        hin_text = Text("हिंदी वीडियो (Hindi)", color=WHITE, font="Sans", font_size=15)

        eng_text.next_to(eng_video, DOWN, buff=0.2)
        hin_text.next_to(hin_video, DOWN, buff=0.2)

        eng_vid_text = VGroup(eng_video, eng_text)
        hin_vid_text = VGroup(hin_video, hin_text)

        eng_vid_text.to_corner(UR, buff=1)
        hin_vid_text.to_corner(DR, buff=1)

        eng_vid_text.shift(UP * 0.25)
        hin_vid_text.shift(DOWN * 0.25)

        eng_rect = SurroundingRectangle(
            eng_vid_text, color=BLUE, buff=0.2, corner_radius=0.1, stroke_width=2
        )

        hin_rect = SurroundingRectangle(
            hin_vid_text, color=BLUE, buff=0.2, corner_radius=0.1, stroke_width=2
        )

        upload_button_text = Text("Upload Video", color=WHITE, font_size=15)
        upload_button_box = SurroundingRectangle(
            upload_button_text,
            color=WHITE,
            buff=0.2,
            corner_radius=0.05,
            stroke_width=1,
        )

        upload_btn = VGroup(upload_button_box, upload_button_text)
        upload_btn.move_to(eng_rect)

        select_lang = Text("Select Language", color=WHITE, font_size=15)
        select_voice = Text("Select Voice", color=WHITE, font_size=15)

        arrow = Arrow(
            eng_vid_text.get_bottom(),
            hin_vid_text.get_top(),
            color=GRAY_B,
            buff=0.4,
        )

        dubbing_text = Text("Dubbing", color=GRAY_B, font_size=15)
        dubbing_text.rotate(90 * DEGREES)
        dubbing_text.next_to(arrow, LEFT, buff=0.2)
        arrow_text = VGroup(arrow, dubbing_text)

        small_eng_vid_text = eng_vid_text.copy().scale(0.5)
        small_eng_vid_text.move_to(
            eng_vid_text.get_top() + DOWN * small_eng_vid_text.height / 2
        )

        select_lang.move_to(small_eng_vid_text.get_bottom() + DOWN * 0.5)
        select_voice.move_to(select_lang.get_center())

        languages = [
            "मराठी वीडियो (Marathi)",
            "ગુજરાતી વિડિઓ (Gujarati)",
            "తెలుగు వీడియో (Telugu)",
            "ਪੰਜਾਬੀ ਵੀਡੀਓ (Punjabi)",
            "বাংলা ভিডিও (Bengali)",
            "ଓଡ଼ିଆ ଭିଡ଼ିଓ (Odia)",
            "ಕನ್ನಡ ವೀಡಿಯೊ (Kannada)",
            "தமிழ் வீடியோ (Tamil)",
            "മലയാളം വീഡിയോ (Malayalam)",
            "मैथिली वीडियो (Maithili)",
            "मणिपुरी वीडियो (Manipuri)",
            "कोंकणी व्हिडिओ (Konkani)",
            "বোডো ভিডিও (Bodo)",
            "डोगरी वीडियो (Dogri)",
            "असमिया भिडिओ (Assamese)",
            "ਸੰਥਾਲੀ ਵੀਡੀਓ (Santali)",
            "संस्कृत वीडियो (Sanskrit)",
            "नेपाली भिडिओ (Nepali)",
            "हिंदी वीडियो (Hindi)",
        ]

        self.add(title)
        self.play(
            LaggedStartMap(FadeIn, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeIn, desc, lag_ratio=0.2, run_time=2),
        )
        self.wait(0.5)
        self.play(
            Create(eng_rect),
            Write(upload_btn),
        )
        self.wait(0.5)
        # Circumscribe
        self.play(Circumscribe(upload_btn, color=YELLOW, run_time=1.5, buff=0.2))
        # self.play(Flash(upload_btn, color=WHITE, line_length=0.2, flash_radius=0.5))
        self.wait(0.5)
        self.play(
            FadeOut(upload_btn, run_time=0.25),
            Write(small_eng_vid_text),
            Write(select_lang),
        )
        self.wait(0.5)
        self.play(Circumscribe(select_lang, color=YELLOW, run_time=1.5, buff=0.2))
        # self.play(Flash(select_lang, color=WHITE, flash_radius=0.6))
        self.wait(0.5)
        self.play(
            FadeOut(select_lang, shift=UP * 0.25), FadeIn(select_voice, shift=UP * 0.25)
        )
        self.wait(0.5)
        self.play(Circumscribe(select_voice, color=YELLOW, run_time=1.5, buff=0.2))
        # self.play(Flash(select_voice, color=WHITE, flash_radius=0.6))
        self.wait(0.5)
        self.play(
            FadeOut(select_voice, run_time=0.5),
            Transform(small_eng_vid_text, eng_vid_text),
        )
        self.play(Write(arrow_text))
        self.play(Write(hin_vid_text), Create(hin_rect))

        prev = hin_text
        for lang in languages:
            text = Text(lang, color=WHITE, font="Sans", font_size=15).move_to(prev)
            self.play(
                FadeOut(prev, shift=UP * 0.25),
                FadeIn(text, shift=UP * 0.25),
            )
            prev = text
            self.wait(0.5)

        self.wait(1)

        # dubbing = VGroup(
        #     small_eng_vid_text, eng_rect, arrow_text, hin_vid_text, prev, hin_rect
        # )

        self.play(
            LaggedStartMap(FadeOut, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeOut, desc, lag_ratio=0.2, run_time=2),
            # LaggedStartMap(FadeOut, dubbing, lag_ratio=0.2, run_time=1),
            Unwrite(small_eng_vid_text, run_time=1.5),
            Unwrite(eng_rect, run_time=1.5),
            Unwrite(arrow_text, run_time=1.5),
        )
