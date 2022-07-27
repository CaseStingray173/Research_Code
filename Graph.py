import random
import numpy as np

# THIS FUNCTION WAS USED FOR THE PREVIOUS VERSION OF THE CODE
# NOT REQUIRED FOR THE CURRENT VERSION
# def rand_coords():
#     coordinates = []
#     for _ in range(10):
#         x = random.randint(0, 9)
#         y = random.randint(0, 9)
#         coordinates.append([x, y])
#     return np.array(coordinates)


def draw_mst(X, copy_X=True):
    if copy_X:
        X = X.copy()

    # Checks to see if the matrix is square or not
    if X.shape[0] != X.shape[1]:
        raise ValueError("X needs to be square matrix of edge weights")
    n_vertices = X.shape[0]
    spanning_edges = []

    # initialize with node 0:
    visited_vertices = [0]
    num_visited = 1
    # exclude self connections:
    diag_indices = np.arange(n_vertices)
    X[diag_indices, diag_indices] = np.inf

    while num_visited != n_vertices:
        new_edge = np.argmin(X[visited_vertices], axis=None)
        # 2d encoding of new_edge from flat, get correct indices
        new_edge = divmod(new_edge, n_vertices)
        new_edge = [visited_vertices[new_edge[0]], new_edge[1]]
        # add edge to tree
        spanning_edges.append(new_edge)
        visited_vertices.append(new_edge[1])
        # remove all edges inside current tree
        X[visited_vertices, new_edge[1]] = np.inf
        X[new_edge[1], visited_vertices] = np.inf
        num_visited += 1
    return np.vstack(spanning_edges)



