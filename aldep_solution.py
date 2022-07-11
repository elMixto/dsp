from model import *
from geometry import *
from matplotlib import pyplot as plt
from numpy import array

cost_matrix = np.ones((10, 10))

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
def tc(distances):
    suma = 0
    for i in range(distances.shape[0]):
        for j in range(distances.shape[1]):
            suma += distances[i, j]*flow_matrix[i, j]*cost_matrix[i, j]
    return suma
external_layout = Polygon.rectangle(Point(0, 0), 500, 500)

departments = {
    Department(1, Polygon.rectangle(Point(0, 300), 100, 200)),
    Department(3, Polygon([Point(0, 0),
                           Point(0, 300),
                           Point(100, 300),
                           Point(100, 50),
                           Point(200, 50),
                           Point(200, 0),
                           Point(0, 0)
                           ])),

    Department(2, Polygon.rectangle(Point(100, 50), 100, 250)),
    Department(1, Polygon.rectangle(Point(0, 300), 100, 200)),
    Department(4, Polygon.rectangle(Point(100, 300), 100, 75)),
    Department(5, Polygon.rectangle(Point(100, 375), 100, 125)),
    Department(6, Polygon.rectangle(Point(200, 375), 100, 125)),
    Department(7, Polygon.rectangle(Point(200, 375), 100, -125)),
    Department(8, Polygon([Point(200, 0),
                           Point(200, 250),
                           Point(300, 250),
                           Point(300, 500),
                           Point(400, 500),
                           Point(400, 0),
                           Point(200, 0), ])),
    Department(10, Polygon.rectangle(Point(400, 400), 100, 100)),
    Department(9, Polygon.rectangle(Point(400, 400), 100, -200)),

}

external_layout.plot()
for d in departments:
    d.plot()
initial_tc = round(tc(distance_matrix(departments)),1)
print(initial_tc)
plt.title(f"TC: {initial_tc}")
plt.savefig("aldep.png",dpi=300)
