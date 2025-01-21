import pandas as pd
import networkx as nx
df = pd.read_csv("data.csv")


G = nx.erdos_renyi_graph(n=20, p=0.15)  # Generates a random graph


def compute_degree_centrality(graph):
    return nx.degree_centrality(graph)


def compute_shortest_path(graph, source, target):
    return nx.shortest_path(graph, source=source, target=target)

import plotly.graph_objects as go
def draw_graph(graph):
    pos = nx.spring_layout(graph)
    edge_x, edge_y = [], []
    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=0.5, color='#888'), hoverinfo='none', mode='lines')

    node_x, node_y, node_text = [], [], []
    for node in graph.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(str(node))

    node_trace = go.Scatter(
        x=node_x, y=node_y, mode='markers+text', text=node_text,
        marker=dict(color='skyblue', size=10, line=dict(width=2))
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(showlegend=False, hovermode='closest'))
    return fig



import streamlit as st

st.title("Network Visualization Tool")
#This line sets the title for the Streamlit web app.

# Network selection options
nodes = list(G.nodes)
source = st.selectbox("Select source node:", nodes)
target = st.selectbox("Select target node:", nodes)

# Display computed metrics
if st.button("Compute Degree Centrality"):
    st.write(compute_degree_centrality(G))

if st.button("Find Shortest Path"):
    path = compute_shortest_path(G, source, target)
    st.write(f"Shortest path from {source} to {target}: {path}")

# Display network visualization
st.plotly_chart(draw_graph(G))