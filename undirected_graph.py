# undirected_graph.py
# An undirected graph G=(V,E) is a set V of vertices and a set E of undirected
# edges over V.  Loops are allowed.
# Here, we define functions to support a data structure for an undirected graph.
# V is an unnamed set of vertices.
# E is an unnamed set of undirected edges over V.
# G is a two-element list [V,E].
# Error checking assumes the user does not change the representation directly.

# Runs Dijkstras algorithm on the graph
def dijkstra(graph,vertex):
	numdict = dict()
	W = list()
	for vert in graph[0]:
		numdict[vert] = None
	numdict[vertex] = 0
	insert(vertex,0,W)
	while W != []:
		rogers = popmin(W)
		neighbors = neighbor_set(rogers[0],graph)
		for each in neighbors:
			wedge = (rogers[0],each)
			if (numdict[each] == None) or (numdict[each] > (numdict[rogers[0]] + weight(wedge,graph))):
				old = numdict[each]
				numdict[each] = numdict[rogers[0]] + weight(wedge,graph)
				if (each,old) in W:
					W.remove((each,old))
				insert(each,numdict[each],W)
	return numdict
	
# Distance function for undirected graph.
def distance(vert1,vert2,graph):
	dfunct = dijkstra(graph,vert1)
	return dfunct[vert2]

# Sorting function for ordered list
def insort(W):
	for index in range(1,len(W)):
		vert = W[index][0]
		value = W[index][1]
		i = index - 1
		while i>=0:
			if value < W[i][1]:
				W[i+1] = W[i]
				W[i] = (vert,value)
				i = i - 1
			else:
				break
	return
	
# Inserts an item into the list.	
def insert(vertex,weight,W):
	W.append((vertex,weight))
	insort(W)
	
# Returns and removes the first item in the list.
def popmin(W):
	return W.pop(0)
	
	
# Return an empty graph.
def empty_graph():
    return [set(),set(),dict()]

# Return weight function as a dictionary.	
def weights_dictionary(graph):
	return graph[2]

# Return the vertex set.
def vertex_set(graph):
    return graph[0]

# Return the edge set.
def edge_set(graph):
    return graph[1]

# Check whether a vertex is in a graph.
def vertex_in_graph(vertex,graph):
    return vertex in vertex_set(graph)

# Check whether an edge is in a graph.
def edge_in_graph(edge,graph):
    if len(edge) != 2:
        return False
    elif edge in edge_set(graph):
        return True
    else:
        return (edge[1],edge[0]) in edge_set(graph)

# Add a vertex to a graph.
def add_vertex(vertex,graph):
    if vertex_in_graph(vertex,graph):
        return False
    graph[0].add(vertex)
    return True

# Add an edge to a graph.
def add_edge(edge,graph,weight):
    if (len(edge) != 2):
        return False
    elif weight < 0:
	    raise ValueError
    elif not (vertex_in_graph(edge[0],graph) and vertex_in_graph(edge[1],graph)):
	    return False
    elif edge_in_graph(edge,graph):
        return False
    else:
        graph[1].add((edge[0],edge[1]))
        graph[2][(edge[0],edge[1])] = weight
        return True

# Return the neighbor set of a vertex.
def neighbor_set(vertex,graph):
    n = set()
    for edge in edge_set(graph):
        if edge[0] == vertex:
            n.add(edge[1])
        elif edge[1] == vertex:
            n.add(edge[0])
    return n

# Return the weight of an edge.
def weight(edge,graph):
	egde = (edge[1],edge[0])
	if edge_in_graph(edge,graph):
		try:
			weight = graph[2][(edge[0],edge[1])]
		except KeyError:
			weight = graph[2][(egde[0],egde[1])]
		return weight
	return None
	
# Returns a graph built from input text file.
def load_graph(file):
	graph = empty_graph()
	try: 
		fi = open(file)
	except:
		print("No file found, detonating...")
		exit()
	line = []
	line = fi.readline().strip(['\t'])
	while line:		
		try:
			floweight = float(line[2])
			add_vertex(line[0],graph)
			add_vertex(line[1],graph)			
		except:
			print("Incorrect string format for weight input")
			exit()
		try:
			add_edge([line[0],line[1]],graph,floweight)
		except:
			print("Weight must be greater than zero.")
			exit()
		line = fi.readline().strip(['    '])