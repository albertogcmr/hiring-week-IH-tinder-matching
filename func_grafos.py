import networkx as nx
import matplotlib
from random import choice


# https://networkx.github.io/documentation/networkx-1.10/reference/introduction.html

def create_graph(df): 
    G_res=nx.Graph()
    for a in df.index: 
        for c in df.columns: 
            
            G_res.add_edge(a ,c, weight=df.loc[a][c])
            # print(a ,c, df.loc[a][c])
    return G_res

def plot_bipartite_graph(G, set_X, set_Y): 
    X, Y = set_X, set_Y # df1.index, df1.columns
    pos = dict()
    pos.update( (n, (1, i)) for i, n in enumerate(X) ) # put nodes from X at x=1
    pos.update( (n, (2, i)) for i, n in enumerate(Y) ) # put nodes from Y at x=2
    nx.draw(G, pos=pos)

# sort por peso DESCENCENTE
def get_best_match(G, node, used): 
    # print(node)
    
    for edge in sorted(G.edges(data=True), key=lambda x: - x[2]['weight']): # sort por weight DESCENCENTE
        if node in edge and all(u not in edge for u in used): 
            res = edge
            break
    else: # si no existe una arista para el nodo que queremos elegimos una random
        options = [(node1, node2, w) for node1, node2, w in list(G.edges(data=True)) if (node1 not in used and node2 not in used)]
        if len(options) == 0: # si no hay opciones devuelve nada
            print("No hay emparejamiento posible")
            return None
        res = choice(options) 
    
    node1, node2, w = res
    return node1, node2, w['weight']