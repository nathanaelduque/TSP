import networkx as nx
import matplotlib.pyplot as plt

# Ler os dados da planilha
dados = [
    (0, 4),
    (4, 2),
    (2, 1),
    (1, 3),
    (3, 0)
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