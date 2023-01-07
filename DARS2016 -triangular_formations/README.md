# Triangular networks for resilient formations 
## _Distributed Autonomous Robotic Systems - DARS 2016_
![Triangular Network](http://swarmslab.com/wp-content/uploads/2022/01/triangular2.png)
### Abstract
Consensus algorithms allow multiple robots to achieve agreement on estimates of variables in a distributed manner, hereby coordinating the robots as a team, and enabling applications such as formation control and cooperative area coverage. These algorithms achieve agreement by relying only on local, nearest-neighbor communication. The problem with distributed consensus, however, is that a single malicious or faulty robot can control and manipulate the whole network. The objective of this paper is to propose a formation topology that is resilient to one malicious node, and that satisfies two important properties for distributed systems: (i) it can be constructed incrementally by adding one node at a time in such a way that the conditions for attachment can be computed locally, and (ii) its robustness can be verified through a distributed method by using only neighborhood-based information. Our topology is characterized by triangular robust graphs, consists of a modular structure, is fully scalable, and is well suited for applications of large-scale networks. We describe how our proposed topology can be used to deploy networks of robots. Results show how triangular robust networks guarantee asymptotic consensus in the face of a malicious agent.

### Paper
Saldana, D., Prorok, A., Campos, M. F., & Kumar, V. (2018). Triangular networks for resilient formations. In _Distributed Autonomous Robotic Systems_ (pp. 147-159). Springer, Cham.

* [Preprint](DARS2016-triangular_formations.pdf)
* [Website](https://link.springer.com/chapter/10.1007/978-3-319-73008-0_11)

### Jupyter Notebooks

* [Classical average consensus:](average_consensus.ipynb) This notebook exemplifies how a single malicious agent can influence cooperative agents to avoid reaching consensus.

    ![Fig:malicious](figs/malicious.png)
* [Forming triangular graphs:](forming_triangular_graphs.ipynb) Triangular graphs describe a simple topology to be resilient against a single malicious agent. This notebook shows a simple method to expand triangular graphs.

 ![Fig:malicious](figs/forming.png)
* [Resilient consensus](resilient_consensus.ipynb) This notebook shows that cooperative agents can reach consensus in the presence of a malicious agents if the communication network is a triangular graph.

![Fig:malicious](figs/triangular.png)
![Fig:malicious](figs/consensus.png)