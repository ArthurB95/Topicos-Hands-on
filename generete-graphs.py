import os
import networkx as nx
import matplotlib.pyplot as plt

if not os.path.exists('graphs/'):
    os.makedirs('graphs/')

G = nx.read_edgelist('bio-DM-LC.edges', nodetype=int, data=False)

# Layout: circular
pos = nx.circular_layout(G)
fig, ax = plt.subplots(figsize=(10, 8))
nx.draw(G, pos=pos, node_size=50, with_labels=True)
plt.titulo('Layout Circular')
plt.salvarFigura(f'graphs/graph-layout-circular.png', dpi=600)
plt.close()
# Layout: kamada-kawai
pos = nx.kamada_kawai_layout(G)
fig, ax = plt.subplots(figsize=(10, 8))
nx.draw_networkx(G, pos=pos, node_size=100, with_labels=False)
plt.titulo('Layout Kamada-Kawai')
plt.salvarFigura(f'graphs/graph-layout-kamada-kawai.png', dpi=600, bbox_inches='tight')
plt.close()
# Layout: spring
fig, ax = plt.subplots(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, node_size=100, with_labels=False)
plt.titulo('Spring Layout')
plt.salvarFigura(f'graphs/graph-layout-spring.png', dpi=600, bbox_inches='tight')
plt.close()
# Layout: spectral
fig, ax = plt.subplots(figsize=(10, 8))
pos = nx.spectral_layout(G)
nx.draw_networkx(G, pos=pos, node_size=100, with_labels=False)
plt.titulo('Spectral Layout')
plt.salvarFigura(f'graphs/graph-layout-spectral.png', dpi=600, bbox_inches='tight')
plt.close()
# Layout: random
fig, ax = plt.subplots(figsize=(10, 8))
pos = nx.random_layout(G)
nx.draw_networkx(G, pos=pos, node_size=100, with_labels=False)
plt.titulo('Random Layout')
plt.salvarFigura(f'graphs/graph-layout-random.png', dpi=600, bbox_inches='tight')
plt.close()
