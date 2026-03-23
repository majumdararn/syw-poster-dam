"""
Plot script for creating flowchart
purposeÖ overview of syw framework
"""
from graphviz import Digraph
import paths

# initiation
g = Digraph(format="pdf")

#formatting
fs='40'
fs_big='40'
g.attr(size="2, 1")   # width=8 inches, height=6 inches
g.attr(ratio="fill")   # compresses to fit
g.attr('edge', arrowsize="2.0")

# CLuster and nodes definition
## overleaf cluster
with g.subgraph(name='cluster_group1') as c1:
    c1.attr(label="Overleaf", fontsize=fs_big, labelloc="t", labeljust="l")
    c1.node('A', 'manuscript', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
## github cluster
with g.subgraph(name='cluster_group2') as c2:
    c2.attr(label="GitHub", fontsize=fs_big, labelloc="t", labeljust="l")
    c2.node('B', 'analysis scripts', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c2.node('C', 'figure scripts', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c2.node('D', 'environment', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c2.node('E', 'rules', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c2.node('F', 'manuscript', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
## zenodo cluster
with g.subgraph(name='cluster_group3') as c3:
    c3.attr(label="Zenodo", fontsize=fs_big, labelloc="t", labeljust="l")
    c3.node('G', 'static dataset', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c3.node('H', 'dynamic dataset', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
## github ci/cd cluster
with g.subgraph(name='cluster_group4') as c4:
    c4.attr(label="GitHub action", fontsize=fs_big, labelloc="t", labeljust="l")
    c4.node('I', 'manuscript', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c4.node('J', 'figures', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
## final manuscript
with g.subgraph(name='cluster_group5') as c5:
    c5.attr(label="Final manuscript", fontsize=fs_big, labelloc="t", labeljust="l")
    c5.node('K', 'GitHub/ Arxiv', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")

# connections
## A - manuscript (overleaf)
## B - analysis scripts (github)
## C - figure scripts (github)
## D - environment (github)
## E - rules (github)
## F - manuscript (github)
## G - static dataset (zenodo)
## H - dynamic dataset (zenodo)
## I - manuscript (github action)
## J - figures (github action)
## K - github/arxiv (github action)

g.edge("A", "F", style='dotted')
g.edge("F", "I")
g.edge("C", "J")
g.edge("G", "J")
g.edge("H", "J")
g.edge("B", "H", style='dotted')
g.edge("H", "G", style='dotted')
g.edge("I", "K")

# # if you want to see the flowchart outside pdf
# # uncomment below
# g.render("overview", view=True)

# saving the figure
g.render(paths.figures / 'overview', format='pdf', cleanup=True)