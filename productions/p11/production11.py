from itertools import combinations
from networkx.classes import neighbors
from productions.production import Production

class ProductionP11(Production):
    """
    Production P11:
    Divides a hexagon (with R=1) into 6 smaller quadrilaterals 
    when two adjacent edges have hanging nodes.
    Predicate: 
    - Selected node with label "S" and R=1
    - All its immediate neighbors have h=0
    - Exactly two adjacent edges have a hanging node (h=1)
    """

    @property
    def check(self):
        """Check if the production can be applied to the selected hexagon with two adjacent hanging nodes."""
        for node, data in self.graph.nodes(data=True):
            # Sprawdzamy czy węzeł to "S" i R=1
            if data.get("label") == "S" and data.get("R") == 1:
                neighbors_list = list(self.graph.neighbors(node))
                
                # Wszyscy sąsiedzi muszą mieć h=0
                if not all(self.graph.nodes[n].get("h") == 0 for n in neighbors_list):
                    continue

                # Zlicz krawędzie pomiędzy sąsiadami
                neighbors_edges_cnt = 0
                for n1, n2 in combinations(neighbors_list, 2):
                    if self.graph.has_edge(n1, n2):
                        neighbors_edges_cnt += 1

                # Dla sześciokąta powinniśmy mieć 6 węzłów sąsiednich.
                # Normalny sześciokąt połączony ma zwykle 6 krawędzi między tymi sąsiadami.
                # Jeśli to warunek podobny do P10, to zakładamy, że warunek 
                # topologiczny jest taki, że neighbors_edges_cnt == 5 lub 6.
                # W P10 sprawdzaliśmy ==5. Tutaj analogicznie możemy sprawdzić,
                # czy liczba krawędzi jest oczekiwana (np. ==5), zależy od specyfiki siatki.
                # Załóżmy, że również == 5 jest warunkiem poprawnym.
                if neighbors_edges_cnt != 5:
                    continue

                # Sprawdźmy teraz sąsiadów tych sąsiadów, aby wykryć istnienie 
                # dokładnie dwóch sąsiednich krawędzi z węzłami wiszącymi
                # Logika: dla każdego sąsiada węzła centralnego sprawdzamy czy posiada sąsiada z h=1
                # Szukamy dokładnie dwóch takich sąsiadów, a węzły h=1 muszą być "sąsiednie" 
                # tzn. te wiszące węzły muszą występować na dwóch kolejnych krawędziach heksagonu.
                
                # Pierwszy krok: znajdź wszystkich "hanging neighbors" dla każdego sąsiada.
                neighbors_with_hanging = []
                for neighbor in neighbors_list:
                    hanging_neighbors = [n for n in self.graph.neighbors(neighbor) 
                                         if self.graph.nodes[n].get("h") == 1]
                    # Interesują nas tylko sąsiedzi z dokładnie jednym wiszącym węzłem
                    # (lub może więcej – zależnie od definicji. Przyjmujemy 1 jak w P10.)
                    if len(hanging_neighbors) == 1:
                        neighbors_with_hanging.append((neighbor, hanging_neighbors[0]))

                # Teraz sprawdzamy czy mamy dokładnie dwóch sąsiadów z wiszącymi węzłami
                # i czy te dwa wiszące węzły są na krawędziach sąsiadujących ze sobą.
                if len(neighbors_with_hanging) == 2:
                    # Sprawdźmy czy sąsiedzi heksagonu z wiszącymi node'ami są sąsiadami w porządku cyklicznym
                    # Zakładamy, że neighbors_list ułożone są w kolejności "dookoła" sześciokąta (jeśli tak nie jest,
                    # należałoby je posortować, ale to zależy od struktury danych).
                    # W prosty sposób: sprawdzimy indeksy w neighbors_list.
                    indices = [neighbors_list.index(pair[0]) for pair in neighbors_with_hanging]
                    indices.sort()
                    # Dwie krawędzie są sąsiednie, jeśli różnica indeksów to 1 lub (przy wrap-around) 5
                    if (indices[1] - indices[0] == 1) or (indices[0] == 0 and indices[1] == 5):
                        print("Production 11 can be applied.")
                        return self._extract_subgraph(node, neighbors_list)

        print("Production 11 can't be applied.")
        return None

    def apply(self):
        """Apply P11 to divide the hexagon into 6 smaller quadrilaterals."""
        result = self.check

        if not result:
            return
        
        q_node, nodes = result
        self.subgraph.remove_node(q_node)
        self.graph.remove_node(q_node)

        midpoints = {}
        for (n1, n2) in combinations(nodes, 2):
            # Sprawdź czy istnieje krawędź w subgrafie
            if self.subgraph.get_edge_data(n1, n2):
                self._create_midpoint(midpoints, n1, n2)
            # Jeśli nie istnieje, ale oba węzły mają stopień 1 (wskazuje to na krawędź z hanging node)
            # i musi zostać "uzupełniona"
            elif self.subgraph.degree(n1) == 1 and self.subgraph.degree(n2) == 1:
                self.subgraph.add_edge(n1, n2, label='E', B=1)
                self.graph.add_edge(n1, n2)
                self._create_midpoint(midpoints, n1, n2)

        # Wypełnij graf nowymi elementami (analogicznie do P10, lecz uwzględniając
        # różną geometrię z dwoma wiszącymi węzłami)
        self._fill_graph(nodes, midpoints)

        # Aktualizuj główny graf
        self.graph.update(self.subgraph)


