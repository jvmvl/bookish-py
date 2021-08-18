#-------------------------------------------------------------------------------
# Application permet de tracer un graphe pour simuler un réseau social
# On ajoute des sommets
# On dessine les arêtes entre les sommets voulus
#-------------------------------------------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt

social_network = nx.Graph()

social_network.add_node('Naruto')
social_network.add_node('Sasuke')
social_network.add_node('Itashi')
social_network.add_node('Jiraiya')
social_network.add_node('Kakashi')
social_network.add_node('Madara')
social_network.add_node('Obito')

social_network.add_edge('Naruto','Sasuke')
social_network.add_edge('Naruto','Jiraiya')
social_network.add_edge('Naruto','Kakashi')
social_network.add_edge('Sasuke','Itashi')
social_network.add_edge('Sasuke','Kakashi')
social_network.add_edge('Sasuke','Madara')
social_network.add_edge('Itashi','Kakashi')
social_network.add_edge('Kakashi','Obito')
social_network.add_edge('Madara','Obito')
social_network.add_edge('Obito','Naruto')


nx.draw(social_network, with_labels=True)
plt.draw()
plt.show()

print("Number of Nodes : ", social_network.number_of_nodes())
print("Number of Edges : ", social_network.number_of_edges())
print("Diameter : ", nx.diameter(social_network))
print("Radius : ", nx.radius(social_network))
print("Center : ", nx.center(social_network))
