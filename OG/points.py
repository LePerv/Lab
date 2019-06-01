import numpy as np
from argparse import ArgumentParser

argumentParser = ArgumentParser('Random points generator')
argumentParser.add_argument('num_points')
args = argumentParser.parse_args()

points = np.random.rand(int(args.num_points), 2)
out = open('input.txt', 'w')
for point in points:
    out.write(str(point[0]) + ' ' + str(point[1]) + '\n')