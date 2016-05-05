'''
Numpy Implementation of Eigenvector Centrality, PageRank, KatzCentrality
'''

import numpy as np
from numpy import linalg as LA
from numpy import matrix

from numpy.matrixlib.defmatrix import asmatrix


def eigenVectorCentrality(adjacency):
    '''
    :param adjacency: numpy matrix
    :return: (vector Eigenvalue, vector eigenVector, int maxiumEigenValue, int centralityScore, int centralNode)
    '''
    eigenValue, eigenVector = LA.eig(adjacency)
    maxEigenValue = eigenValue.argmax()
    centrality = np.absolute(eigenVector[:,maxEigenValue])
    max_node = centrality.argmax()+1
    return eigenValue,eigenVector,maxEigenValue, centrality, max_node


def pageRank(A, alpha, beta):
    '''
    :param A:
    :param D:
    :param alpha:
    :param beta:
    :return:
    '''
    D = np.transpose(A)*A
    diagD = np.diag(D)
    D = np.asmatrix(np.identity(A.shape[0])*diagD)
    print (D)
    Id = np.identity(A.shape[0])
    ADI = A*D.I
    print (ADI)
    one = np.linspace(1,1,A.shape[0]).reshape(A.shape[0],1)
    page_rank = beta*(Id-alpha*ADI).I*one
    return page_rank, page_rank.argmax()+1


def katzCentrality(A, beta, alpha):
    '''
    :param A:
    :param beta:
    :param alpha:
    :return:
    '''
    Id = np.identity(A.shape[0])
    one = np.linspace(1,1,A.shape[0]).reshape(A.shape[0],1)
    katz = beta*(Id-alpha*A).I*one
    return katz


if __name__ == '__main__':
    A = np.matrix([[0,1,1,1,0],
                   [1,0,1,1,1],
                   [1,1,0,1,1],
                   [1,1,1,0,0],
                   [0,1,1,0,0]])

    #Calculate the EigenVectorCentrality:
    eigenValue, eigenVector, maxEigenValue, centrality, node = eigenVectorCentrality(A)
    print ('EigenVector Centrality: ', centrality, 'Node', node)

    #Calculate PageRank
    vectorPageRank, nodePageRank = pageRank(A, 0.3, 0.3)
    print ('PageRank: ',vectorPageRank ,' Node: ', nodePageRank)

    #Calculate KatzCentrality:
    nodeKatz = katzCentrality(A, 0.2, 0.25)
    print ('Katz Centrality: ', nodeKatz)





