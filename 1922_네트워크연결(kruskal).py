import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = {}
graph['vertices'] = list(range(1,N+1))
graph['edges'] = list()
for i in range(M):
    graph['edges'].append(list(map(int,input().split())))


parent = {}
rank = {}


def make_set(v):
    parent[v] = v
    rank[v] = 0


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
        
    return parent[v]

def union(v, u):
    root1 = find(v)
    root2 = find(u)
    
    if root1 != root2:

        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(graph):    
    for v in graph['vertices']:
        make_set(v)
    
    mst = []
    mst_cost = 0
    edges = graph['edges']
    edges.sort(key = lambda a : a[2])
    
    for edge in edges:
        v, u,weight = edge
                
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
            mst_cost+= edge[2]
    
    return mst_cost

print(kruskal(graph))