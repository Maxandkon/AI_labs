import random

class Vertex:
    def __init__(self, point):
        self.point = point
        self.is_visited = False

class Graph:
    MAX = 4
    Q = 20
    P = 0.1
    
    def __init__(self):
        self.array = [[0] * Graph.MAX for _ in range(Graph.MAX)]
        self.f_on_way = [[0.0] * Graph.MAX for _ in range(Graph.MAX)]
        self.list = [None] * Graph.MAX
        self.cur = 0

    def add_vertex(self, point):
        self.list[self.cur] = Vertex(point)
        self.cur += 1

    def add_edge(self, start, end, val):
        self.array[start - 1][end - 1] = val
        self.array[end - 1][start - 1] = val

    def add_f(self, start, end, val):
        self.f_on_way[start - 1][end - 1] = val
        self.f_on_way[end - 1][start - 1] = val

    def check(self, i):
        return self.list[i].is_visited

    def round(self):
        ways = []
        way = 1
        L = 0
        flag = True

        while flag:
            self.list[way - 1].is_visited = True
            probability = [0.0] * Graph.MAX

            for i in range(Graph.MAX):
                if self.check(i) or self.array[way - 1][i] == 0:
                    continue

                pr = self.calc2(way, i)
                den = 0.0
                for j in range(Graph.MAX):
                    if not self.check(j) and self.array[way - 1][j] != 0:
                        den += self.calc2(way, j)
                pr = pr / den
                probability[i] = pr

            rand_num = random.random()
            res = 0.0
            m = 0

            for f in probability:
                res += f
                if res > rand_num:
                    L += self.array[way - 1][m]
                    break

                m += 1

            ways.append(way)
            way = m + 1
            all_unvisited = sum(not f.is_visited for f in self.list)

            if all_unvisited == 0:
                flag = False

        L += self.array[0][3]
        T = Graph.Q / L
        a = 0

        for i in range(len(ways) - 1):
            self.f_on_way[ways[a] - 1][ways[a + 1] - 1] = (1 - Graph.P) * self.f_on_way[ways[a] - 1][ways[a + 1] - 1] + T
            self.f_on_way[ways[a + 1] - 1][ways[a] - 1] = self.f_on_way[ways[a] - 1][ways[a + 1] - 1]
            a += 1

        print("ways:", ways)
        for v in self.list:
            v.is_visited = False

    def calc(self, way, i):
        return 1.0 / self.array[way - 1][i]

    def calc2(self, way, i):
        return self.f_on_way[way - 1][i] * self.calc(way, i)

if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)

    graph.add_edge(1, 2, 24)
    graph.add_f(1, 2, 1)

    graph.add_edge(1, 3, 5)
    graph.add_f(1, 3, 1)

    graph.add_edge(1, 4, 48)
    graph.add_f(1, 4, 1)

    graph.add_edge(2, 3, 51)
    graph.add_f(2, 3, 1)

    graph.add_edge(2, 4, 3)
    graph.add_f(2, 4, 1)

    graph.add_edge(3, 4, 75)
    graph.add_f(3, 4, 1)

    for i in range(5):
        print("The path of the ant", i + 1, ":")
        graph.round()

    for row in graph.f_on_way:
        print(row)
