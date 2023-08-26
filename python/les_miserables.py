import networkx as nx
import pandas as pd

# 从NetworkX加载数据集
G = nx.les_miserables_graph()

# 创建一个从人名到数字的映射
name_to_number = {name: number for number, name in enumerate(G.nodes(), start=1)}

# 使用映射更新图中的节点和边
G = nx.relabel_nodes(G, name_to_number)

# 生成 edges.csv
edges_df = pd.DataFrame(list(G.edges()), columns=['NodeA', 'NodeB'])
edges_df.to_csv("edges.csv", index=False)

# 计算度数并生成 degree.csv
degree_data = dict(G.degree())
degree_df = pd.DataFrame(list(degree_data.items()), columns=['Node', 'Degree'])
degree_df.to_csv("degree.csv", index=False)

print("Files generated successfully!")
