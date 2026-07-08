import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        
        if self.rank[rx] < self.rank[ry]:
            temp = rx
            rx = ry
            ry = temp
            
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] = self.rank[rx] + 1
        return True

def kruskal_algo(n, edge_list):
    edge_list.sort()
    uf = UnionFind(n)
    mst_edges = []
    total_cost = 0
    
    for item in edge_list:
        w = item[0]
        u = item[1]
        v = item[2]
        if uf.union(u, v) == True:
            mst_edges.append((u, v, w))
            total_cost = total_cost + w
            
        if len(mst_edges) == n - 1:
            break
            
    return mst_edges, total_cost

def prim_algo(n, adj_graph, start):
    inf_val = 999999
    key = [inf_val] * n
    parent = [-1] * n
    in_mst = [False] * n
    
    key[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    mst_edges = []
    total_cost = 0
    
    while len(pq) > 0:
        curr = heapq.heappop(pq)
        w = curr[0]
        u = curr[1]
        
        if in_mst[u] == True:
            continue
            
        in_mst[u] = True
        if parent[u] != -1:
            mst_edges.append((parent[u], u, w))
            total_cost = total_cost + w
            
        if u in adj_graph:
            neighbors = adj_graph[u]
            for edge in neighbors:
                v = edge[0]
                wt = edge[1]
                if in_mst[v] == False:
                    if wt < key[v]:
                        key[v] = wt
                        parent[v] = u
                        heapq.heappush(pq, (wt, v))
                        
    return mst_edges, total_cost

if __name__ == "__main__":
    num_nodes = 7
    edges = [
        (7, 0, 1), (5, 0, 3), (8, 1, 2), (9, 1, 3),
        (7, 1, 4), (5, 2, 4), (15, 3, 4), (6, 3, 5),
        (8, 4, 5), (9, 4, 6), (11, 5, 6)
    ]
    
    graph = {}
    for edge in edges:
        w = edge[0]
        u = edge[1]
        v = edge[2]
        
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))
        
        if v not in graph:
            graph[v] = []
        graph[v].append((u, w))
        
    k_mst, k_cost = kruskal_algo(num_nodes, edges[:])
    p_mst, p_cost = prim_algo(num_nodes, graph, 0)
    
    print("=== Kruskal's MST ===")
    for edge in k_mst:
        u = edge[0]
        v = edge[1]
        w = edge[2]
        print(f" Edge ({u} - {v}) Weight: {w}")
    print(f" Total MST Cost: {k_cost}\n")
    
    print("=== Prim's MST ===")
    for edge in p_mst:
        u = edge[0]
        v = edge[1]
        w = edge[2]
        print(f" Edge ({u} - {v}) Weight: {w}")
    print(f" Total MST Cost: {p_cost}")