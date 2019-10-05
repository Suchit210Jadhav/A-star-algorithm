import math
import matplotlib.pyplot as plt
points = []
path_points = []
def print_path(node):
    if parent[node] == -1:
        return
    else:
        print_path(parent[node])
        path_points.append(node)
        print("->", node, end="")

def heuristic(node):
    x1 = vert[node][0]
    y1 = vert[node][1]
    x2 = vert[end][0]
    y2 = vert[end][1]
    return int(math.sqrt((x1-x2)**2 + (y1-y2)**2))

def fofnn(node):
    fofnt = gon[node] + heuristic(node)
    if node in closed:
        return
    elif node in fofn.keys():
        if fofn[node] > fofnt:
            fofn.update({node : fofnt})
    else:
        fofn[node] = fofnt
        
def min_fofn():
    minimum = min(fofn, key= fofn.get)
    return minimum

vert = {}
edge = {}
gon = {}
fofn = {}
closed = []
parent = {}
v = int(input("No. of nodes:"))
for o in range(v):
    name, xt, yt = input().split()
    points.append(name)
    vert[name] = (int(xt), int(yt))

e = int(input("No. of edges:"))
for o in range(e):
    v1, v2, cost = input().split()

    if v1 in edge.keys():
        edge[v1].append((v2, int(cost)))
    else:
        edge[v1] = [(v2, int(cost))]

start, end = input("Enter start and end node:").split()
stop = 0
gon[start] = 0
fofnn(start)
parent[start] = -1

while(len(fofn)>0) and stop ==0:
    current_node = min_fofn()
    del fofn[current_node]
    closed.append(current_node)

    if current_node in edge.keys():
        for i in range(len(edge[current_node])):
            next_node = edge[current_node][i][0]
            next_node_path_cost = edge[current_node][i][1]

            if next_node == end:
                stop = 1
                parent[next_node] = current_node
                final_cost = gon[current_node] + next_node_path_cost
                closed.append(next_node)
                break

            gon_next_node = gon[current_node] + next_node_path_cost

            if next_node in gon.keys():
                if gon[next_node] > gon_next_node:
                    parent.update({next_node : current_node})
                    gon.update({next_node : gon_next_node})
                    fofnn(next_node)
            else:
                parent[next_node] = current_node
                gon[next_node] = gon[current_node] + next_node_path_cost
                fofnn(next_node)

print("Verices: ", vert, "\nEdges: ", edge, "\ng(n): ", gon, "\nOpen w/ f(n): ", fofn, "\nClosed: ", closed)
print("Path: ", start, end="")
path_points.append(start)
print_path(end)
print("\nCost: ", final_cost)

for p in points:
    plt.plot(vert[p][0], vert[p][1], 'ro')
    plt.annotate(p, (vert[p][0], vert[p][1]))

for i in range(len(path_points)-1):
    x1 = vert[path_points[i]][0]
    y1 = vert[path_points[i]][1]
    x2 = vert[path_points[i+1]][0]
    y2 = vert[path_points[i+1]][1]
    plt.plot([x1, x2], [y1, y2], 'k-')
    
plt.show()