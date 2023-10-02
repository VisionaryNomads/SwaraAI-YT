from manim import *
import numpy as np
import copy

from .network import Network


class NetworkMobject(VGroup):
    neuron_radius = 0.15
    neuron_to_neuron_buff = MED_SMALL_BUFF
    layer_to_layer_buff = LARGE_BUFF
    neuron_stroke_color = YELLOW
    neuron_stroke_width = 3
    neuron_fill_color = YELLOW
    edge_color = GREY_D
    edge_stroke_width = 2
    edge_propogation_color = YELLOW
    edge_propogation_time = 1
    max_shown_neurons = 16
    brace_for_large_layers = True
    average_shown_activation_of_large_layer = True
    include_output_labels = False

    def __init__(self, neural_network: Network, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.neural_network = neural_network
        self.layer_sizes = neural_network.sizes
        self.add_neurons()
        self.add_edges()

    def add_neurons(self):
        layers = VGroup(*[self.get_layer(size) for size in self.layer_sizes])
        layers.arrange(RIGHT, buff=self.layer_to_layer_buff)
        self.layers = layers
        self.add(self.layers)
        if self.include_output_labels:
            self.add_output_labels()

    def get_layer(self, size):
        layer = VGroup()
        n_neurons = size
        if n_neurons > self.max_shown_neurons:
            n_neurons = self.max_shown_neurons

        neurons = VGroup(
            *[
                Circle(
                    radius=self.neuron_radius,
                    stroke_color=self.neuron_stroke_color,
                    stroke_width=self.neuron_stroke_width,
                    fill_color=self.neuron_fill_color,
                    fill_opacity=0,
                )
                for _ in range(n_neurons)
            ]
        )
        neurons.arrange(DOWN, buff=self.neuron_to_neuron_buff)
        for neuron in neurons:
            neuron.edges_in = VGroup()
            neuron.edges_out = VGroup()
        layer.neurons = neurons
        layer.add(neurons)

        if size > n_neurons:
            dots = Tex("\\vdots")
            dots.move_to(neurons)

            VGroup(*neurons[: len(neurons) // 2]).next_to(dots, UP, MED_SMALL_BUFF)
            VGroup(*neurons[len(neurons) // 2 :]).next_to(dots, DOWN, MED_SMALL_BUFF)

            layer.dots = dots
            layer.add(dots)

            if self.brace_for_large_layers:
                brace = Brace(layer, LEFT)
                brace_label = brace.get_tex(str(size))
                layer.brace = brace
                layer.brace_label = brace_label
                layer.add(brace, brace_label)

        return layer

    def add_edges(self):
        self.edge_groups = VGroup()

        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            neuron_pairs = [(n1, n2) for n1 in l1.neurons for n2 in l2.neurons]

            for n1, n2 in neuron_pairs:
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)

            self.edge_groups.add(edge_group)
        self.add_to_back(self.edge_groups)

    def get_edge(self, neuron1, neuron2):
        return Line(
            neuron1.get_center(),
            neuron2.get_center(),
            buff=self.neuron_radius * 1.1,
            stroke_color=self.edge_color,
            stroke_width=self.edge_stroke_width,
        )

    def get_active_layer(self, layer_index, activation_vector):
        layer = copy.deepcopy(self.layers[layer_index])
        self.activate_layer(layer, activation_vector)
        return layer

    def activate_layer(self, layer, activation_vector):
        n_neurons = len(layer.neurons)
        av = activation_vector

        def arr_to_num(arr):
            return (np.sum(arr > 0.1) / float(len(arr))) ** (1.0 / 3)

        if len(av) > n_neurons:
            if self.average_shown_activation_of_large_layer:
                indices = np.arange(n_neurons)
                indices *= int(len(av) / n_neurons)
                indices = list(indices)
                indices.append(len(av))
                av = np.array(
                    [arr_to_num(av[i1:i2]) for i1, i2 in zip(indices[:-1], indices[1:])]
                )

            else:
                av = np.append(
                    av[: n_neurons / 2],
                    av[-n_neurons / 2 :],
                )

        for activation, neuron in zip(av, layer.neurons):
            neuron.set_fill(color=self.neuron_fill_color, opacity=activation)

        return layer

    def get_edge_propogation_animations(self, index):
        edge_group_copy = self.edge_groups[index].copy()
        edge_group_copy.set_stroke(
            self.edge_propogation_color, width=1.5 * self.edge_stroke_width
        )

        return [
            ShowCreationThenFadeOut(
                edge_group_copy, run_time=self.edge_propogation_time, lag_ratio=0.5
            )
        ]
