from manim import *

from _imports import RenderNetwork, video_frame, audio_wave


class RVCA2RV(RenderNetwork):
    audio_group = None
    video_group = None

    def nn_name(self):
        return "Syncronizing cloned audio and \n lip movement using Wav2Lip"

    def nn_input(self):
        audio = audio_wave(2, 6)
        audio_label = Text("Cloned Regional Audio")
        audio_label.move_to(self.get_left_coord(audio_label))
        audio_label.next_to(audio, DOWN).scale(0.5)
        audio_group = VGroup(audio, audio_label)

        self.audio_group = audio_group

        video = video_frame()
        video_label = Text("Input Video")
        video_group = VGroup(video, video_label)
        video_label.next_to(video, DOWN).scale(0.5)
        self.video_group = video_group

        return VGroup(audio_group, video_group)

    def nn_output(self):
        video = video_frame()

        video_label = Text("Lip Synced Video in \n Regional Language")
        video_label.next_to(video, DOWN).scale(0.5)

        return VGroup(video, video_label)

    def fade_start(self):
        return True

    def fade_end(self):
        return True

    def add_nn_input(self):
        return False

    def construct(self):
        self.play(FadeIn(self.audio_group))
        self.wait(1)

        video_height = self.video_group.height / 2
        self.video_group.shift(UP * video_height + DOWN * 0.20)

        self.play(
            self.audio_group.animate.shift(DOWN * video_height + DOWN * 0.20),
            FadeIn(self.video_group, shift=DOWN * 2),
        )

        super().construct()
