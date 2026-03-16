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
    c1.attr(label="Overleaf", fontsize=fs_big, labelloc="t", labeljust="l")

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