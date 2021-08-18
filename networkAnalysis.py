import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('jira_sample.csv')
df1 = df[['Assignee', 'Reporter']]
G = nx.Graph()
G = nx.from_pandas_edgelist(df1, 'Assignee', 'Reporter')
figure(figsize=(10, 8))
nx.draw_shell(G, with_labels=True)
plt.show()

G['barbie.doll']
len(G['barbie.doll'])

leaderboard = {}
    for x in G.nodes:
leaderboard[x] = len(G[x])
s = pd.Series(leaderboard, name='connections')
df2 = s.to_frame().sort_values('connections', ascending=False)
df2.head()
