import networkx as nx
import matplotlib.pyplot as plt

# Ler os dados da planilha
dados = [
    (0,39),
    (39,12),
    (12,29),
    (29,24),
    (24,31),
    (31,8),
    (8,40),
    (40,4),
    (4,57),
    (57,23),
    (23,21),
    (21,7),
    (7,10),
    (10,15),
    (15,51),
    (51,16),
    (16,45),
    (45,14),
    (14,50),
    (50,48),
    (48,2),
    (2,47),
    (47,34),
    (34,28),
    (28,46),
    (46,26),
    (26,17),
    (17,19),
    (19,49),
    (49,37),
    (37,6),
    (6,30),
    (30,41),
    (41,38),
    (38,18),
    (18,44),
    (44,20),
    (20,32),
    (32,13),
    (13,27),
    (27,35),
    (35,3),
    (3,52),
    (52,11),
    (11,5),
    (5,25),
    (25,53),
    (53,54),
    (54,36),
    (36,55),
    (55,33),
    (33,1),
    (1,9),
    (9,42),
    (42,56),
    (56,22),
    (22,43),
    (43,0)
]

# Criar um grafo direcionado
G = nx.DiGraph()

# Adicionar arestas ao grafo
for origem, destino in dados:
    G.add_edge(origem, destino)

# Desenhar o grafo
pos = nx.spring_layout(G)  # Layout para posicionar os nós
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, font_color='red', font_size=10, edge_labels={(origem, destino): f"{origem}-{destino}" for origem, destino in G.edges()})
plt.title("Grafo a partir dos dados da planilha")
plt.show()