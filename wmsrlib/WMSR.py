import math
from scipy.linalg import circulant
import networkx as nx
import numpy as np

import matplotlib.pyplot as plt


# Plot range
def draw_range(tmax, x0):
    # x0g = [xi for i, xi in enumerate(x0) if i != id_malicious]
    x0g = x0
    plt.plot((0, tmax), (np.mean(x0g), np.mean(x0g)), 'g:')  # Mean value
    plt.plot((0, tmax), (np.max(x0g), np.max(x0g)), 'b:')  # Max value
    plt.plot((0, tmax), (np.min(x0g), np.min(x0g)), 'b:')  # Min value


def WMSR(A, x0, id_malicious=0, tmax=500, K=.02):
    X = np.copy(x0)  # Agents state.
    Xlog = [np.copy(x0)]  # Log.
    N = len(A)

    f = 1

    # Consensus
    for t in range(tmax):
        # for t in range(1):

        # Wrong information
        mal = lambda t: 45 + 55 * math.cos(.031 * t)
        # mal = lambda t: val_malicious
        X[id_malicious] = mal(t)
        # new WMSR Laplacian matrix
        wmsr_L = []

        # For each x value in X
        for i, x in enumerate(X):
            ## get all the neighbors from M along with their id
            # Get neighbors ids
            # nids = [(i+1+j) % N for j in range(neig)] + [(i-1-j) % N  for j in range(neig)]
            nids = np.where(A[i] == 1)[0]
            # print i, nids

            ## Sort the neighbors
            # columns are (ids, values)
            sorted_neighs = np.array(sorted(enumerate(X[nids]), key=lambda x: x[1]))
            sorted_neighs[:, 0] = np.array(nids)[sorted_neighs[:, 0].astype(int)]

            # print 'x', x, i
            # print 'a', sorted_neighs
            # Separate the neighbors by smallers and largers
            sorted_vals = sorted_neighs[:, 1]
            n_smallers = len(sorted_vals[sorted_vals < x])
            n_largers = len(sorted_vals[sorted_vals > x])

            ### remove f values
            # Remove f values from smallers
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

            # Create a laplacian line
            # print 'b',sorted_neighs
            l = np.zeros(N)  # Init with zeros
            l[sorted_neighs[:, 0].astype(int)] = -1  # not removed neighbors
            l[i] = len(sorted_neighs)  # Degree of node i
            wmsr_L.append(l)
            # print 'l',l

            # print np.array(wmsr_L)
        # Apply the consensus algorithm with the new Laplacian matrix
        U = np.dot(wmsr_L, X)  # Sharing bad information
        # U[m_id] = np.dot(L[m_id], X)  # Malicious agent behaves properly (its own information is right)

        # Control action
        X += -K * U

        X[id_malicious] = mal(t)
        Xlog.append(np.copy(X))

    Xlog = np.array(Xlog)

    return Xlog.T


def WMSRv2(A, x0, id_malicious=[0], f=None, tmax=500):
    if f is None:
        f = len(id_malicious)  # Number of malicious agents
    X = np.copy(x0)  # Agents state.
    Xlog = []  # Log.
    N = len(A)

    # Consensus
    for t in range(tmax):

        # Wrong information
        #mal = lambda t: [m * 20 + (-1) ** m * 20 * math.sin(.21 * t) + 20 + 20 * np.random.rand() for m, id in
        #                 enumerate(id_malicious)]
        #mal = lambda t: [120 + 20 * np.random.rand() for m, id in enumerate(id_malicious)]
        mal = lambda t: [90 + 20 * np.random.rand() for m, id in enumerate(id_malicious)]
        # mal = lambda t: [50+(-1)**m*50 + 20 * np.random.rand() for m, id in enumerate(id_malicious)]

        X[id_malicious] = mal(t)
        Xlog.append(np.copy(X))

        # New X
        X_tmp = np.copy(X)

        # For each x value in X
        for i, x in enumerate(X):
            ## get all the neighbors from M along with their id
            # Get neighbors ids
            # nids = [(i+1+j) % N for j in range(neig)] + [(i-1-j) % N  for j in range(neig)]
            nids = np.where(A[i] == 1)[0]
            # print i, nids

            ## Sort the neighbors
            # columns are (ids, values)
            sorted_neighs = np.array(sorted(enumerate(X[nids]), key=lambda x: x[1]))
            sorted_neighs[:, 0] = np.array(nids)[sorted_neighs[:, 0].astype(int)]

            # print 'x', x, i
            # print 'a', sorted_neighs
            # Separate the neighbors by smallers and largers
            sorted_vals = sorted_neighs[:, 1]
            n_smallers = len(sorted_vals[sorted_vals < x])  # Number of smaller neighbours
            n_largers = len(sorted_vals[sorted_vals > x])  # Number of larger neighbours

            ### remove f values
            # Remove f values from smallers
            
            if n_smallers >= f:                
                sorted_neighs = sorted_neighs[f:]
            else:                
                # Revmove all
                sorted_neighs = sorted_neighs[n_smallers:]
                        
            # Remove f values from largers
            if n_largers >= f:
                if  f > 0:
                    sorted_neighs = sorted_neighs[: -f]
                
            else:
                # Remove all largers
                if n_largers > 0:
                    sorted_neighs = sorted_neighs[: -n_largers]

            # Create a laplacian line
            # l = np.zeros(N)  # Init with zeros
            # l[sorted_neighs[:, 0].astype(int)] = -1  # not removed neighbors
            # l[i] = len(sorted_neighs)  # Degree of node i
            # wmsr_L.append(l)            
            if not i in id_malicious:
                X_tmp[i] = (sum(sorted_neighs[:, 1]) + X[i]) / (len(sorted_neighs[:, 1]) + 1)
                
                # print (i, X_tmp[i])
                # print (sorted_neighs)

                # print np.array(wmsr_L)
        # Apply the consensus algorithm with the new Laplacian matrix
        # U = np.dot(wmsr_L, X)  # Sharing bad information


        # Control action
        # X += -K * U

        # X[id_malicious] = mal(t)
        X = np.copy(X_tmp)
        # Xlog.append(np.copy(X))

    Xlog = np.array(Xlog)

    return Xlog.T


