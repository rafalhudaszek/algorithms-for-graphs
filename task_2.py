
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import itertools
import random
import generators as gen
import sys

#prints the consecutive vertices of the Hamilton cycle
def hamilton(neighMatrix):

    #initialization
    graph = neighMatrix
    stack = []
    used = dict((node, False) for node in range(len(graph)))
    nodes = [i for i in range(len(graph))]

    #recursive search
    hamilton_dfs(0, graph, stack, used)

    print("Koniec przeszukiwania")


#recursive depth first search
def hamilton_dfs(node, graph, stack, used):
    stack.append(node)
    if len(stack) == len(graph):
        isCycle = False
        if  graph[stack[-1]][stack[0]] == 1:
            isCycle = True
        if isCycle:
            stack.append(stack[0])
            print("Jest to cykl Hamiltona: ", stack)
            return True
        else:
            print("Jest to scieżka Hamiltona", stack)
            print("Następuje dalsze szukanie cyklu")
    else:
        used[node] = True
        row = list(graph[node])
        iterator = 0
        for edge in row:
            if edge == 1 and not used[iterator]:
                if hamilton_dfs( iterator, graph, stack, used) == True:
                    return True
            iterator = iterator + 1
        used[node] = False
    stack.pop()
