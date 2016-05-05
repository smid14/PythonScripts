'''
Simple Implementatio of the Preferend Attachement Model:
'''

import igraph as ig
import numpy as np

def pref_attach_graph(n, t, m):
    '''
    Construct a preferrend attachemend Graph
    :param n: int
    :param t: int
    :param m: int
    :return: igraph graph object
    '''
    G = ig.Graph.Full(n)
    G_update = G
    #Iterate through all time steps e.g vertics that should be added
    for n in range(1,t):
        G_update.add_vertex()
        #add to every new node m-1 edges
        while G_update.degree(G_update.vcount()-1) < m:
            #get degree of all nodes
            node_degrees = G_update.degree()
            #total degree of the graph
            sum_degree = sum(node_degrees)
            #degree of node j divide by total degree
            degree_dist = [x/float(sum_degree) for x in node_degrees]
            #choose random number with probability corresponding to node degree distribution
            rnd = np.random.choice(node_degrees, 1, p=degree_dist)
            #get index of the node list which correspond to node id in igraph
            node = node_degrees.index(rnd[0])
            #add edge to the node
            G_update.add_edge(G_update.vcount()-1, node)

    #Take some Graph Statistics:
    noVertics = G_update.vcount()
    noEdges = G_update.ecount()
    sumDegree = sum(G_update.degree())
    clusterCoef = G_update.transitivity_undirected()
    avgPath = G_update.average_path_length()

    #Print some statistics for the graph:
    print ('A Graph with n={} and t={} and m={} was constructed.'.format(n,t,m))
    print ('The Number of Vertics is: {}'.format(noVertics))
    print ('The Number of Edges is: {}'.format(noEdges))
    print ('The Sum of degress is: {}'.format(sumDegree))
    print ('The Clustering Coefficient is: {}'.format(clusterCoef))
    print ('The Average Path Length is: {}'.format(avgPath))

    return G_update




if __name__ == "__main__":
    graph_1= pref_attach_graph(3,1000, 3)
    graph_2= pref_attach_graph(4,1000, 3)
    graph_3= pref_attach_graph(5,1000, 3)
    graph_4= pref_attach_graph(10,1000, 3)

