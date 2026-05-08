# ================================================================
# NAMA : MUHAMMAD RAFLY
# NIM : J0403251002
# KELAS : A1
# PRAKTIKUM 1
# ================================================================

def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Add each edge to the adjacency matrix
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1

        # since the graph is undirected
        mat[v][u] = 1
    return mat

if __name__ == "__main__":
    V = 4

    # List of edges (u, v)
    edges = [[0, 1], [0, 2], [1, 2], [2,3]]

    # Build the graph using edges
    mat = createGraph(V, edges)

    print("Adjacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()

# PENJELASAN TIAP BARIS
print("\nPENJELASAN TIAP BARIS")
print("\nBaris 0: Node 0 ini terhubung ke node 1 dan node 2")
print("\nBaris 1: Node 1 ini terhubung ke node 0 dan node 2")
print("\nBaris 2: Node 2 ini terhubung ke node 0, node 1 dan node 3")
print("\nBaris 3: Node 3 ini terhubung ke node 2")