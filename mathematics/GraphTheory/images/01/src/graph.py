#!/usr/bin/env python
graph = { "a" : ["c"],
          "b" : ["c" "d"],
          "c" : ["a", "b", "d"],
          "d" : ["c"]
          }
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))

    return edges

print(generate_edges(graph))
