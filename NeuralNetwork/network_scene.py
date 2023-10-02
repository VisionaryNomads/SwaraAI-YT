from manim import *
import numpy as np

from .network import Network
from .network_mobject import NetworkMobject


class NetworkScene(Scene):
    layer_sizes = [8, 6, 6, 4]
    network_mob_config = {}

    weights_text = Text("Loading weights...").scale(0.5)
    inference_text = Text("Inference...").scale(0.5)
    model_text = None

    whole_network = None

    def setup(self):
        self.add_network()
        self.weights_text.move_to(self.network_mob.get_top() + UP * 0.5)
        self.inference_text.move_to(self.weights_text.get_center())

    def set_model_name(self, name):
        self.model_text = Text(name).scale(0.7)
        self.model_text.move_to(self.network_mob.get_bottom() + DOWN * 0.7)

    def load_network(self):
        self.play(Write(self.model_text), run_time=0.5)
        self.play(Write(self.weights_text), Write(self.network_mob.layers))
        self.play(Write(self.network_mob.edge_groups))

    def inference(self):
        self.play(ReplacementTransform(self.weights_text, self.inference_text))
        self.feed_forward(np.random.random(self.layer_sizes[0]))

    def add_network(self):
        self.network = Network(sizes=self.layer_sizes)
        self.network_mob = NetworkMobject(self.network, **self.network_mob_config)

    def feed_forward(self, input_vector, false_confidence=False, added_anims=None):
        if added_anims is None:
            added_anims = []

        activations = self.network.get_activation_of_all_layers(input_vector)

        if false_confidence:
            i = np.argmax(activations[-1])
            activations[-1] *= 0
            activations[-1][i] = 1.0

        for i, activation in enumerate(activations):
            self.show_activation_of_layer(i, activation, added_anims)
            added_anims = []

    def show_activation_of_layer(
        self, layer_index, activation_vector, added_anims=None
    ):
        if added_anims is None:
            added_anims = []

        layer = self.network_mob.layers[layer_index]
        active_layer = self.network_mob.get_active_layer(layer_index, activation_vector)
        anims = [Transform(layer, active_layer)]

        if layer_index > 0:
            anims_i = self.network_mob.get_edge_propogation_animations(layer_index - 1)
            anims.extend(anims_i)

        anims += added_anims
        self.play(*anims)
