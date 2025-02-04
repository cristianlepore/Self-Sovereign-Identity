import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    "Existence and representation", "Consent", "Ownership and control", "Security and protection", "Persistence",
    "Privacy and minimal disclosure", "Access and availability", "Transparency", "Portability", "Interoperability",
    "Cost", "Standard", "Decentralization and Autonomy", "Verifiability and Authenticity", "Usability and consistency"
]

edges = [
    ("Existence and representation", "Consent", 6), ("Existence and representation", "Ownership and control", 7),
    ("Existence and representation", "Persistence", 3), ("Existence and representation", "Privacy and minimal disclosure", 4),
    ("Existence and representation", "Access and availability", 4),
    ("Existence and representation", "Decentralization and Autonomy", 2),
    ("Existence and representation", "Usability and consistency", 2),

    ("Consent", "Ownership and control", 6), ("Consent", "Persistence", 3),
    ("Consent", "Privacy and minimal disclosure", 4), ("Consent", "Access and availability", 4),
    ("Consent", "Portability", 2), ("Consent", "Decentralization and Autonomy", 3), ("Consent", "Usability and consistency", 2),

    ("Ownership and control", "Persistence", 2), ("Ownership and control", "Privacy and minimal disclosure", 4),
    ("Ownership and control", "Access and availability", 3),
    ("Ownership and control", "Decentralization and Autonomy", 2),

    ("Security and protection", "Persistence", 6), ("Security and protection", "Privacy and minimal disclosure", 5),
    ("Security and protection", "Access and availability", 2),
    ("Security and protection", "Verifiability and Authenticity", 2),

    ("Persistence", "Privacy and minimal disclosure", 7), ("Persistence", "Access and availability", 3),
    ("Persistence", "Transparency", 2), ("Persistence", "Portability", 2),
    ("Persistence", "Decentralization and Autonomy", 2),
    ("Persistence", "Verifiability and Authenticity", 2),

    ("Privacy and minimal disclosure", "Access and availability", 3), ("Privacy and minimal disclosure", "Portability", 2),
    ("Privacy and minimal disclosure", "Decentralization and Autonomy", 2),
    ("Privacy and minimal disclosure", "Verifiability and Authenticity", 2),

    ("Access and availability", "Transparency", 5), ("Access and availability", "Portability", 2),
    ("Access and availability", "Interoperability", 4),
    ("Access and availability", "Decentralization and Autonomy", 2),
    ("Access and availability", "Verifiability and Authenticity", 2),
    ("Access and availability", "Usability and consistency", 2),

    ("Transparency", "Portability", 4), ("Transparency", "Interoperability", 6),
    ("Persistence", "Cost", 4), ("Transparency", "Standard", 4),

    ("Portability", "Interoperability", 8), ("Portability", "Cost", 2), ("Portability", "Standard", 3),
    
    ("Interoperability", "Cost", 2), ("Interoperability", "Standard", 3),

    ("Cost", "Standard", 4),
]

G = nx.Graph()
G.add_nodes_from(nodes)

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42, k=0.2)
edges_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}

nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2500, edge_color="gray", font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edges_labels, font_size=9)

plt.title("Graph Representation of the Table")
plt.show()
