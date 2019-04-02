class Cell:
    def __init__(self, neighbourhood:list, properties={}, agents=[]):
        self.neighbourhood = neighbourhood
        self.properties = properties
        self.agents = agents
        