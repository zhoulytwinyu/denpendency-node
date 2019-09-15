#!/usr/bin/env python3
from collections import namedtuple

DependencyNode = namedtuple(
  "DependencyNode",
  ["payload","dependencies","outputs"]
)

def resolve_dependency_to_edges(nodes):
  upstream_map = {}
  edges = []
  for node in nodes:
    for output in node.outputs:
      if output in upstream_map:
        raise ValueError("Duplicated dependencies: {}".format(output))
      upstream_map[output] = node
  for node in nodes:
    for dependency in node.dependencies:
      if dependency not in upstream_map:
        raise ValueError("Missing dependencies: {}".format(dependency))
      edges.append( (upstream_map[dependency],node) )
  return edges
