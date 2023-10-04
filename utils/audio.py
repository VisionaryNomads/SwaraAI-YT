from manim import *
import numpy as np


def audio_wave(start=0, end=4):
    func = lambda x: abs(sum([(1.0 / n) * np.sin((n + 3) * x) for n in range(1, 5)]))
    audio = VGroup(
        *[Line(func(x) * DOWN, func(x) * UP) for x in np.arange(start, end, 0.1)]
    )
    audio.set_stroke(width=2)
    audio.arrange(RIGHT, buff=MED_SMALL_BUFF)
    audio.set(height=1)

    return audio
