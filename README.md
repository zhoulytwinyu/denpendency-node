# dependency_node
This is a python module that is useful in automticly resolving DAG network edges in `make` style.

You specify the dependencies and outputs for nodes. The resolver returns all edges for use in airflow or other libraries.

## Install
```
pip install git+https://github.com/zhoulytwinyu/dependency-node
```

## Import
```
from dependency_node import DependencyNode, resolve_dependency_to_edges
```

## Usage
```
nodes = [
  DependencyNode(
    payload= ...,
    dependencies=[...],
    outputs=[...]
  ),
  ...
]
edges = resolve_dependency_to_edges(nodes)
node_from,node_to = edges[0]
```
