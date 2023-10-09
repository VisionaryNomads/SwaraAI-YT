from manim import *
import os
import cv2

from _imports import video_frame, latex


class AnotherExample(MovingCameraScene):
    _intro = "Let's see another example dubbed video."

    def construct(self):
        intro = latex(
            self._intro,
            10,
            color=WHITE,
            tex_environment="flushleft",
        ).to_corner(UL, buff=1)

        # Frame 1
        eng_video = video_frame(corner_radius=0)
        eng_video.set(width=10)
        eng_video_text = Text("English Video", color=WHITE, font="Sans", font_size=25)
        eng_video_text.next_to(eng_video, DOWN, buff=0.2)
        eng_video_grp = VGroup(eng_video, eng_video_text)
        eng_video_grp.move_to(ORIGIN)

        eng_video_rect = SurroundingRectangle(
            eng_video_grp, color=BLUE, buff=0.2, corner_radius=0.1, stroke_width=2
        )
        eng_video_grp = VGroup(eng_video_grp, eng_video_rect)

        # Frame 2
        hin_video = video_frame(add_subtitle=True, corner_radius=0)
        hin_video.set(width=10)
        hin_video_text = Text(
            "हिंदी वीडियो (Hindi)", color=WHITE, font="Sans", font_size=25
        )
        hin_video_text.next_to(hin_video, DOWN, buff=0.2)
        hin_video_grp = VGroup(hin_video, hin_video_text)
        hin_video_grp.move_to(ORIGIN)

        hin_video_rect = SurroundingRectangle(
            hin_video_grp, color=BLUE, buff=0.2, corner_radius=0.1, stroke_width=2
        )
        hin_video_grp = VGroup(hin_video_grp, hin_video_rect)

        hin_video_grp.shift(RIGHT * 14)

        # Arrow
        arrow = Arrow(
            eng_video_grp.get_right(),
            hin_video_grp.get_left(),
            color=GRAY_B,
            stroke_width=2,
        )

        current_dir = os.path.dirname(os.path.realpath(__file__))
        os.chdir(current_dir)

        ab_video_eng = []

        cap = cv2.VideoCapture("../assets/videos/AB.mp4")

        # Frame rate
        ab_video_eng_frame_rate = cap.get(cv2.CAP_PROP_FPS)

        # Number of frames in the video file
        ab_video_eng_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # First frame
        first_frame = cap.read()[1]
        first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2RGB)
        first_frame = ImageMobject(first_frame)
        first_frame.match_width(eng_video)
        first_frame.move_to(eng_video.get_center())
        ab_video_eng.append(first_frame)

        # Last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, ab_video_eng_frames - 1)
        last_frame = cap.read()[1]
        last_frame = cv2.cvtColor(last_frame, cv2.COLOR_BGR2RGB)
        last_frame = ImageMobject(last_frame)
        last_frame.match_width(eng_video)
        last_frame.move_to(eng_video.get_center())
        ab_video_eng.append(last_frame)

        cap.release()

        ab_video_hin = []

        cap = cv2.VideoCapture("../assets/videos/AB_Dub.mov")

        # Frame rate
        ab_video_hin_frame_rate = cap.get(cv2.CAP_PROP_FPS)

        # Number of frames in the video file
        ab_video_hin_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # First frame
        first_frame = cap.read()[1]
        first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2RGB)
        first_frame = ImageMobject(first_frame)
        first_frame.match_width(hin_video)
        first_frame.move_to(hin_video.get_center())
        ab_video_hin.append(first_frame)

        # Last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, ab_video_hin_frames - 1)
        last_frame = cap.read()[1]
        last_frame = cv2.cvtColor(last_frame, cv2.COLOR_BGR2RGB)
        last_frame = ImageMobject(last_frame)
        last_frame.match_width(hin_video)
        last_frame.move_to(hin_video.get_center())
        ab_video_hin.append(last_frame)

        cap.release()

        self.play(Write(intro))
        self.wait(0.5)
        self.play(FadeOut(intro))
        self.play(FadeIn(eng_video_grp))
        self.wait(0.5)

        wait_time = ab_video_eng_frames / ab_video_eng_frame_rate

        self.play(FadeIn(ab_video_eng[0]))
        self.wait(wait_time / 2)
        self.add(ab_video_eng[1])
        self.wait(wait_time / 2)

        self.wait(0.5)

        self.play(GrowArrow(arrow))

        self.play(self.camera.frame.animate.shift(RIGHT * 14), run_time=1)
        self.play(FadeIn(hin_video_grp))
        self.wait(0.5)

        wait_time = ab_video_hin_frames / ab_video_hin_frame_rate

        self.play(FadeIn(ab_video_hin[0]))
        self.wait(wait_time / 2)
        self.add(ab_video_hin[1])
        self.wait(wait_time / 2)

        self.wait(0.5)

        whole_screen_black = Rectangle(
            width=14,
            height=8,
            color=BLACK,
            fill_opacity=1,
        ).shift(RIGHT * 14)

        self.play(FadeIn(whole_screen_black, run_time=2))
        self.wait(0.25)
