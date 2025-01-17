# Gramatyki Grafowe AGH  - Projekt 1

## Podział na grupy

| Grupa | Produkcje | Osoby                                  |
| --- | --- |----------------------------------------|
| Grupa 1 | P1, P2 | Damian Tworek, Bartłomiej Wiśniewski   |
| Grupa 2 | P3, P4, P7 | Wojciech Przybytek, Dariusz Piwowarski |
| Grupa 3 | P5, P6, P8 |                                        |
| Grupa 4 | P9, P10, P21 | Maciej Nessel, Tomasz Ostafin         |
| Grupa 5 | P11, P12, P22 |                                        |

## Organizacja pracy

1. Każda grupa forkuje repo i pracuje na swoim.
2. Pracujemy tylko w swoich plikach w katalogu productions, możecie sobie testować w nieistniejącym z perspektywy gita pliku main.py.
3. Piszemy testy
4. Merge do `main` głównego repo robimy tylko przez Pull Requesta. Będą akceptowane najpóźniej na początku zajęć.


## Reprezentacja hipergrafu

Używamy biblioteki `networkx`, htóra służy do modelowania i wizualizacji grafów (nie hipergrafów).
Hipergraf można zasymulować przez dodanie sztucznego wierzchołka dla każdej hiperkrawędzi i połączenia go z wirzchołkami przynależącymi do hiperkrawędzi. To podejście stosujemy.  
Przykład:
```
# hypergraph
vertices = { 1, 2, 3, 4 }
hyperedges = { E: (1, 2, 3), A: (1, 2), B: (2, 4) }

# hypergraph as graph
vertices = { 1, 2, 3, 4, E }
edges = { E1: (1, E), E2: (2, E), E3: (3, E), A: (1, 2), B: (2, 4) }
```
