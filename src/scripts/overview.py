from graphviz import Digraph
import paths

g = Digraph(format="pdf")

#formatting
fs='40'
fs_big='55'
g.attr(size="15, 15")   # width=8 inches, height=6 inches
g.attr(ratio="fill")   # compresses to fit
g.attr('edge', arrowsize="4.0")

# Nodes
with g.subgraph(name='cluster_group1') as c1:
    c1.attr(label="Overleaf", fontsize=fs_big, labelloc="t", labeljust="l")
    c1.node('A', 'manuscript', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
with g.subgraph(name='cluster_group2') as c2:
    c2.attr(label="GitHub", fontsize=fs_big, labelloc="t", labeljust="l")
    c2.node('B', 'analysis scripts', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c2.node('C', 'figure scripts', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c2.node('D', 'environment', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c2.node('E', 'rules', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c2.node('F', 'manuscript', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
with g.subgraph(name='cluster_group3') as c3:
    c3.attr(label="Zenodo", fontsize=fs_big, labelloc="t", labeljust="l")
    c3.node('G', 'static dataset', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c3.node('H', 'dynamic dataset', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
with g.subgraph(name='cluster_group4') as c4:
    c4.attr(label="GitHub action", fontsize=fs_big, labelloc="t", labeljust="l")
    c4.node('I', 'manuscript', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c4.node('J', 'figures', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
with g.subgraph(name='cluster_group4') as c5:
    c4.attr(label="Final manuscript", fontsize=fs_big, labelloc="t", labeljust="l")
    c4.node('K', 'GitHub', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
    c4.node('J', 'Arxiv', shape='box', fontsize=fs, style="filled", fillcolor="lightblue")
# g.node("data", "Data")
# g.node("scripts", "Scripts")
# g.node("figures", "Figures")
# g.node("tex", "LaTeX manuscript")
# g.node("pdf", "Article PDF")

# # Workflow
# g.edge("data", "scripts")
# g.edge("scripts", "figures")
# g.edge("figures", "tex")
# g.edge("tex", "pdf")

g.render("overview", view=True)

g.render(paths.figures / 'overview', format='pdf', cleanup=True)