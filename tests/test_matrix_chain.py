
from itertools import islice
import numpy as np
from unittest import TestCase
from markov_matrix import matrix_chain

class TestMatrixChain(TestCase):
    def test_matrix_chain(self):
        chain = matrix_chain(np.array([
                [ .8 , .2 , .0 ,],
                [ .1 , .8 , .1 ,],
                [ .0 ,1.0 , .0 ,],
            ]))
        draws = islice(chain,100)
        print([*draws][-1])
