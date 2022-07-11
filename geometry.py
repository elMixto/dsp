from dataclasses import dataclass
from typing import List
import numpy as np
from matplotlib import pyplot as plt
from functools import lru_cache
from copy import deepcopy

@dataclass(frozen=True)
class Point:
    x: float
    y: float

    @staticmethod
    @lru_cache
    def euclidean_distance(one: "Point",other: "Point"):
        return np.sqrt((one.x-other.x)**2+(one.y-other.y)**2)
    
    @staticmethod
    @lru_cache
    def rectilinear_distance(one: "Point",other: "Point"):
        return (one.x-other.x)+(one.y-other.y)
    
    def extend_y(self,val: float):
        return Point(self.x,self.y+val)
    
    def extend_x(self,val: float):
        return Point(self.x+val,self.y)
    
    def copy(self):
        return Point(self.x, self.y)
    @staticmethod
    def direction(one:"Point",other:"Point")->"Point":
        x_salida = 0
        y_salida = 0
        if one.y == other.y:
            x_salida =  (one.x-other.x)/abs(one.x-other.x)
        elif one.x == other.x:
            y_salida =  (one.y-other.y)/abs(one.y-other.y)
        else:
            return None
        return Point(int(x_salida), int(y_salida))



@dataclass
class Polygon:
    points: List[Point]
    
    def rotate(self):
        self.points = self.points[-1:] + self.points[:-1]
    def rotate2(self):
        self.points = self.points[1:] + self.points[:1]
    
    def area(self):
        get_info = lambda x1,x2: x1.x*x2.y - x1.y*x2.x
        points = self.points
        N = len(points)
        x2 = points[0]
        x1 = x2
        res = 0
        for i in range(1, N):
           nx = points[i]
           res = res + get_info(x1,nx)
           x1 = nx
        res = res + get_info(x1,x2)
        return abs(res)/2.0
    @property
    def without_last(self):
        return Polygon(self.points[:len(self.points)-1])
    
    @property
    def centroid(self)->Point:
     _x_list = [p.x for p in self.points]
     _y_list = [p.y for p in self.points]
     _len = len(self.points)
     x = sum(_x_list) / _len
     y = sum(_y_list) / _len
     return Point(x, y)

    @classmethod
    def rectangle(cls,pos: Point,ancho: float,alto: float):
        return Polygon([pos,pos.extend_y(alto),pos.extend_y(alto).extend_x(ancho),pos.extend_x(ancho),pos])

    def plot(self):
        plt.plot([p.x for p in self.points],[p.y for p in self.points])
    @staticmethod 
    def adyacentes(self: "Polygon",other:"Plygon")->bool:
        for i in range(1,len(self.points)):
            pair1 = (self.points[i-1].copy(),self.points[i].copy())
            for j in range(2,len(other.points)-1):
                pair2 = (other.points[j-1].copy(),other.points[j].copy())
                equal_x = (pair1[0].x == pair1[1].x) and (pair2[0].x == pair2[1].x) and (pair2[0].x == pair1[0].x)
                equal_y = ((pair1[0].y == pair1[1].y) and (pair2[0].y == pair2[1].y) and (pair2[0].y == pair1[0].y))
                return True
        return False
        
    
    def __add__(self: "Polygon",other:"Plygon")->"Polygon":
        is_between = lambda a,b: a[0] <= a[1] <= b[0] or a[0] <= b[1] <= b[0] or a[1] <= a[0] <= b[1] or a[1] <= b[0] <= b[1]
        is_between2 = lambda a,b: a[0] >= a[1] >= b[0] or a[0] >= b[1] >= b[0] or a[1] >= a[0] >= b[1] or a[1]>= b[0] >= b[1]
        counter = 0

        for i in range(len(self.points)-1):
            p1 = (self.points[i-1].copy(),self.points[i].copy())
            for j in range(len(other.points)-1):
                p2 = (other.points[j-1].copy(),other.points[j].copy())
                
                if (p1[0].x == p1[1].x) and (p2[0].x == p2[1].x) and (p2[0].x == p1[0].x) or ((p1[0].y == p1[1].y) and (p2[0].y == p2[1].y) and (p2[0].y == p1[0].y)):
                        #Checkear si se intersectan
                        return Polygon(bigger.points+smaller.points+[bigger.points[0]])
                            
                        
                        
                    