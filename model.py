from dataclasses import dataclass
from geometry import Point,Polygon
from matplotlib import pyplot as plt

@dataclass
class Department:
    
    number: int
    polygon: Polygon
    
    def __hash__(self):
        return hash(self.number)
    
    def plot(self):
        c = self.polygon.centroid
        plt.text(c.x, c.y, str(self.number),
                 horizontalalignment='center',
                 verticalalignment="center"
                 )
        self.polygon.plot()
        
    