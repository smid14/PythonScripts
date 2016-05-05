'''
Simple Implementation of the ICM Algorithm:
'''

import igraph as ig


def ICM_Algorithm(graph, activation_Node, prob):
    '''
    :param graph: igraph graph object
    :param activation_Node: igraph node
    :param prob: edge weight prob
    :return: list of nodes
    '''
    i = 0
    A_0 = []
    A_0.append(activation_Node)
    activated_Nodes = []
    activated_Nodes.append(A_0)
    while len(activated_Nodes[i]) > 0:
        i = i+1
        A_i = []
        for node in activated_Nodes[i-1]:
            neighbors = graph.neighbors(node,mode='OUT')
            for element in neighbors:
                #rnd = random.uniform(0,1)
                if graph.es[graph.get_eid(node, element, error=False)]['weight'] > prob:
                    A_i.append(element)
        activated_Nodes.append(A_i)
    return_Nodes = []

    #Find nodes that are activated twice and delete all up to one
    for e in activated_Nodes:
        s = set(e)
        res = list(s)
        return_Nodes.append(res)
    print (activated_Nodes, '----' ,return_Nodes)

    return return_Nodes



if __name__ == '__main__':
     # Just reads in the test graph as edgelist with weigths on the edges and plots
     test_file = 'test_data.txt'
     graph = ig.Graph.Read_Ncol(test_file, names=True, directed=True, weights=True)
     layout = graph.layout_kamada_kawai()
     #ig.plot(graph, layout=layout, vertex_label = graph.vs['name'], edge_label = graph.es['weight'])


     node = graph.vs.select(name='1')[0].index
     neigh =  graph.neighbors(node,mode='OUT')
     test = graph.vs[9]['name']
     print ('Neighbors: ',neigh, test)
     weight = graph.es[graph.get_eid(node, neigh[0], error=False)]['weight']
     print ('Weight: ',weight)
     print ('Test: ')
     print (ICM_Algorithm(graph, node, 0.3))
     #ig.plot(graph, layout=layout, vertex_label = graph.vs['name'], edge_label = graph.es['weight'])