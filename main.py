from numpy import array, tensordot
import numpy as np
from pprint import pprint as pp
from geometry import Polygon, Point
from matplotlib import pyplot as plt
from model import Department
import itertools
from copy import deepcopy

n = 10
zero = 0
cost_matrix = np.ones((n, n))

flow_matrix = array([[0, 50, 70, 35, 40, 7, 4, 3, 2, 5],
                     [0, 0, 75, 25, 8, 2, 1, 1, 2, 1],
                     [0, 0, 0, 50, 50, 3, 1, 1, 2, 1],
                     [0, 0, 0, 0, 60, 5, 7, 3, 2, 65],
                     [0, 0, 0, 0, 0, 30, 7, 7, 2, 3],
                     [0, 0, 0, 0, 0, 0, 45, 8, 2, 2],
                     [0, 0, 0, 0, 0, 0, 0, 75, 2, 15],
                     [0, 0, 0, 0, 0, 0, 0, 0, 2, 60],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

flow_matrix = flow_matrix + flow_matrix.transpose()
print(flow_matrix)


def tc(distances):
    suma = 0
    for i in range(distances.shape[0]):
        for j in range(distances.shape[1]):
            suma += distances[i, j]*flow_matrix[i, j]*cost_matrix[i, j]
    return suma


layout_h = 500
layout_w = 500
external_layout = Polygon.rectangle(Point(0, 0), 500, 500)

# In order
departments = {
    Department(7, Polygon.rectangle(Point(0, 150), 100, 137.5)),
    Department(8, Polygon([Point(0, 287.5),Point(0, 500),Point(200, 500),Point(200, 375),
                           Point(100, 375),Point(100, 287.5),Point(0,287.5)])),
    Department(6, Polygon.rectangle(Point(0, 25), 100, 125)),
    Department(10, Polygon.rectangle(Point(200, layout_h-100), 100, 100)),
    Department(2, Polygon.rectangle(Point(300, layout_h-150), 150, 150)),
    Department(4, Polygon([Point(357.5, 0),Point(357.5, 200),Point(400, 200),Point(400, 275),Point(500, 275),Point(500, 0),Point(357.5, 0)],)),
    Department(3, Polygon([Point(325, 0),Point(325, 200),Point(357.5, 200),Point(357, 0),Point(325, 0)],)),
    Department(1, Polygon.rectangle(Point(150, 200), 100, 100)),
    Department(9, Polygon.rectangle(Point(125, 0), 200, 100)),
    Department(5, Polygon.rectangle(Point(125, 100), 125, 100)),
}
print(list(departments)[0].polygon.points)
areas_originales = {d.number: d.polygon.area() for d in departments}


# Falta colocar el TC inicial
external_layout.plot()
for i, d in enumerate(departments):
    d.plot()





def distance_matrix(departments):
    departments = list(departments)
    distance_matrix = np.zeros((len(departments), len(departments)))
    for i in range(distance_matrix.shape[0]):
        for j in range(distance_matrix.shape[1]):
            distance = Point.euclidean_distance(
                departments[i].polygon.centroid,
                departments[j].polygon.centroid)
            distance_matrix[i, j] = distance
    return distance_matrix


# We define departments as a dictionary, this way we can indexit

# Now we have all the matrices necesary to make this crap
initial_tc = round(tc(distance_matrix(departments)),1)
print(initial_tc)
plt.title(f"TC: {initial_tc}")
plt.savefig("entrada.png",dpi=300)

def execute_best_permutation(departments):
    #Solo los departamentos adyacentes y departamentos con igual area son válidos
    departments = list(departments)
    permutations_of_departments = list(itertools.permutations(range(len(departments)), r=2))
    old_tc = initial_tc
    best = None
    for ab in permutations_of_departments:
        da = departments[ab[0]]
        db = departments[ab[1]]
        if (da.number,db.number) in [(1,4),(4,1),(4,9),(9,4)]:
                continue
        if not ( Polygon.adyacentes(da.polygon,db.polygon) or da.polygon.area() == db.polygon.area()):
            continue
        a, b = ab
        # copy the departmentes
        nd = deepcopy(departments)
        na = nd[a]
        nb = nd[b]
        na.number = b + 1
        nb.number = a + 1
        nd[a], nd[b] = nd[b], nd[a]
        # Now i have to interchangethem manually
        new_tc = tc(distance_matrix(nd))
        if new_tc < old_tc:
            best = nd.copy()
            
            best_a = nd[a]
            best_b = nd[b] 
            old_tc = new_tc

    return best,best_a,best_b

best,a,b = execute_best_permutation(departments)
print(a.number,a.polygon.area(),b.polygon.area(), b.number)

#external_layout.plot()
# central_corridor.plot()
plt.savefig("salida2.png")
