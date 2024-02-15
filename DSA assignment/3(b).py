# Class to represent a graph edge
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

# Class to represent a subset for union-find
class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

class KruskalAlgorithm:
    def __init__(self, v, e):
        self.V = v
        self.E = e
        self.edges = [Edge(0, 0, 0) for _ in range(e)]

    # Function to find the set of an element 'i'
    def find(self, subsets, i):
        if subsets[i].parent != i:
            subsets[i].parent = self.find(subsets, subsets[i].parent)
        return subsets[i].parent

    # Function that does union of two sets of x and y
    def union(self, subsets, x, y):
        xroot = self.find(subsets, x)
        yroot = self.find(subsets, y)

        # Attach smaller rank tree under the root of the high rank tree
        if subsets[xroot].rank < subsets[yroot].rank:
            subsets[xroot].parent = yroot
        elif subsets[xroot].rank > subsets[yroot].rank:
            subsets[yroot].parent = xroot
        else:
            subsets[yroot].parent = xroot
            subsets[xroot].rank += 1

    # Function to construct MST using Kruskal's algorithm
    def kruskal_mst(self):
        result = [Edge(0, 0, 0) for _ in range(self.V)]  # This will store the resultant MST
        e = 0  # An index variable, used for result[]
        i = 0  # An index variable, used for sorted edges
        for i in range(self.V):
            result[i] = Edge(0, 0, 0)

        # Step 1: Sort all the edges in non-decreasing order of their weight
        self.edges.sort(key=lambda x: x.weight)

        # Allocate memory for creating V subsets
        subsets = [Subset(i, 0) for i in range(self.V)]

        i = 0  # Index used to pick the next edge

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            # Step 2: Pick the smallest edge. Increment the index for the next iteration
            next_edge = self.edges[i]
            i += 1

            x = self.find(subsets, next_edge.src)
            y = self.find(subsets, next_edge.dest)

            # If including this edge doesn't cause a cycle, include it in the result and increment the index
            # of the result for the next edge
            if x != y:
                result[e] = next_edge
                e += 1
                self.union(subsets, x, y)

        # Print the edges of MST
        print("Following are the edges in the constructed MST:")
        minimum_cost = 0
        for i in range(e):
            print(f"{result[i].src} -- {result[i].dest} == {result[i].weight}")
            minimum_cost += result[i].weight
        print(f"Minimum Cost Spanning Tree: {minimum_cost}")


# Main class
if __name__ == "__main__":
    V = 4  # Number of vertices in the graph
    E = 5  # Number of edges in the graph
    graph = KruskalAlgorithm(V, E)

    # Add edge 0-1
    graph.edges[0] = Edge(0, 1, 10)
    # Add edge 0-2
    graph.edges[1] = Edge(0, 2, 6)
    # Add edge 0-3
    graph.edges[2] = Edge(0, 3, 5)
    # Add edge 1-3
    graph.edges[3] = Edge(1, 3, 15)
    # Add edge 2-3
    graph.edges[4] = Edge(2, 3, 4)

    # Function call to find the minimum spanning tree
    graph.kruskal_mst()
