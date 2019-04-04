class Cell:
    def __init__(self, neighbourhood:list, properties={}, agents=[]):
        self.neighbourhood = neighbourhood
        self.properties = properties
        self.agents = agents
        
class Cell_Grid:
    def __init__(self, rows:int, columns:int ):
        self.rows = rows
        self.columns = columns
        self.cells=[[Cell([],{},[]) for _ in range(self.columns)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                self.cells[i][j].properties['grid_position']= [i, j]     
    
    def Moore_nh(self, gridposition:list, radius:int):
        result=[]
        u= [gridposition[0] - radius , gridposition[1] - radius]
        for i in range(2*radius + 1):
            for j in range(2*radius + 1):
                result.append([u+i,u+j])
        return result

    def vonNeumann_nh(self, radius:int):
        pass

    def __str__(self):
        output = self.columns*" ___" + "\n"
        for _ in range(self.rows):
            for i in range(self.columns):   
                output += "|___"
                if i==self.columns-1:
                    output += "|"
            output += "\n"
        return "".join(output)

grid = Cell_Grid(10,10)
print(grid)