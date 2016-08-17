import numpy as np
import networkx as nx


def binary_opinion_reverse_pressure_to_conform(threshold, size, timesteps=1000,  seed=None):
    """
    This function simulates the dynamics of the process
    :param threshold: is the threshold of the model
    :param size:  number of individuals
    :param seed: seed for the random number generator
    :return:
    """

    # TODO: Make this track the evolution of the system through time

    # seed the rng
    np.random.seed(seed)
    # generate a random graph
    graph = nx.Graph(np.random.choice([0, 1], size=(size, size)))

    # generate random initial behaviour
    expressed_behaviour = np.random.choice([0, 1], size=size)

    # generate attitude -- attitude is fixed
    fixed_attitude = np.copy(expressed_behaviour)

    for _ in range(1, timesteps):
        number_of_ignorant_individuals = 0
        for node in range(size):
            neighbours = graph.neighbors(node)









