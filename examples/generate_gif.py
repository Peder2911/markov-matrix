
from matplotlib import pyplot as plt, animation
import numpy as np
from markov_matrix import matrix_chain

chain = matrix_chain(np.array([
        [ .90, .02, .08,],
        [ .0 ,1.0 , .0 ,],
        [ .1 , .0 , .9 ,],
    ]), shape = (25,25))

fig,ax = plt.subplots()
im = ax.imshow(next(chain))

def init():
    return (im,)

def frame(_: int):
    im.set_data(next(chain))
    return (im,)



ani = animation.FuncAnimation(fig, frame, frames = 100, init_func = init, blit = True, interval = 10)
ani.save("images/example.gif")
