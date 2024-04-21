class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.d={}
        self.visited = [False]*n
        def search(source):
            self.visited[source] = True
            if source == destination:
                return True
            
            for newEdge in self.d[source]:
                if self.visited[newEdge]==False and search(newEdge):
                    return True
            return False

        for i in edges:
            if i[0] in self.d:
                self.d[i[0]].append(i[1])
            else:
                self.d[i[0]] = [i[1]]
            if i[1] in self.d:
                self.d[i[1]].append(i[0])
            else:
                self.d[i[1]] = [i[0]]
        
        return search(source)  