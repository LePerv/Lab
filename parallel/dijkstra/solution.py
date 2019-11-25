# import gmpy2
from Pyro4 import expose
import random


def dijkstra(weights, v):
    INFINITY = float('inf')
    a = v
    n = len(weights)
    distances = [INFINITY for x in range(0, n)]
    visited = [False for x in range(0, n)]

    distances[a] = 0

    while False in visited:
        for i in range(0, n):
            if weights[a][i] != 0 and not visited[i]:
                current = weights[a][i] + distances[a]
                if distances[i] > current:
                    distances[i] = current

        visited[a] = True

        min_index = -1
        min_distance = INFINITY
        for i in range(0, n):
            if distances[i] < min_distance and not visited[i]:
                min_index = i
                min_distance = distances[i]

        if min_index != -1:
            a = min_index
        else:
            break

    return distances

class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers
        print("Inited")

    def solve(self):
        print("Job Started")
        print("Workers %d" % len(self.workers))

        weights = self.read_input()
        n = len(weights)
        step = n / len(self.workers)

        # map
        mapped = []
        for i in xrange(0, len(self.workers)):
            mapped.append(self.workers[i].mymap(i * step, i * step + step, weights))

        # reduce
        distances = self.myreduce(mapped)

        # output
        self.write_output(distances)

        print("Job Finished")

    @staticmethod
    @expose
    def mymap(a, b, weights):
        res = []
        for i in xrange(a, b):
            res.append(dijkstra(weights, i))
        return res

    @staticmethod
    @expose
    def myreduce(mapped):
        print("reduce")
        output = []

        for x in mapped:
            print("reduce loop")
            output.extend(x.value)
        print("reduce done")
        return output

    def read_input(self):
        f = open(self.input_file_name, 'r')
        weights = []
        for line in f.readlines():
            weights.append([int(x) for x in line.split(' ')])
        f.close()
        return weights

    def write_output(self, output):
        f = open(self.output_file_name, 'w')
        f.write(str(output))
        f.close()
        print("output done")
