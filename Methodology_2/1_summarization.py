from manim import *

from _imports import video_frame, latex, MyColors


class Summarization(Scene):
    _heading = "Video Summarization"

    _desc = [
        "Video Summarization is a process of creating a short summary of a video in choosen regional language.",
        # Why is it needed?
        "It is needed because it is difficult to watch a long video and understand the content. It is also difficult to find the relevant content in a long video.",
        # How SwaraAI will handle it?
        "SwaraAI will create a time-stamped summary of the video in choosen regional language.",
        "User can click on the time-stamp to jump to the relevant part of the video. User can also ask SwaraAI questions about the video. SwaraAI will answer the questions and jump to the relevant part of the video if needed.",
    ]

    def key_frames(self):
        shift = LEFT * 0.2 + DOWN * 0.2

        frame = RoundedRectangle(
            width=8.0,
            height=4.5,
            color=WHITE,
            stroke_width=2,
            fill_opacity=1.0,
            fill_color=BLACK,
            corner_radius=0.2,
        )

        frame_2 = frame.copy().shift(shift)
        frame_3 = frame.copy().shift(shift * 2)
        frame_4 = frame.copy().shift(shift * 3)

        frames = VGroup(frame, frame_2, frame_3, frame_4)
        return frames

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
                        "Video Summarization": MyColors.highlight_color,
                        "short summary": MyColors.highlight_color,
                        "regional language": MyColors.highlight_color,
                        "time-stamped summary": MyColors.highlight_color,
                        "relevant part of the video": MyColors.highlight_color,
                        "questions": MyColors.highlight_color,
                        "answer the questions": MyColors.highlight_color,
                    },
                )
                .set(width=10)
                .next_to(heading, gap, buff=0.5)
                .shift(down_shift)
                .align_to(heading, LEFT)
            )
            desc.add(line)
            down_shift -= line.height + 0.2

        self.add(heading)
        self.play(
            LaggedStartMap(FadeIn, desc, lag_ratio=0.2, run_time=2),
        )
        self.wait(5)

        self.play(
            LaggedStartMap(FadeOut, desc, lag_ratio=0.2, run_time=2),
        )

        process_heading = latex(
            "Process",
            font_size=15,
            color=WHITE,
        )
        process_heading.next_to(heading, RIGHT, buff=0.25)

        self.play(Write(process_heading))

        process = VGroup()

        eng_video = video_frame()
        eng_video.to_edge(LEFT, buff=1)

        key_frames = self.key_frames()
        key_frames.scale(1 / 3)
        key_frames.next_to(eng_video, RIGHT * 2 + UP, buff=0.5)

        key_frames_desc = latex(
            "Key Frames",
            color=WHITE,
            font_size=6,
        ).next_to(key_frames, DOWN, buff=0.2)

        key_frames_group = VGroup(key_frames, key_frames_desc)

        eng_video_to_key_frames = Arrow(
            eng_video.get_right(),
            key_frames.get_left(),
            color=WHITE,
            buff=0.5,
        )

        eng_captions = latex(
            "English Captions",
            color=WHITE,
            font_size=10,
        )
        eng_captions.match_width(key_frames)
        eng_captions.next_to(eng_video, RIGHT * 2 + DOWN * 2, buff=0.5)

        eng_captions_to_key_frames = Arrow(
            eng_video.get_right(),
            eng_captions.get_left(),
            color=WHITE,
            buff=0.5,
        )

        reg_lang_image_caption = latex(
            "Regional Language Captions",
            color=WHITE,
            font_size=15,
        )
        reg_lang_image_caption.match_width(key_frames)
        reg_lang_image_caption.width += 1.5
        reg_lang_image_caption.next_to(key_frames, RIGHT * 2, buff=1)

        reg_lang_arrow = Arrow(
            key_frames.get_right(),
            reg_lang_image_caption.get_left(),
            color=WHITE,
            buff=0.5,
        )

        reg_lang_translated_captions = latex(
            "Translated Captions",
            color=WHITE,
            font_size=10,
        )
        reg_lang_translated_captions.match_width(key_frames)
        reg_lang_translated_captions.width += 1
        reg_lang_translated_captions.next_to(eng_captions, RIGHT * 2, buff=1)

        reg_lang_translated_arrow = Arrow(
            eng_captions.get_right(),
            reg_lang_translated_captions.get_left(),
            color=WHITE,
            buff=0.5,
        )

        final_summary = latex(
            "Final Summary",
            color=WHITE,
            font_size=10,
        )

        final_summary.match_width(key_frames)
        final_summary.next_to(reg_lang_image_caption, RIGHT * 2, buff=1)
        final_summary.shift(
            UP * (eng_video.get_center()[1] - final_summary.get_center()[1])
        )

        final_summary_arrow_1 = Arrow(
            reg_lang_image_caption.get_right(),
            final_summary.get_left(),
            color=WHITE,
            buff=0.5,
        )

        final_summary_arrow_2 = Arrow(
            reg_lang_translated_captions.get_right(),
            final_summary.get_left(),
            color=WHITE,
            buff=0.5,
        )

        process.add(
            eng_video,
            eng_video_to_key_frames,
            key_frames_group,
            eng_captions_to_key_frames,
            eng_captions,
            reg_lang_arrow,
            reg_lang_image_caption,
            reg_lang_translated_arrow,
            reg_lang_translated_captions,
            final_summary_arrow_1,
            final_summary_arrow_2,
            final_summary,
        )

        process.move_to(ORIGIN)
        process.shift(DOWN)
        process.width = 13.5

        self.play(
            LaggedStartMap(
                Write,
                process,
                lag_ratio=0.4,
                rate_func=linear,
            )
        )

        self.wait(5)

        self.play(
            LaggedStartMap(
                Unwrite,
                process[::-1],
                lag_ratio=0.4,
                rate_func=linear,
            ),
            FadeOut(process_heading),
            FadeOut(heading),
        )

        self.wait(0.5)
