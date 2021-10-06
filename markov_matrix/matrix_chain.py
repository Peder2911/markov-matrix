from typing import Tuple
from numpy.typing import ArrayLike
import numpy as np

def normalize(mat, axis = 0):
    return mat / mat.sum(axis=axis)

def matrix_chain(
        transition_matrix: ArrayLike,
        shape: Tuple[int, int] = (10,10),
        homogenization_factor: float = .1):

    assert transition_matrix.shape[0] == transition_matrix.shape[1]

    n_states = transition_matrix.shape[0]
    states = np.linspace(0, n_states-1, n_states, dtype=int)
    current = 0

    base_tm = normalize(transition_matrix,axis=1)

    mat = np.zeros(shape, dtype = int)
    cells = mat.ravel()
    while True:
        for idx, current in enumerate(cells):
            current_p = base_tm[current, :]
            cells[idx] = np.random.choice(states, p = current_p)
        yield mat.copy()
