# ================================================================
# NAMA : MUHAMMAD RAFLY
# NIM : J0403251002
# KELAS : A1
# PRAKTIKUM 3
# ================================================================

print("Sebelum diubah")
matrix = [ 
[0,1,1,0], 
[1,0,1,0], 
[1,1,0,1], 
[0,0,1,0] 
] 
print(matrix)

print("=" * 60)

print("Sesudah Diubah")
def createGraph(V, edges):
    adj = [[] for _ in range(V)]

    # Add each edge to the adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)

        # since the graph is undirected
        adj[v].append(u)
    return adj

if __name__ == "__main__":
    V = 4

    # List of edges (u, v)
    edges = [[0, 1], [0, 2], [1, 2], [2,3] ]

    # Build the graph using edges
    adj = createGraph(V, edges)

    print("Adjacency List Representation:")
    for i in range(V):

        # Print the vertex
        print(f"{i}:", end=" ")
        for j in adj[i]:

            # Print its adjacent
            print(j, end=" ")
        print()