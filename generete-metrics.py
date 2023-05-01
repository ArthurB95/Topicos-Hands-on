import networkx as nx
import os

G = nx.read_edgelist('bio-DM-LC.edges', nodetype=int, data=False)


if not os.path.exists('metrics/'):
    os.makedirs('metrics/')

with open('metrics/metrics.txt', 'w') as file:
    print(f'Nodes: {G.number_of_nodes()}', file=file)
    print(f'Edges: {G.number_of_edges()}', file=file)
    print(f'Density: {nx.density(G):.4f}', file=file)
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    degree_count = dict([(deg, degree_sequence.count(deg)) for deg in degree_sequence])
    print(f'Distribution of degrees: {degree_count}', file=file)
    maximo_grafico = max([d for n, d in G.degree()])
    print(f"Maximum degree: {maximo_grafico}", file=file)
    minumo_grafico = min([d for n, d in G.degree()])
    print(f"Minimum degree: {minumo_grafico}", file=file)
    avg_grafico = sum(dict(G.degree()).values()) / len(G)
    print(f"Average degree: {avg_grafico}", file=file)
    assortativity = nx.assortativity.degree_pearson_correlation_coefficient(G)
    print(f"Assortativity: {assortativity}", file=file)
    numero_triangulo = sum(nx.triangles(G).values())
    print(f"Number of triangles: {numero_triangulo}", file=file)
    maximo_numero_triangulo = max(nx.triangles(G).values())
    print(f"Maximum number of triangles: {maximo_numero_triangulo}", file=file)
    avg_clustering = nx.average_clustering(G)
    print(f"Average clustering coefficient: {avg_clustering}", file=file)
    clicks = list(nx.find_cliques(G))
    maximo_clique = max([len(click) for click in clicks])
    print(f"Lower bound of Maximum Click: {maximo_clique}", file=file)



