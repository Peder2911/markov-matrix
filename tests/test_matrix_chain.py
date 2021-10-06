
from itertools import islice
import numpy as np
from unittest import TestCase
from markov_matrix import matrix_chain

np.random.seed(1337)

class TestMatrixChain(TestCase):
    def test_matrix_chain(self):
        chain = matrix_chain(np.array([
                [ .8 , .2 , .0 ,],
                [ .1 , .8 , .1 ,],
                [ .0 ,1.0 , .0 ,],
            ]), shape=(3,3))
        draws = islice(chain,25)
        for mat in draws:
            self.assertEqual(mat.shape, (3,3))
    def test_distrib(self):
        chain = matrix_chain(np.array([
                [ .5 , .5 ],
                [ .5 , .5 ],
            ]), shape=(3,3))
        draws = np.stack([*islice(chain,1000)],axis=2)
        means = draws.mean(axis=2)
        for number in means.ravel():
            diff = abs(.5 - number)
            self.assertLess(diff, .15)
