# ================================================================
# NAMA : MUHAMMAD RAFLY
# NIM : J0403251002
# KELAS : A1
# PRAKTIKUM 2
# ================================================================

from collections import defaultdict 

graph = defaultdict(list) 

graph["A"].append("B") 
graph["A"].append("C")

graph["B"].append("A")
graph["B"].append("D")

graph["C"].append("A")
graph["C"].append("D") 

graph["D"].append("B")
graph["D"].append("C")   

print("HASIL ADJACENCY LIST")
for node in graph:
    print(node, ":", graph[node])

# PENJELASAN TIAP NODE
print("\nPENJELASAN TIAP NODE")
print("\nNode A ini terhubung ke node B dan node C")
print("\nNode B ini terhubung ke node A dan node D")
print("\nNode C ini terhubung ke node A dan node D")
print("\nNode D ini terhubung ke node B dan node C")