from manim import *
import os
import cv2

from _base import MyScene
from _imports import video_frame, latex


class Example(MyScene):
    _desc = [
        "Let's see an example dubbed video to understand how it works.",
    ]

    def construct(self):
        gap = DOWN * 1.5

        title = self.get_title()

        down_shift = 0
        desc = VGroup()
        for line in self._desc:
            line = (
                latex(
                    line,
                    16,
                    color=WHITE,
                    tex_environment="flushleft",
                )
                .set(width=8)
                .next_to(title, gap, buff=0.5)
                .shift(down_shift)
                .align_to(title, LEFT)
            )
            desc.add(line)
            down_shift -= line.height + 0.2

        hin_video = video_frame(add_subtitle=True)
        hin_text = Text("हिंदी वीडियो (Hindi)", color=WHITE, font="Sans", font_size=15)
        hin_text.next_to(hin_video, DOWN, buff=0.2)
        hin_vid_text = VGroup(hin_video, hin_text)
        hin_vid_text.to_corner(DR, buff=1)
        hin_vid_text.shift(DOWN * 0.25)
        hin_rect = SurroundingRectangle(
            hin_vid_text, color=BLUE, buff=0.2, corner_radius=0.1, stroke_width=2
        )
        hin_grp = VGroup(hin_vid_text, hin_rect)

        big_video = video_frame(add_subtitle=True, corner_radius=0)
        big_video.set(width=10)
        big_video_text = Text(
            "हिंदी वीडियो (Hindi)", color=WHITE, font="Sans", font_size=25
        )
        big_video_text.next_to(big_video, DOWN, buff=0.2)
        big_video_grp = VGroup(big_video, big_video_text)
        big_video_grp.move_to(ORIGIN)
        big_video_rect = SurroundingRectangle(
            big_video_grp, color=BLUE, buff=0.2, corner_radius=0.1, stroke_width=2
        )
        big_video_grp = VGroup(big_video_grp, big_video_rect)

        ja_video = []

        current_dir = os.path.dirname(os.path.realpath(__file__))
        os.chdir(current_dir)

        cap = cv2.VideoCapture("../assets/videos/JA_Dub.mp4")

        # Frame rate
        ja_video_frame_rate = cap.get(cv2.CAP_PROP_FPS)

        # Number of frames in the video file
        ja_video_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # First frame
        first_frame = cap.read()[1]
        first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2RGB)
        first_frame = ImageMobject(first_frame)
        first_frame.match_width(big_video)
        first_frame.move_to(big_video.get_center())
        ja_video.append(first_frame)

        # Last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, ja_video_frames - 1)
        last_frame = cap.read()[1]
        last_frame = cv2.cvtColor(last_frame, cv2.COLOR_BGR2RGB)
        last_frame = ImageMobject(last_frame)
        last_frame.match_width(big_video)
        last_frame.move_to(big_video.get_center())
        ja_video.append(last_frame)

        # flag = True
        # while flag:
        #     flag, frame = cap.read()
        #     if flag:
        #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #         frame_img = ImageMobject(frame)
        #         frame_img.match_width(big_video)
        #         frame_img.move_to(big_video.get_center())
        #         ja_video.append(frame_img)

        cap.release()

        self.add(title, hin_grp)
        self.wait(0.5)

        self.play(
            LaggedStartMap(FadeIn, desc, lag_ratio=0.1),
        )
        self.wait(2)

        self.play(
            FadeOut(title),
            FadeOut(desc),
            Transform(hin_grp, big_video_grp, run_time=2),
        )

        self.wait(0.5)

        # print(f"Total frames: {len(ja_video)}")

        self.play(FadeIn(ja_video[0]))
        # self.wait(1 / ja_video_frame_rate)

        # for frame_no in range(1, len(ja_video)):
        #     self.add(ja_video[frame_no])
        #     self.wait(1 / ja_video_frame_rate)

        #     if frame_no % (len(ja_video) // 20) == 0:
        #         percent = frame_no / len(ja_video) * 100
        #         print(
        #             "["
        #             + "=" * int(percent // 5)
        #             + ">"
        #             + " " * (20 - int(percent // 5))
        #             + "]",
        #             f"{int(percent)}%",
        #         )

        wait_time = ja_video_frames / ja_video_frame_rate

        self.wait(wait_time / 2)
        self.add(ja_video[1])
        self.wait(wait_time / 2)

        self.wait(0.5)

        whole_screen_black = Rectangle(
            width=14,
            height=8,
            color=BLACK,
            fill_opacity=1,
        )

        self.play(FadeIn(whole_screen_black, run_time=2))
        self.wait(0.25)
