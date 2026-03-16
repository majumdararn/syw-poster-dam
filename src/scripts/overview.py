from graphviz import Digraph
import paths

g = Digraph(format="pdf")

# Nodes
g.node("data", "Data")
g.node("scripts", "Scripts")
g.node("figures", "Figures")
g.node("tex", "LaTeX manuscript")
g.node("pdf", "Article PDF")

# Workflow
g.edge("data", "scripts")
g.edge("scripts", "figures")
g.edge("figures", "tex")
g.edge("tex", "pdf")

# g.render("overview", view=True)

g.render(paths.figures / 'overview', format='pdf', cleanup=True)