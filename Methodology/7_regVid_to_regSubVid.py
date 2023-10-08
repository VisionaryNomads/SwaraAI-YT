from manim import *

from _imports import RenderNetwork, video_frame


class RV2RSV(RenderNetwork):
    def nn_name(self):
        return "Adding regional language subtitles \n          to video using OpenCV"

    def nn_input(self):
        video = video_frame()

        video_label = Text("Lip Synced Video in \n Regional Language")
        video_label.next_to(video, DOWN).scale(0.5)

        return VGroup(video, video_label)

    def nn_output(self):
        video = video_frame(True)

        video_label = Text("Regional Subtitled \n    Dubbed Video")
        video_label.next_to(video, DOWN).scale(0.5)

        return VGroup(video, video_label)

    def fade_start(self):
        return True

    def fade_end(self):
        return False

    def slide_output(self):
        return False
