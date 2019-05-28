import math
import numpy as np 
import matplotlib.pyplot as plt

class ListNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        pass
    
class LinkedList:
    def __init__(self, array):
        self.start = None
        if array:
            while len(array) > 0:
                x = array.pop()
                node = ListNode(x)
                self.add(node)
    
    def add(self, node):
        if self.start:
            last = self.start.right
            last.left = node
            node.right = last
            node.left = self.start
            self.start.right = node
        else:
            self.start = node
            self.start.left = node
            self.start.right = node

    def remove(self, node):
        _node = None
        while _node != self.start:
            if _node is None:
                _node = self.start
            if _node == node:
                l = _node.left
                r = _node.right
                l.right = r
                r.left = l
                if node == self.start:
                    self.start = l
                break
            _node = _node.left

    def length(self):
        result = 0
        node = None
        while node != self.start:
            if node is None:
                node = self.start
            result += 1
            node = node.left
        return result

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

def calculateAngle(left, middle, right):
    v1 = Point(left.x - middle.x, left.y - middle.y)
    v2 = Point(middle.x - right.x, middle.y - right.y)
    
    return math.acos((v1.x * v2.x + v1.y * v2.y) / (math.sqrt(math.pow(v1.x, 2) + math.pow(v1.y, 2)) * math.sqrt(math.pow(v2.x, 2) + math.pow(v2.y, 2))))

def calculateTriangleSquare(t1, t2, t3):
    a = math.sqrt(math.pow(t1.x - t2.x, 2) + math.pow(t1.y - t2.y, 2))
    b = math.sqrt(math.pow(t2.x - t3.x, 2) + math.pow(t2.y - t3.y, 2))
    c = math.sqrt(math.pow(t1.x - t3.x, 2) + math.pow(t1.y - t3.y, 2))
    hp = (a + b + c) / 2

    return math.sqrt(hp * (hp - a) * (hp - b) * (hp - c))

def isPointInTriangle(p, t1, t2, t3):
    s = calculateTriangleSquare(t1, t2, t3)
    s1 = calculateTriangleSquare(p, t1, t2)
    s2 = calculateTriangleSquare(p, t2, t3)
    s3 = calculateTriangleSquare(p, t3, t1)
    
    return math.fabs(s - (s1 + s2 + s3)) < 1e-9

def drawPolygon(points):
    x = []
    y = []
    for point in points:
        x.append(point.x)
        y.append(point.y)
    x = np.array(x)
    y = np.array(y)
    plt.figure()
    plt.fill(x, y, facecolor='none', edgecolor='black', linewidth=1)
    plt.show()

def drawTriangles(triangles):
    plt.figure()
    for triangle in triangles:
        x = np.array([triangle.v1.value[0].x, triangle.v2.value[0].x, triangle.v3.value[0].x])
        y = np.array([triangle.v1.value[0].y, triangle.v2.value[0].y, triangle.v3.value[0].y])
        plt.fill(x, y, facecolor='none', edgecolor='black', linewidth=1)
    plt.show()

def main():
    temp = open('input.txt', 'r')

    points = []
    for line in temp:
        xy = line.split(' ')
        points.append(Point(float(xy[0]), float(xy[1])))
    points = LinkedList(points)
    angles = []
    node = None
    while node != points.start:
        if node is None:
            node = points.start
        angles.append(calculateAngle(node.left.value, node.value, node.right.value))
        node = node.left

    vertices = []
    node = None
    while node != points.start:
        if node is None:
            node = points.start
        vertices.append([node.value, angles.pop()])
        node = node.left
    vertices = LinkedList(vertices)

    result_triangles = []
    work = vertices.start

    while vertices.length() > 2:
        temp_triangles = []
        left = work.left
        right = work.right

        #fisrt check
        v11 = work
        v12 = left
        v13 = left.left
        node1 = left.left.left
        check1 = True
        while node1 != work:
            if isPointInTriangle(node1.value[0], v11.value[0], v12.value[0], v13.value[0]):
                check1 = False
                break
            node1 = node1.left
        if left.value[1] < math.pi and check1:
            temp_triangles.append(Triangle(v11, v12, v13))

        #second check
        v21 = work
        v22 = right
        v23 = right.right
        node2 = right.right.right
        check2 = True
        while node2 != work:
            if isPointInTriangle(node2.value[0], v21.value[0], v22.value[0], v23.value[0]):
                check2 = False
                break
            node2 = node2.right
        if right.value[1] < math.pi and check2:
            temp_triangles.append(Triangle(v21, v22, v23))

        #third check
        v31 = work
        v32 = left
        v33 = right
        node3 = left.left
        check3 = True
        while node3 != right:
            if isPointInTriangle(node3.value[0], v31.value[0], v32.value[0], v33.value[0]):
                check3 = False
                break
            node3 = node3.right
        if work.value[1] < math.pi and check3:
            temp_triangles.append(Triangle(v31, v32, v33))

        if len(temp_triangles) == 0:
            work = work.left
        else:
            min_delta_angle = None
            min_triangle = None
            for x in temp_triangles:
                a1 = calculateAngle(x.v1.value[0], x.v2.value[0], x.v3.value[0])
                a2 = calculateAngle(x.v2.value[0], x.v3.value[0], x.v1.value[0])
                a3 = calculateAngle(x.v3.value[0], x.v1.value[0], x.v2.value[0])
                min_a = min([a1, a2, a3])
                max_a = max([a1, a2, a3])
                delta = max_a - min_a
                if min_delta_angle is None or delta < min_delta_angle:
                    min_delta_angle = delta
                    min_triangle = x
            result_triangles.append(min_triangle)
            trash = min_triangle.v2
            vertices.remove(trash)
            trash.left.value[1] = calculateAngle(left.left.value[0], left.value[0], right.value[0])
            trash.right.value[1] = calculateAngle(left.value[0], right.value[0], right.right.value[0])
            work = trash.left
    
    drawTriangles(result_triangles)


if __name__ == '__main__':
    main()