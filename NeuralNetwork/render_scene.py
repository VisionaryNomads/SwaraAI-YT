from manim import *
import numpy as np

from .network_scene import NetworkScene


class RenderNetwork(NetworkScene):
    __nn_input = None
    __nn_output = None

    _nn_left = None
    _nn_right = None

    _io_height = 3
    _io_small_height = 1.5

    def nn_name(self):
        """Returns the name of the neural network"""
        return None

    def nn_input(self):
        """Returns the input of the neural network as a mobject"""
        return None

    def nn_output(self):
        """Returns the output of the neural network as a mobject"""
        return None

    def fade_start(self):
        """Returns whether the input should fade in"""
        return False

    def fade_end(self):
        """Returns whether the output should fade out"""
        return False

    def slide_output(self):
        """Returns whether the output should slide to next scene input"""
        return False

    def add_nn_input(self):
        """Returns whether the input should be added to the scene"""
        return True

    def _nn_input(self):
        if self.__nn_input is None:
            self.__nn_input = self.nn_input()

        return self.__nn_input

    def _nn_output(self):
        if self.__nn_output is None:
            self.__nn_output = self.nn_output()

        return self.__nn_output

    def get_left_coord(self, mobject):
        super().setup()
        width = mobject.width
        return self.network_mob.get_left() + LEFT * width / 2 + LEFT

    def get_right_coord(self, mobject):
        super().setup()
        width = mobject.width
        return self.network_mob.get_right() + RIGHT * width / 2 + RIGHT

    def setup(self):
        super().setup()
        if self.nn_name() is not None:
            self.set_model_name(self.nn_name())

        if self._nn_input() is not None and self._nn_output() is not None:
            nn_input_width = self._nn_input().get_width()
            nn_output_width = self._nn_output().get_width()

            self._nn_left = self.network_mob.get_left() + LEFT * nn_input_width / 2
            self._nn_right = self.network_mob.get_right() + RIGHT * nn_output_width / 2

            self._nn_input().move_to(self._nn_left + LEFT)
            self._nn_output().move_to(self._nn_right + RIGHT)

    def construct(self):
        self.setup()

        if self.add_nn_input():
            if self.fade_start():
                self.play(FadeIn(self._nn_input()))
            else:
                self.add(self._nn_input())
                self.wait(1)

        self.load_network()

        nn_input_copy = self._nn_input().copy()
        nn_input_copy.move_to(self._nn_left + RIGHT * self._nn_input().get_width() / 2)
        nn_input_copy.set_height(self._io_small_height)
        nn_input_copy.set_opacity(0)

        self.play(TransformFromCopy(self._nn_input(), nn_input_copy))
        self.inference()

        nn_output_copy = self._nn_output().copy()
        nn_output_copy.move_to(
            self._nn_right + LEFT * self._nn_output().get_width() / 2
        )
        nn_output_copy.set_height(self._io_small_height)
        nn_output_copy.set_opacity(0)

        self.play(Transform(nn_output_copy, self._nn_output()))
        self.wait(2)

        self.play(
            FadeOut(self._nn_input()),
            FadeOut(self.network_mob),
            FadeOut(self.inference_text),
            FadeOut(self.model_text),
        )

        if self.slide_output():
            self.play(
                Transform(
                    nn_output_copy,
                    self._nn_output()
                    .copy()
                    .move_to(
                        self.network_mob.get_left()
                        + LEFT * self._nn_output().get_width() * 0.5
                        + LEFT
                    ),
                )
            )

        elif self.fade_end():
            self.play(FadeOut(nn_input_copy), FadeOut(nn_output_copy))