def plot_log(Xlog, id_mal=None, colors=None, thikness=2):
    # Plot
    if colors is None:
        for i, x in enumerate(Xlog):
            plt.plot(x, label=str(i), linewidth=thikness)
    else:
        for i, (x, color) in enumerate(zip(Xlog, colors)):
            plt.plot(x, color, label=str(i), linewidth=thikness)

    if id_mal is not None:
        plt.plot(Xlog[id_mal], 'r--', label=str(i), linewidth=thikness)
    draw_range(len(Xlog.T), Xlog.T[0])


def plot_log_v2(Xlog, set_mal=None, colors=None, thikness=2):
    # Plot
    if colors is None:
        for i, x in enumerate(Xlog):
            plt.plot(x, label=str(i), linewidth=thikness)
    else:
        for i, (x, color) in enumerate(zip(Xlog, colors)):
            if i not in set_mal:
                plt.plot(x, color, label=str(i), linewidth=thikness)
            else:
                print ('mal')
                plt.plot(x, 'r..', label=str(i), linewidth=thikness)


            # plt.plot(Xlog[id_mal], 'r--', label=str(i), linewidth=thikness)
    # draw_range(len(Xlog.T), Xlog.T[0])


############### GRAPH
#
A = [[0, 1, 1, 0, 0, 0, 1],
     [1, 0, 1, 1, 0, 0, 0],
     [1, 1, 0, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 1, 0],
     [0, 0, 0, 1, 0, 1, 1],
     [0, 0, 0, 1, 1, 0, 1],
     [1, 0, 0, 0, 1, 1, 0]
     ]
# Triangular
A = [[0, 1, 1, 0, 0, 0, 0],
     [1, 0, 1, 1, 0, 0, 0],
     [1, 1, 0, 1, 1, 0, 0],
     [0, 1, 1, 0, 1, 1, 0],
     [0, 0, 0, 1, 0, 1, 1],
     [0, 0, 0, 1, 1, 0, 1],
     [0, 0, 0, 0, 1, 1, 0]
     ]

A = np.array([[0, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 0, 0, 1, 1],
              [1, 1, 1, 1, 1, 0, 1],
              [1, 1, 1, 1, 1, 1, 0]])


# A = np.array(A)
# G = nx.from_numpy_matrix(A)
# pos = {0: (0, 0), 1: (.4, 1.3), 2: (1.3, .7), 3: (2, 2), 4: (2.7, .7), 5: (3.6, 1.3), 6: (4, 0)}
#
# draw_graph = False
# if draw_graph:
#     nx.draw(G, pos=pos, with_labels=True, bbox_inches="0", font_color='w')
#     plt.show()
#
# ############# Plot
# N = len(A)
# x0 = 100 * np.random.rand(N)
# # x0 = np.array([60.44893393, 74.98778144, 2.58844596, 85.26558854, 66.82731276,
# #                83.67424014, 79.78491275])
# id_malicious = 6
# Xlog = WMSR(A, x0, id_malicious=id_malicious)
# plot_log(Xlog)
# plt.legend()
# plt.show()
