import numpy as np
import networkx as nx


def binary_opinion(size, pressure_to_conform_function, threshold, graph=None, timesteps=1000, seed=None):

    """
    This function simulates the dynamics of the process
    :param threshold: is the threshold of the model
    :param size:  number of individuals
    :param seed: seed for the random number generator
    :param pressure_to_conform_function: a function from [0, 1] into [0, 1]
    :param threshold: Threshold value
    :param timesteps: timesteps
    :return:
    """

    # TODO: Make this track the evolution of the system through time

    # seed the rng
    np.random.seed(seed)
    # generate a random graph
    if graph is None:
        graph = nx.Graph(np.random.choice([0, 1], size=(size, size)))
    else:
        assert len(graph) == size

    # generate random initial behaviour
    expressed_behaviour = np.random.choice([0, 1], size=size)

    # generate attitude -- attitude is fixed
    fixed_attitude = np.copy(expressed_behaviour)

    ans = []

    for _ in range(1, timesteps):
        number_of_ignorant_individuals = 0
        for node in range(size):
            neighbours = graph.neighbors(node)
            # IMPORTANT ASSUME EXPRESSED BEHAVIOUR DOES NOT CHANGE
            # IF ONLY ONE NEIGHBOUR OR NO NEIGHBOURS

            ratio_0 = 0.0
            my_expressed_behaviour = expressed_behaviour[node]

            ratio = 0.0
            number_of_neighbours = len(neighbours)
            for index_neighbour in neighbours:
                if expressed_behaviour[index_neighbour] == 1 - my_expressed_behaviour:
                        ratio += 1/ number_of_neighbours

            # pressure
            pressure_to_change = pressure_to_conform_function(ratio)
            if pressure_to_change > threshold:
                expressed_behaviour[node] = 1 - expressed_behaviour[node]

        for i in range(len(expressed_behaviour)):
            if expressed_behaviour[i] != fixed_attitude[i]:
                number_of_ignorant_individuals += 1
        ans.append(number_of_ignorant_individuals)
    return ans


















