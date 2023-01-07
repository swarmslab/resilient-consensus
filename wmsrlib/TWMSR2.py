import numpy as np
from numpy import matrix

n=30

def SW_MSR(i, t, T, Alog, xlog, F=1, V=range(n)):
    """
    SWMSR for a time step, for a single agent.
    """
    # Neighbors in the time interval
    A = Alog[- T + t:]
    Tp = len(A)  # Time interval T when T<t
    own_x = xlog[-1][i]

    time_neighbor = {}  # Recent time
    # Recent values
    for tau in range(Tp):
        for j in V:
            if A[-Tp + tau][i, j]:
                time_neighbor[j] = tau

                if Tp - tau >= len(xlog):  # if T<t
                    time_neighbor[j] = Tp

    tuples = [xlog[-Tp + tau][j] for j, tau in time_neighbor.items()]
    sorted_tuples = sorted(tuples)
    # Larger values
    largers = [tup for tup in sorted_tuples if tup >= own_x]
    # Smaller values
    smallers = [tup for tup in sorted_tuples if tup <= own_x]

    # Remove F largers and F smallers, and the own value
    remaining = smallers[F:] + largers[:-F] + [own_x]

    # Return the mean of the remaining values and the own value
    return np.mean(remaining)



################### Simulation ######
T = 10
step_duration = 1
cycles = 5
total_time = cycles * step_duration * T

# log for A
Alog = [A for A in At for _ in range(step_duration)]


step_duration = 1
SW_MSR(0, 30, T * step_duration, Alog, xlog)
