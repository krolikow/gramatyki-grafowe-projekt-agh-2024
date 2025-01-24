from fake_graphs import *
from plot_graph import plot_graph
from productions.p03.production3 import ProductionP3
from productions.p1.production1 import ProductionP1
from productions.p11.production11 import ProductionP11
from productions.p2.production2 import ProductionP2
from productions.p07.production7 import ProductionP7
from productions.p22.production22 import ProductionP22
from productions.p8.production8 import ProductionP8
from productions.utils import find_q_with_one_neighbor_xy

if __name__ == '__main__':

    G = start_graph()
    plot_graph(G)

    q_node = find_q_with_one_neighbor_xy(G, 16, 16)
    prod1 = ProductionP7(G)
    prod1.apply_2(q_node)
    plot_graph(G)

    prod2 = ProductionP1(G)
    prod2.apply()
    plot_graph(G)

    q_node = find_q_with_one_neighbor_xy(G, 11, 13)
    prod3 = ProductionP7(G)
    prod3.apply_2(q_node)
    plot_graph(G)

    prod4 = ProductionP8(G)
    prod4.apply()
    plot_graph(G)

    prod5 = ProductionP22(G)
    prod5.apply()
    plot_graph(G)

    prod6 = ProductionP2(G)
    prod6.apply()
    plot_graph(G)

    prod7 = ProductionP11(G)
    prod7.apply()
    plot_graph(G)

    prod8 = ProductionP1(G)
    prod8.apply()
    plot_graph(G)

    q_node = find_q_with_one_neighbor_xy(G, 12.25, 13.75)
    prod9 = ProductionP7(G)
    prod9.apply_2(q_node)
    plot_graph(G)

    prod10 = ProductionP8(G)
    prod10.apply()
    plot_graph(G)

    prod11 = ProductionP8(G)
    prod11.apply()
    plot_graph(G)

    prod12 = ProductionP2(G)
    prod12.apply()
    plot_graph(G)

    prod13 = ProductionP3(G)
    prod13.apply()
    plot_graph(G)

    prod14 = ProductionP1(G)
    prod14.apply()
    plot_graph(G)
