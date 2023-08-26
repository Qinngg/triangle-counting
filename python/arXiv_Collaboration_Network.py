import networkx as nx
import pandas as pd
import gzip

def decompress_file(file_path):
    """解压 .txt.gz 文件并返回解压后的文件名"""
    output_path = file_path.replace(".gz", "")
    with gzip.open(file_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            f_out.write(f_in.read())
    return output_path

# 解压文件
decompressed_file = decompress_file("/Users/qingf/Desktop/LDPGraphStatistics-master/python/ca-AstroPh.txt.gz")  # 替换为你的 .txt.gz 文件路径

# 使用networkx加载数据集
G = nx.read_edgelist(decompressed_file)

# 重新标记节点为从1到n的数字
node_mapping = {node: i for i, node in enumerate(G.nodes(), start=1)}
G = nx.relabel_nodes(G, node_mapping)

# 生成 edges.csv
edges_df = pd.DataFrame(list(G.edges()), columns=['NodeA', 'NodeB'])
edges_df.to_csv("arxiv_edges.csv", index=False)

# 计算度数并生成 degree.csv
degree_data = dict(G.degree())
degree_df = pd.DataFrame(list(degree_data.items()), columns=['Node', 'Degree'])
degree_df.to_csv("arxiv_degree.csv", index=False)

print("Files generated successfully!")
