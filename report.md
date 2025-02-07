
**!** For both subtasks we analized the time complexity of each algorithm and comparing them to the library-ready algorithms which will show the performance of our team's realisations

The work was distrubuted in this way:
* **Kruskal's algorithm and Prim's algorithm optimisation** - Roman Prokhorov

* **Algorithm comparisment and visualisation** -  Roman Prokhorov

* **Decision tree classifier** - Roman Prokhorov

* **Dataset tunning and fitting it for the classifier** - Taras Kopach

* **Prim's algorithm and lab report** - Taras Kopach

* **Report and decision tree classifier analysis** - Taras Kopach



### Subtask 1.1

In Subtask 1.1 our team had realised Kruskal's and Prim's algorithms to iterate over NetowkX Graph in order to create a minimum spanning tree




#### Kruskal's algorithm


#### Prim's algorithm

The algorithm creates a minimal spanning tree 

**Time Complexity**	

$O((V + E) log V)$

**Space Complexity**	

$O(V + E)$

##### Algorithm work

    - Heappush every edge that goes from the starting node to the heapq 

    - We repeat this instruction until every node is visited:
        - Heappop the minimal weight edge 
        - **!** We check if the destination node in the edge is not visited, since it will create a cycle and we don't need that
        
        - If everything's ok we add the destination node to the visited set and the edge to the span_tree list

        - We run a cycle adding the edges adjacent to the newly visited node destination, checking the destination nodes of these nodes too.

        - Heappush the edges 

    - The visited set should contain all of the nodes of the graph at the moment of the loop breaking, which also signals the end of the algorithm

    + We return the edge data for a minimal spanning tree

#### Kruskal's algorithm

The algorithm also creates also a minimal spanning tree 

**Time Complexity**	

$O(E log E)$

**Space Complexity**	

$O(V + E)$

##### Algorithm work

    - Create a list of every node of the graph

    - Sort those edges by weight

    - Create an empty graph, it will be our future minimal spanning tree

    - Initialize a UnionFind class with the nodes of a graph

    - Iterating over every edge:

        - Perform a union (add edge to our union connectivity component) if both nodes don't have the same parent\representive node (basically if they're not in a union to avoid creating cycles)

        - Add this edge to the MST

    - Return the MST

Analysing the performance graph we found that our realisation of the Prim's algorithm works faster than Kruskal's in the 20-70 node region, but performs slower on higer node counts. 



### Subtask 1.2


#### Bellman-Ford algorithm

Finds the shorest simple path between any two nodes.

**Time Complexity**
$O(V * E)$

**Space Complexity**
$O(V)$

##### Algorithm work

    - Get the nodes and create distances and predecessors dict matricies

    - Iterating **n - 1** times we compare the distances from source to each node and comparing with the set values in the distances matrix

        - If we find a shorter distance between the nodes, we set this value to the dict and the predecessor node to the predecessors matrix

        - Check if there is no negative cycles within the graph, return -1, -1 if there are 

    - Return the predecessors sand distances matrices



#### Floyd-Warshall algorithm

Finds the shorest simple path between any two nodes.

**Time Complexity**
$O(V^3)$

**Space Complexity**
$O(V^2)$

##### Algorithm work

    - Create distances and predecessors matrices 

    - Set the distance for each node in the diagonal (n -> n) equal to 0

    - Fill the matrices with data from edges of the graph

    - Iterating through a possible intermediate node and through source\desination nodes we check the distance with through the intermediate node is shorter than the initial distance between two nodes. If there is this distance we change the distances and predecessors matrices

    - Return the predecessors sand distances matrices



While realising both algorithms we noticed that our floyd-warshall's algorithm realisation didn't have a proper negative cycle detection, making our bellman-ford's algorithm realisation work better with finding the shortest path and do it faster overall. Analysing the performance graph, we can tell the a huge time difference is present when there are 200+ nodes in a graph.


## Task 2

For this task we had to create a decision tree classifier based on some data

### Decision Tree Classifier

#### Dataset

The data set used for this classifier is about daily russian attacks on Ukraine. For classification and filtering we picked these criteria:
    + Model of weapon (Drone, Missile, Bomb, etc)

    + Amount of weapons launched

    + Amount of destroyed targets

    + Targets, that didn't reach their goal

The dataset was slightly tuned, filling null values with "*Unknown*" or dropping them, since some information could be classified or not accurate.


#### Development



##### Prediction

##### Visualisation

To make the visualisator work with our dataset, we had to use an open source debugger and visulisator

Credit: 
https://github.com/joachimvalente/decision-tree-cart.git

#### Gini

Our decision tree classifier successfuly managed to get pure nodes with gini = 0, getting the samples of the models with the decision data we would need.

#### Summary


