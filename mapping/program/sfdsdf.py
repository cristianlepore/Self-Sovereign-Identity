from graphviz import Digraph

dot = Digraph()

dot.node("Identity", shape="oval", style="filled", fillcolor="gold")

principles = ["Existence", "Control", "Access", "Transparency", "Persistence",
              "Portability", "Interoperability", "Consent", "MinimalDisclosure", "RightsProtection"]

for p in principles:
    dot.node(p, shape="circle", style="filled", fillcolor="lightblue")
    dot.edge("Identity", p, label="follows")

dot.edge("Control", "Consent", label="hasSubPrinciple")
dot.edge("Control", "MinimalDisclosure", label="hasSubPrinciple")

influences = ["Security", "Privacy", "Usability"]
for i in influences:
    dot.node(i, shape="box", style="filled", fillcolor="gray")
    dot.edge("Principle", i, label="influences")

dot.render("ssi_knowledge_graph", format="png", cleanup=False)  # Genera il file PNG
