
# Markov Matrix

[](images/example.gif)

This package provides a simple, extensible interface for simulating series of
matrices, where the value of each cell is the result of a, potentially
interdependent, markov process.

## Installation

```
pip install markov-matrix
```

## Usage

```
from markov_matrix import matrix_chain
import itertools

p_matrix = np.array([
   [ .1 , .1 , .8 ],
   [ .0 , .0 ,1.0 ],
   [ .9 , .1 , .0 ],
   [],
])

chain = matrix_chain(p_matrix)
cube = np.stack(itertools.islice(chain, 100), axis=2)
```
