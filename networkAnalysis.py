import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df1 = df[['Assignee', 'Reporter']]
df1.dropna(inplace=True)
sn = nx.Graph()
sn = nx.from_pandas_edgelist(df1, 'Assignee', 'Reporter')
nx.draw_shell(sn, with_labels=True)
plt.show()

print("Number of Nodes : ", sn.number_of_nodes())
print("Number of Edges : ", sn.number_of_edges())
print("Diameter : ", nx.diameter(sn))
print("Radius : ", nx.radius(sn))
print("Center : ", nx.center(sn))
print("Clustering Coefficient : ", nx.average_clustering(sn))
print("Degree : ", sn.degree())
print("Efficiency : ", nx.global_efficiency(sn))

print(len(sn['susan.lee']))

leaderboard = {}
for x in sn.nodes:
    leaderboard[x] = len(sn[x])
s = pd.Series(leaderboard, name='connections')
df2 = s.to_frame().sort_values('connections', ascending=False)
print(df2.head())
