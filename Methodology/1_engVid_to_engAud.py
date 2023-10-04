from manim import *

from _imports import RenderNetwork, video_frame, audio_wave


class EV2EA(RenderNetwork):
    def nn_name(self):
        return "Video to Audio"

    def nn_input(self):
        video = video_frame()

        video_label = Text("English Video")
        video_label.next_to(video, DOWN).scale(0.5)

        return VGroup(video, video_label)

    def nn_output(self):
        audio = audio_wave(0, 4)

        label = Text("English Audio")
        label.next_to(audio, DOWN).scale(0.5)

        return VGroup(audio, label)

    def slide_output(self):
        return True
