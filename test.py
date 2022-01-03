import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz2.38\\bin'
dot = graphviz.Digraph(comment='The Round Table')
dot.node('A', 'King Arthur')
dot.node('B', 'Erfan')
dot.node('C', 'XX')
dot.edge('A', 'B')
dot.edge('A', 'C')
# print(dot.source)
dot.render('doctest-output/round-table.gv', view=True) 