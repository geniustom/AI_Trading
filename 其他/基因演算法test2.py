# genetic algorithm
from numpy import random
import matplotlib.pyplot as plt


# environment
err = 0.5  # error tolerance
ns = 5  # number of survivor
nc = 20  # number of child
gens = 100  # generation


def get_childs(parents):
    return [parent + random.randn()*err
            for _ in range(nc)
            for parent in parents]

def get_survivors(offsprings, f):
    return sorted(offsprings, key=f, reverse=True)[:ns]

def ga(f, guess=0, lb=0):
    parents = [guess]
    history = []
    for _ in range(gens):
        offsprings = [child for child in get_childs(parents)
                      if child > lb]
        survivors = get_survivors(offsprings, f)
        parents = survivors
        history.append(max(survivors))
    return history


if __name__ == '__main__':
    # problem
    f = lambda x: -x**2 + 100*x
    history = ga(f, guess=1)

    plt.plot(history)
    plt.show()