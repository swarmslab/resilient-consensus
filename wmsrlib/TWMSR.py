from scipy.linalg import circulant
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)

# Initial values
N = 10  # Number of robots
np.random.seed(0)
x0 = 100 * np.random.rand(N)
tmax = 150  # Time steps
f = 1  # Malicious agents

# Zeros matrix
Z = np.zeros((N, N))
I = np.identity(N)

As = []

# Adjacency Matrix 1
a = np.zeros(N)
a[-1] = 1
# a[-2] = 1
As.append(circulant(a))

a = np.zeros(N)
# a[-1] = 1
a[-2] = 1
As.append(circulant(a))

a = np.zeros(N)
a[1] = 1
# a[2] = 1
As.append(circulant(a))

a = np.zeros(N)
# a[1] = 1
a[2] = 1
As.append(circulant(a))

nA = len(As)

XT = np.hstack((np.copy(x0), np.copy(x0), np.copy(x0), np.copy(x0)))
# XT = np.copy(x0)

Xlog = [np.copy(XT)]

# Consensus
for t in range(tmax):

    # Adjacency matrix (A2 for even t and A1 for odd.)
    # Main matrix
    A = np.copy(np.hstack(np.roll(As, t % N, axis=0)))  # [:,:N]

    # Wrong information
    M = np.copy(XT)
    M[0] = 200  # Bad value is shared

    # For each x value in X
    for i, x in enumerate(XT[:N]):

        ## get all the neighbors from M along with their id
        # Get neighbors ids
        nids = np.where(A[i] == 1)[0]

        ## Sort the neighbors
        # columns are (ids, values)
        sorted_neighs = np.array(sorted(enumerate(M[nids]), key=lambda x: x[1]))
        sorted_neighs[:, 0] = np.array(nids)[sorted_neighs[:, 0].astype(int)]

        # Split the neighbors by smallers and largers
        sorted_vals = sorted_neighs[:, 1]
        n_smallers = len(sorted_vals[sorted_vals < x])
        n_largers = len(sorted_vals[sorted_vals > x])

        ### remove f values
        # Remove f values from smallers
        if True:
            # print n_smallers
            if n_smallers >= f:
                sorted_neighs = sorted_neighs[f:]
            else:
                # Revmove all
                sorted_neighs = sorted_neighs[n_smallers:]

            # Remove f values from largers
            if n_largers >= f:
                sorted_neighs = sorted_neighs[: -f]
            else:
                # Remove all largers
                if n_largers > 0:
                    sorted_neighs = sorted_neighs[: -n_largers]

        A[i] = 0
        A[i][sorted_neighs[:, 0].astype(int)] = 1

    #A[:, N:] = 0
    print np.sum(A,axis=1)
    # extended identity
    ia = np.hstack((I, Z, Z, Z))

    # sumM = I + A  #matrix to sum
    sumM = ia + A  # matrix to sum
    # Weight = 1/(degree + currentValue)
    w = 1. / np.sum(sumM, axis=1)
    sumM = [wi * sumi for wi, sumi in zip(w, sumM)]

    # Update old values for X+1
    # Xp1 =  np.dot(sumM, M)
    Xp1 = np.dot(sumM, XT)
    XT = np.roll(XT, N)
    XT[:N] = Xp1

    Xlog.append(np.copy(XT))

Xlog = np.array(Xlog)
series = Xlog.T[:N]
# Plot
for x in series[:]:
    plt.plot(x[:], '.-')

plt.show()
# print x[:]
# draw_range()
