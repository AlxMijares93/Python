#implementacion de grafos en python
#utilizamos un diccionario para la implementacion del grafo
#las llaves son los nodos del grafo
#a cada nodo le corresponde una lista los cuales representa 
#todos los nodos con los cuales estan unidos

graph = {
	'A':['B','C'],
	'B':['C','D'],
	'C':['D'],
	'D':['C'],
	'E':['F'],
	'F':['C']
}

#realiza la busqueda de la ruta mas corta para el grafo dirijido

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

#print(find_shortest_path(graph, 'F', 'D'))


