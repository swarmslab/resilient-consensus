# Resilient consensus for time-varying networks of dynamic agents
## _American Control Conference (ACC), 2017_

### Abstract
We consider networks of dynamic agents that execute cooperative, distributed control algorithms in order to coordinate themselves and to collectively achieve goals. The agents rely on consensus algorithms that are based on local interactions with their nearest neighbors in the communication graph. However, such systems are not robust to one or more malicious agents and there are no performance guarantees when one or more agents do not cooperate. Recent results in network science deal with this problem by requiring specific graph topological properties. Nevertheless, the required network topologies imply high connectivity levels, which may be difficult to achieve in systems that exhibit time-varying communication graphs. In this paper, we propose an approach that provides resilience for networks of dynamic agents whose communication graphs are time-varying. We show that in the case where the required connectivity constraints cannot be satisfied at all times, we can resort to a consensus protocol that guarantees resilience when the union of communication graphs over a bounded period of time satisfies certain robustness properties. We propose a control policy to attain resilient behavior in the context of perimeter surveillance with a team of robots. We provide simulations that support our theoretical analyses.
### Paper
Saldana, D., Prorok, A., Sundaram, S., Campos, M. F., & Kumar, V. (2017, May). Resilient consensus for time-varying networks of dynamic agents. In 2017 American control conference (ACC) (pp. 252-258). IEEE.

* [Preprint](acc17-resilient-consensus-dynamic-agents.pdf)
* [Website](https://ieeexplore.ieee.org/abstract/document/7962962)

### Jupyter Notebooks

* [SW-MSR 1:](Circular%20consensus%20-%20Oscillatory%20beh%20-%20SW-MSR.ipynb) This notebook implements the algorithms in the paper and produce the presented results.

* [SW-MSR 2:](Clustering%20method%20-%20Submited.ipynb) This notebook implements the algorithms in the paper and produce the presented results.

