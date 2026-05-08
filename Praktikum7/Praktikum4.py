# ================================================================
# NAMA : MUHAMMAD RAFLY
# NIM : J0403251002
# KELAS : A1
# PRAKTIKUM 4
# ================================================================

#Menampilkan Nama node
print('Node yang digunakan adalah “Rafly”, “Ihsan”, “Rangga”, “Diaz”, “Aris”')

print("=" * 60)

#Menampilkan hubungan antar node
print('Hubungan antar node yang dipakai')
print("1.Rafly follow Ihsan")
print("2.Rafly follow Rangga")
print("3.Rafly follow Diaz")
print("4.Ihsan follow Diaz")
print("5.Ihsan follow Aris")
print("6.Rangga follow Aris")
print("7.Rangga follow Ihsan")
print("8.Diaz follow Aris")
print("9.Diaz follow Rafly")
print("10.Aris follow Ihsan")
print("11.Aris follow Rangga")

print("=" * 60)

#Adjacency list
def createGraph_Matriks(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Add each edge to the adjacency matrix
    for it in edges:
        u = it[0]
        v = it[1]

        mat[u][v] = 1

    return mat


if __name__ == "__main__":

    nodes = ["Rafly", "Ihsan", "Rangga", "Diaz", "Aris"]

    V = len(nodes)

    # List of edges (u, v)
    edges = [
        [0,1],  # Rafly -> Ihsan
        [0,2],  # Rafly -> Rangga
        [0,3],  # Rafly -> Diaz
        [1,3],  # Ihsan -> Diaz
        [1,4],  # Ihsan -> Aris
        [2,4],  # Rangga -> Aris
        [2,1],  # Rangga -> Ihsan
        [3,4],  # Diaz -> Aris
        [3,0],  # Diaz -> Rafly
        [4,1],  # Aris -> Ihsan
        [4,2]   # Aris -> Rangga
    ]

    # Build the graph using edges
    mat = createGraph_Matriks(V, edges)

    print("Adjacency Matrix Representation:\n")

    print("       ", end="")
    for node in nodes:
        print(f"{node:8}", end="")
    print()

    for i in range(V):

        print(f"{nodes[i]:7}", end=" ")

        for j in range(V):
            print(mat[i][j], end="       ")

        print()



print("=" * 60)

# Adjacency List

def createGraph_List(V, edges):
    adj = [[] for _ in range(V)]

    # Add each edge to the adjacency list
    for it in edges:
        u = it[0]
        v = it[1]

        adj[u].append(v)

    return adj


if __name__ == "__main__":

    nodes = ["Rafly", "Ihsan", "Rangga", "Diaz", "Aris"]

    V = len(nodes)

    # List of edges (u, v)
    edges = [
        [0,1],  # Rafly -> Ihsan
        [0,2],  # Rafly -> Rangga
        [0,3],  # Rafly -> Diaz
        [1,3],  # Ihsan -> Diaz
        [1,4],  # Ihsan -> Aris
        [2,4],  # Rangga -> Aris
        [2,1],  # Rangga -> Ihsan
        [3,4],  # Diaz -> Aris
        [3,0],  # Diaz -> Rafly
        [4,1],  # Aris -> Ihsan
        [4,2]   # Aris -> Rangga
    ]

    # Build the graph using edges
    adj = createGraph_List(V, edges)

    print("Adjacency List Representation:\n")

    for i in range(V):

        # Print the vertex
        print(f"{nodes[i]}:", end=" ")

        for j in adj[i]:

            # Print its adjacent
            print(nodes[j], end=" ")

        print()