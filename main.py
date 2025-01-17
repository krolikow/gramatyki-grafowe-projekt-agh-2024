"""
Experimental file
Please DO NOT PUSH changes to this file 
"""
from fake_graphs import *
from plot_graph import plot_graph
from productions.p1.production1 import ProductionP1
from productions.p2.production2 import ProductionP2
from productions.p07.production7 import ProductionP7
from productions.p8.production8 import ProductionP8
from productions.utils import find_q_with_one_neighbor_xy

if __name__ == '__main__':

    G = start_graph()
    plot_graph(G)

    q_node = find_q_with_one_neighbor_xy(G, 16, 16)
    print(q_node)

    prod1 = ProductionP7(G)
    prod1.apply_2(q_node)
    plot_graph(G)

    prod2 = ProductionP1(G)
    prod2.apply()
    plot_graph(G)

    q_node = find_q_with_one_neighbor_xy(G, 16, 16)
    prod3 = ProductionP7(G)
    prod3.apply_2(q_node)
    plot_graph(G)

    prod4 = ProductionP8(G)
    prod4.apply()
    plot_graph(G)
   
    prod5 = ProductionP2(G)
    prod5.apply()
    plot_graph(G)
    
    prod6 = ProductionP1(G)
    prod6.apply()
    plot_graph(G)

    q_node = find_q_with_one_neighbor_xy(G, 16, 16)
    prod7 = ProductionP7(G)
    prod7.apply_2(q_node)
    plot_graph(G)

    prod8 = ProductionP8(G)
    prod8.apply()
    plot_graph(G)

    prod9 = ProductionP2(G)
    prod9.apply()
    plot_graph(G)
    
    prod10 = ProductionP1(G)
    prod10.apply()
    plot_graph(G)

    


    

    


    