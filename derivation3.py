
from fake_graphs import *
from plot_graph import plot_graph
from productions.p1.production1 import ProductionP1
from productions.p2.production2 import ProductionP2
from productions.p07.production7 import ProductionP7
from productions.p8.production8 import ProductionP8
from productions.utils import find_q_with_one_neighbor_xy

if __name__ == '__main__':
    G = start_graph()
    plot_graph(G, multiedge_node_size=3000, node_size=1500, font_size=12)

    q_node = find_q_with_one_neighbor_xy(G, 16, 16)

    prod1 = ProductionP7(G)
    prod1.apply_2(q_node)
    plot_graph(G, multiedge_node_size=3000, node_size=1500, font_size=12)

    prod2 = ProductionP1(G)
    prod2.apply()
    plot_graph(G, multiedge_node_size=1300, node_size=1000, font_size=7)

    q_node = find_q_with_one_neighbor_xy(G, 11, 13)
    prod3 = ProductionP7(G)
    prod3.apply_2(q_node)
    plot_graph(G, multiedge_node_size=1300, node_size=1000, font_size=7)

 

    


    

    


    